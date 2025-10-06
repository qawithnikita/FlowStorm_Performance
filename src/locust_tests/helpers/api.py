import uuid
from datetime import datetime
from src.config import BaseConfig

class APIClient:
    sessions = {}

    @classmethod
    def _init_session(cls, org_id):
        if org_id not in cls.sessions:
            cls.sessions[org_id] = {
                "chat_id": str(uuid.uuid4()),
                "user_id": f"app-user-id-{uuid.uuid4()}"
            }
        return cls.sessions[org_id]

    @classmethod
    def call_org_configs(cls, client, user_id):
        url="/org/configs"
        params = { 
            "namespace": "test-namespace",
            "source": "playground",
            "user_id": user_id,
            "include_experiments": "default",
            "include_feature_gates": [
               "is_client_session_enabled",
               "is_new_feature_enabled",
               "is_fine_tuned_model_8b",
               "is_integrated_cx_enabled",
               "is_non_shapewear_enabled",
               "is_force_injection_enabled",
               "is_image_banner_enabled",
               "is_search_hash_enabled"
            ]
        }

        with client.get(url, params=params, name="GET /org/configs", catch_response=True) as response:
            data = {}
            try:
                data = response.json()
            except ValueError:
                data = {}
            return {
                 "status": response.status_code, 
                 "data": data  
            }


    @classmethod
    def call_supported_event(cls, client, org_id, org_short_name):
        session = cls._init_session(org_id)
        url = "/supported_event"
        payload = {
            "context": {
                "chat_id": session["chat_id"],
                "env": "prod",
                "org_id": org_id,
                "org_short_name": org_short_name,
                "source": "playground",
                "user_id": session["user_id"]
            },
            "id": str(uuid.uuid4()),
            "user_event": {
                "attributes": {
                    "attributes": {
                        "id": "stockpots"
                    },
                    "category": "id"
                },
                "category": "plp_visit",
                "created_at": datetime.utcnow().isoformat(timespec='milliseconds') + 'Z',
                "event_id": str(uuid.uuid4())
            }
        }

        with client.post(url, json=payload, name="POST /supported_event", catch_response=True) as response:
            data = {}
            try:
                data = response.json()
            except ValueError:
                data = {}
            return {
                "status": response.status_code, 
                "data": data
            }


    @classmethod
    def call_session_messages(cls, client, org_id):
        session = cls._init_session(org_id)
        url = "/session/messages"

        params = {
            "org_id": org_id,
            "chat_id": session["chat_id"],
            "user_id": session["user_id"] 
        }

        with client.post(url, params=params, name="POST /session/messages", catch_response=True) as response:
            data = {}
            try:
                data = response.json()
            except ValueError:
                data = {}
            return {
                "status": response.status_code,  
                "data": data
            }
    @classmethod
    def call_next_responses(cls, client, payload=None):
        url = "/next_responses"
        with client.post(url, json=payload or {}, name="POST /next_responses", catch_response=True) as response:
            data = {}
            try:
                data = response.json()
            except ValueError:
                data = {}
            return {
                "status": response.status_code, 
                "data": data
            }

    @classmethod
    def call_next_suggestions(cls, client, payload=None):
        url = "/next_suggestions"
        with client.post(url, json=payload or {}, name="POST /next_suggestions", catch_response=True) as response:
            data = {}
            try:
                data = response.json()
            except ValueError:
                data = {}
            return {
                "status": response.status_code, 
                "data": data
            }


    @classmethod
    def call_track_event(cls, client, org_id):
        session = cls._init_session(org_id)
        url = "/analytics/track_event"
        payload = {  
            "event_name": "user_click",
            "user_id": session["user_id"],
            "timestamp": datetime.utcnow().isoformat(timespec='milliseconds') + "Z",
            "properties": {
                "button": "buy_now",
                "page": "/products/123"
            }
        }

        with client.post(url, json=payload, name="POST /analytics/track_event", catch_response=True) as response:
            data = {}
            try:
                data = response.json()
            except ValueError:
                data = {}
            return {
                "status": response.status_code,  
                "data": data
            }