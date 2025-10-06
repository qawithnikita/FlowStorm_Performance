from bottle import route, request, HTTPError, HTTPResponse
import json
from datetime import datetime, timezone
import uuid


def abort(status_code, error_message):
    """
    Abort the current request and return a JSON response with the error message and HTTP status code.

    Args:
        status_code (int): The HTTP status code.
        error_message (str): The error message.

    Returns:
        HTTPResponse: A JSON response with the error message and HTTP status code.
    """
    response_body = {"error": error_message, "status_code": status_code}
    return HTTPResponse(
        body=json.dumps(response_body),
        status=status_code,
        headers={"Content-Type": "application/json"},
    )


def supported_event():
    """
    Mock endpoint for supported_event that validates request shape and returns generic response
    """
    try:
        # Parse JSON request
        data = request.json

        # Validate request structure
        if not isinstance(data, dict):
            return abort(400, "Request body must be a JSON object")

        # Validate required top-level fields
        required_fields = ["context", "id", "user_event"]
        for field in required_fields: 
            if field not in data:
                return abort(400, f"Missing required field: {field}")

        # Validate context structure
        context = data["context"]
        if not isinstance(context, dict):
            return abort(400, "Context must be an object")

        context_required_fields = [
            "chat_id",
            "env",
            "org_id",
            "org_short_name",
            "source",
            "user_id",
        ]
        for field in context_required_fields:
            if field not in context:
                return abort(400, f"Missing required context field: {field}")

        # Validate user_event structure
        user_event = data["user_event"]
        if not isinstance(user_event, dict):
            return abort(400, "User event must be an object")

        user_event_required_fields = [
            "attributes",
            "category",
            "created_at",
            "event_id",
        ]
        for field in user_event_required_fields:
            if field not in user_event:
                return abort(400, f"Missing required user_event field: {field}")

        # Validate user_event.attributes structure
        attributes = user_event["attributes"]
        if not isinstance(attributes, dict):
            abort(400, "User event attributes must be an object")

        if "attributes" not in attributes or "category" not in attributes:
            return abort(
                400,
                "User event attributes must contain 'attributes' and 'category' fields",
            )

        # Validate ID format (should be UUID-like)
        try:
            uuid.UUID(data["id"])
        except ValueError:
            return abort(400, "ID must be a valid UUID format")

        # Generate mock response
        response = {
            "category": None,
            "collections": None,

        

            "created_at": datetime.now(timezone.utc).isoformat(),
            "id": data["id"],  # Use the same ID from request

            "num_of_reviews": None,
            "ready": True,
            "supported": True,
            "top_category": None,
        }

        return response

    except ValueError as e:
        return abort(400, f"Invalid JSON: {str(e)}")
    except HTTPError as e:
        return e
    except Exception as e:
        print("error", e.__class__.__name__)
        return abort(500, f"Internal server error: {str(e)}")
