from locust import FastHttpUser, task, between

class BaseUser(FastHttpUser):
    wait_time = between(1, 2)
    host = "http://localhost:8000"

    def get_uid(self):
        response = self.client.get("/hello")
        return response.cookies.get("uid")

# 1) Guest profile: goes to /world
class GuestUser(BaseUser):
    @task(2)
    def visit_world(self):
        uid = self.get_uid()
        if uid:
            self.client.get("/world", cookies={"uid": uid})

# 2) Logged-in profile: verifies uid
class LoggedInUser(BaseUser):

    @task
    def check_uid(self):
        uid = self.get_uid()
        if uid:
            response = self.client.get("/check-uid", cookies={"uid": uid})
            print("uid Check Response:", response.text)


  