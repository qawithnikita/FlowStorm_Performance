from locust import FastHttpUser, task, between
import uuid
from datetime import datetime, timezone
from src.locust_tests.helpers.api import APIClient
from src.locust_tests.helpers.orgs import OrgGenerator
from src.config import BaseConfig


class BasicFlowUser(FastHttpUser):
    
    wait_time = between(BaseConfig.MIN_WAIT, BaseConfig.MAX_WAIT)  
    host = BaseConfig.HOST  

    def on_start(self):
        OrgGenerator.init()  
        self.user_id = f"test-user-id-{uuid.uuid4()}" 
        self.org = OrgGenerator.generate_org()  
        self.org_id = self.org['org']['id'] 
        self.org_short_name = self.org['org']['short_name']  

    @task
    def basic_flow(self):
    
        APIClient.call_org_configs(client=self.client, user_id=self.user_id)

        APIClient.call_supported_event( 
            client=self.client, 
            org_id=self.org_id,
            org_short_name=self.org_short_name
        )

        APIClient.call_session_messages(
            client=self.client,
            org_id=self.org_id
        )

        APIClient.call_next_responses(client=self.client)

        APIClient.call_next_suggestions(client=self.client)