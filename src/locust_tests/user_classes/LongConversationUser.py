from locust import task, FastHttpUser, between
import uuid
from datetime import datetime, timezone
from faker import Faker
from src.locust_tests.helpers.orgs import OrgGenerator
from src.locust_tests.helpers.api import APIClient
from src.config import BaseConfig

fake = Faker()

class LongConversationUser(FastHttpUser):
    wait_time = between(BaseConfig.MIN_WAIT, BaseConfig.MAX_WAIT)
    host = BaseConfig.HOST 

    def on_start(self):
        OrgGenerator.init()
        self.user_id = f"test-user-id-{uuid.uuid4()}"
        self.org = OrgGenerator.generate_org()
        self.org_id = self.org["org"]["id"]
        self.org_short_name = self.org["org"]["short_name"]

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

    @task
    def long_conversation_flow(self):
        for i in range(1, 21):
            payload = {
                "context": {
                    "chat_id": self.chat_id,
                    "env": "prod",
                    "org_id": self.org_id,
                    "org_short_name": self.org_short_name,
                    "source": "playground",
                    "user_id": self.user_id
                },
                "generation_params": {
                    "num_suggestions": 3,
                    "stream": True
                },
                "id": str(uuid.uuid4()),
                "user_events": [
                    {
                        "attributes": {
                            "query": fake.sentence()
                        },
                        "category": "query_typed",
                        "created_at": datetime.now(timezone.utc).isoformat(),
                        "event_id": str(uuid.uuid4())
                    }
                ]
            }

            APIClient.call_next_responses(client=self.client)
                    
            APIClient.call_next_suggestions(client=self.client)
