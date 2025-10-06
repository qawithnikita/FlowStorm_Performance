from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    host = "http://localhost:8000"

    @task
    def hello_world(self):
        response = self.client.get("/hello")
        uid = response.cookies.get("uid")
        if uid:
            self.client.get("/world", cookies={"uid": uid})

    @task
    def handle_route(self):
        resp = self.client.get("/hello")
        data = resp.json()
        self.client.get(data['route'])

    @task
    def check_uid(self):
        response = self.client.get("/hello")
        uid = response.cookies.get("uid")
        resp = self.client.get("/check-uid", cookies={"uid": uid})
        print("Check uid response:", resp.text)

        