from bottle import post, response
import uuid
import json
from datetime import datetime

@post('/next_responses')
def next_responses():
    """
   mock /next_responses endpoint to simulate chatbot's next possible responses.

    """

    response.content_type = 'application/json'

    # list of possible next chatbot replies
    next_responses_data = [
        {
            "response_id": str(uuid.uuid4()),
            "text": "Can I help you find something else?",
            "confidence": 0.98,
            "suggested_action": "show_categories"
        },
        {
            "response_id": str(uuid.uuid4()),
            "text": "Do you want to know the latest offers?",
            "confidence": 0.95,
            "suggested_action": "show_offers"
        },
        {
            "response_id": str(uuid.uuid4()),
            "text": "Would you like to speak to customer support?",
            "confidence": 0.90,
            "suggested_action": "connect_support"
        }
    ]

    response_body = {
        "request_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "success",
        "next_responses": next_responses_data,
        "message": "Dummy next chatbot responses for load testing"
    }

    return json.dumps(response_body)
