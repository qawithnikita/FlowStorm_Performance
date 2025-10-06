from bottle import response
import json
from org import OrgGenerator

def org_configs():

    response.content_type = "application/json"
    return json.dumps({"configs": OrgGenerator.organization_list})