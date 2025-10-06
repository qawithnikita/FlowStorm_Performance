from locust import task, FastHttpUser, between
import uuid
from src.locust_tests.helpers.orgs import OrgGenerator
from src.locust_tests.helpers.api import APIClient
from src.config import BaseConfig

class PartialFlowUser(FastHttpUser):
    wait_time = between(BaseConfig.MIN_WAIT, BaseConfig.MAX_WAIT)
    host = BaseConfig.HOST

    def on_start(self):
        OrgGenerator.init()
        self.user_id = f"test-user-id-{uuid.uuid4()}"
        self.chat_id = str(uuid.uuid4())
        self.org = OrgGenerator.generate_org()
        self.org_id = self.org["org"]["id"]
        self.org_short_name = self.org["org"]["short_name"]

        APIClient.call_org_configs(client=self.client, user_id=self.user_id)

        APIClient.call_supported_event(
            client=self.client,
            org_id=self.org_id,
            org_short_name=self.org_short_name
        )

    @task
    def idle_task(self):
        print(f"[PartialFlowUser] User {self.user_id} is idle after partial init flow.")
        self.wait()
 
