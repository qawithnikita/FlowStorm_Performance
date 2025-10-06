from bottle import post, request, response
import uuid
import json
from datetime import datetime

@post('/analytics/track_event')
def track_event():
    """
    Mock /analytics/track_event endpoint to simulate event tracking by a chatbot.

    """

    response.content_type = 'application/json'

    #  Parse JSON request
    try:
        data = request.json

        # Validate if JSON body exists
        if not data:
            response.status = 400
            return json.dumps({"error": "Missing JSON body in request"})

        # Validate required fields
        required_fields = ["event_name", "user_id", "timestamp"]
        for field in required_fields:
            if field not in data:
                response.status = 400
                return json.dumps({"error": f"Missing required field: {field}"})


        response_body = {
            "event_id": str(uuid.uuid4()),
            "status": "success",
            "received_at": datetime.utcnow().isoformat() + "Z",
            "message": "Mock analytics event tracked successfully"
        }

        return json.dumps(response_body)

    except Exception as e:
        response.status = 500
        return json.dumps({"error": f"Internal Server Error: {str(e)}"})
