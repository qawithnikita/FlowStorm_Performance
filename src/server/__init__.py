from bottle import Bottle, request, response
from uuid import uuid4
import json
import random
import time
from org_config import ORG_CONFIG
from supported_event import supported_event
from session_messages import session_messages
from next_responses import next_responses
from next_suggestions import next_suggestions
from analytic_track_event import track_event
from org import OrgGenerator
from org_configs import org_configs

app = Bottle()


def get_uuid():
    return str(uuid4())

OrgGenerator.init()


# /org/config?namespace=spiffy-react-components&source=app&user_id=spiffy-user-id-cef946e2-56c1-4fbb-a870-f1326c18431e&include_experiments=default&include_feature_gates=is_client_session_enabled&include_feature_gates=is_new_feature_enabled&include_feature_gates=is_fine_tuned_model_8b&include_feature_gates=is_integrated_cx_enabled&include_feature_gates=is_non_shapewear_enabled&include_feature_gates=is_force_injection_enabled&include_feature_gates=is_image_banner_enabled&include_feature_gates=is_search_hash_enabled


# /session/messages
# ?org_id=ee9855bc-d2c2-46f3-ac94-9b79a8c89d32
# &chat_id=f208801d-4330-43c2-87c0-c0e06178ac62
# &user_id=spiffy-user-id-cef946e2-56c1-4fbb-a870-f1326c18431e

@app.route("/org/config")
def org_config():
    response.content_type = "application/json"
    uid = get_uuid()
    response.set_cookie("uid", uid)
    return json.dumps(ORG_CONFIG)


app.get("/org/configs")(org_configs)
app.post("/supported_event")(supported_event)
app.post("/session/messages")(session_messages)
app.post("/next_responses")(next_responses)
app.post("/next_suggestions")(next_suggestions)
app.post("/analytics/track_event")(track_event)


a = {
    "event": "[Amplitude] Page Viewed",
    "user_id": "spiffy-user-id-cef946e2-56c1-4fbb-a870-f1326c18431e",
    "event_properties": {"event_source": "shopify-web-pixel"},
    "user_properties": {},
}


@app.route("/world")
def world():
    response.content_type = "application/json"
    return json.dumps({"message": "hello world"})


@app.route("/check-uid")
def check_uid():
    response.content_type = "application/json"
    uid = request.get_cookie("uid")
    if uid:
        return json.dumps({"uid": uid})
    else:
        response.status = 400
        return json.dumps({"error": "No uid cookie found"})


@app.route("/sometimes-sleeps")
def sometimes_sleeps():
    response.content_type = "application/json"
    if random.random() > 0.99:
        time.sleep(random.randint(0, 10) / 10)
    return json.dumps({"message": "sometimes sleeps"})


if __name__ == "__main__":
    app.run(debug=True, port=8000, reloader=True)
