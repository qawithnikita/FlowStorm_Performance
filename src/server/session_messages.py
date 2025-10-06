from bottle import request, response
import json

chat_sessions = {}

def session_messages():
    """
    Mock endpoint for /session/messages that validates query parameters
    and simulates session storage.
    """
    # Extracting query params from the request URL
    org_id = request.query.get("org_id")
    chat_id = request.query.get("chat_id")
    user_id = request.query.get("user_id")

    # Validate required query params
    if not all([org_id, chat_id, user_id]):
        response.status = 400
        return json.dumps({"error": "Missing query parameters: org_id, chat_id, user_id"})

    # First time this chat_id is seen
    if chat_id not in chat_sessions:
        # Store the chat_id as seen
        chat_sessions[chat_id] = {
            "org_id": org_id,
            "user_id": user_id
        }
        response.status = 502
        return ""  # Return empty body 
    # Subsequent call: return the dummy JSON response
    response.content_type = "application/json"
    dummy_response = {
        "message": "This is a response for subsequent calls to /session/messages",
        "chat_id": chat_id,
        "org_id": org_id,
        "user_id": user_id
    }
    return json.dumps(dummy_response)

