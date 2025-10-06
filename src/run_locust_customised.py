import os
import gevent
from locust import FastHttpUser, task, between
from locust.env import Environment
from locust.log import setup_logging
from locust.stats import stats_history, StatsCSVFileWriter
from locust.util.timespan import parse_timespan

class DummyUser(FastHttpUser):
    wait_time = between(1, 2)

    @task
    def hello(self):
        self.client.get("/hello")

def main():
    report_dir = "reports/test_run"
    os.makedirs(report_dir, exist_ok=True)

    setup_logging("INFO")

    env = Environment(user_classes=[DummyUser], host="http://localhost:8080")
    env.create_local_runner()


    csv_writer = StatsCSVFileWriter(
        environment=env,
        base_filepath=os.path.join(report_dir, "report"),
        full_history=True,
        percentiles_to_report=[0.5, 0.95, 0.99]
    )

    gevent.spawn(csv_writer)
    gevent.spawn(stats_history, env.runner)

    env.runner.start(user_count=5, spawn_rate=2)
    gevent.spawn_later(parse_timespan("10s"), env.runner.quit)

    env.runner.greenlet.join()

    print("[INFO] Reports generated in:", report_dir)

if __name__ == "__main__":
    main()
