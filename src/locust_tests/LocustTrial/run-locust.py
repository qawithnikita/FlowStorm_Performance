from locust.env import Environment
from src.locust_tests.user_profile import GuestUser, LoggedInUser
import gevent

env = Environment(user_classes=[GuestUser, LoggedInUser])
runner = env.create_local_runner()
runner.start(user_count=4, spawn_rate=2)
gevent.sleep(10)
runner.quit()


print("\n Test complete")
print(f"Total requests made: {env.stats.total.num_requests}")
print(f"Failures: {env.stats.total.num_failures}")
print(f"Average response time: {env.stats.total.avg_response_time:.2f} ms")

