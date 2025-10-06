from locust import FastHttpUser, task, between
from src.locust_tests.helpers.api import APIClient
from src.locust_tests.helpers.orgs import OrgGenerator

class SupportedEventUser(FastHttpUser):
    wait_time = between(1,5)

    def on_start(self):
        OrgGenerator.init()
        org = OrgGenerator.generate_org()
        self.org_id = org["org"]["id"]
        self.org_short_name = org["org"]["short_name"]
        
        APIClient.call_session_messages(self.client, self.org_id)


    @task
    def supported_event_test(self):
        APIClient.call_supported_event(self.client, self.org_id,self.org_short_name)

    @task
    def session_messages_test(self):
        APIClient.call_session_messages(self.client, self.org_id)

    @task
    def next_responses_test(self):
        APIClient.call_next_responses(self.client)


    @task
    def next_suggestions_test(self):
        APIClient.call_next_suggestions(self.client)

    @task
    def analytic_track_event_test(self):
         APIClient.call_track_event(self.client)
        
