import os
import gevent
from locust import FastHttpUser, events, task
from locust.env import Environment
from locust.log import setup_logging
from locust.stats import stats_printer, stats_history
from locust.util.timespan import parse_timespan
import subprocess
from src.config import BaseConfig
from src.locust_tests.user_classes.BasicFlowUser import BasicFlowUser
from src.locust_tests.user_classes.LongConversationUser import LongConversationUser
from src.locust_tests.user_classes.PartialFlowUser import PartialFlowUser

setup_logging(BaseConfig.LOG_LEVEL)

def main():
    os.makedirs(BaseConfig.REPORT_FOLDER, exist_ok=True)
    print(f"[INFO] Reports will be saved to: {BaseConfig.REPORT_FOLDER}")

    env = Environment(
        user_classes=[BasicFlowUser, LongConversationUser, PartialFlowUser],
        events=events,
        host=BaseConfig.HOST
    )

    env.create_local_runner()
    web_ui = env.create_web_ui("127.0.0.1", 8080)

    env.events.init.fire(environment=env, runner=env.runner, web_ui=web_ui)

    gevent.spawn(stats_printer(env.stats))
    gevent.spawn(stats_history, env.runner)

    env.runner.start(user_count=BaseConfig.USERS, spawn_rate=BaseConfig.SPAWN_RATE)

    run_duration = parse_timespan(BaseConfig.RUN_TIME)
    gevent.spawn_later(run_duration, env.runner.quit)

    env.runner.greenlet.join()
    
    web_ui.stop()
    print("[INFO] Load test completed.")

    generate_reports_with_subprocess()

def generate_reports_with_subprocess():
    print("[INFO] Generating reports using subprocess...")

    command = [
        "locust",
        "-f", __file__,
        "--headless",
        "-u", str(BaseConfig.USERS),
        "-r", str(BaseConfig.SPAWN_RATE),
        "--host", BaseConfig.HOST,
        "--run-time", BaseConfig.RUN_TIME,
        "--csv", os.path.join(BaseConfig.REPORT_FOLDER, "report"),
        "--html", os.path.join(BaseConfig.REPORT_FOLDER, BaseConfig.HTML_REPORT),
        "--exit-code-on-error", "0"
    ]

    env = os.environ.copy()
    env["LOCUST_RUN_MODE"] = "report"  

    result = subprocess.run(command, env=env)

    if result.returncode == 0:
        print("[INFO] Reports generated successfully.")
    else:
        print("[ERROR] Failed to generate reports. Exit code:", result.returncode)

if __name__ == "__main__":
    main()
