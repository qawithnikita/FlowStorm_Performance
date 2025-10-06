from bottle import post, response
import uuid
import json
from datetime import datetime

@post('/next_suggestions')
def next_suggestions():
    """
    Mock /next_suggestions endpoint to simulate chatbot's suggested user actions.
    
    """

    response.content_type = 'application/json'

    # List of possible next chatbot suggestions
    suggestions_data = [
        {
            "suggestion_id": str(uuid.uuid4()),
            "text": "View account details",
            "confidence": 0.97,
            "suggested_action": "view_account"
        },
        {
            "suggestion_id": str(uuid.uuid4()),
            "text": "Check order status",
            "confidence": 0.95,
            "suggested_action": "check_order"
        },
        {
            "suggestion_id": str(uuid.uuid4()),
            "text": "Explore new products",
            "confidence": 0.92,
            "suggested_action": "browse_products"
        }
    ]

    response_body = {
        "request_id": str(uuid.uuid4()),
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "status": "success",
        "next_suggestions": suggestions_data,
        "message": "Mock chatbot suggestions for load testing"
    }

    return json.dumps(response_body)
