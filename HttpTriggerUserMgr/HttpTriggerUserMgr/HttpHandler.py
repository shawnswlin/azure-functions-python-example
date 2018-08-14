import os
import json

GET = "GET"
POST = "POST"
PUT = "PUT"
PATCH = "PATCH"
DELETE = "DELETE"

def make_response(status, content):
    response = open(os.environ['res'], 'w')
    json_data = {
        "status": status,
        "body": content,
        "headers": {
            "Content-Type": "application/json"
        }
    }
    response.write(json.dumps(json_data))
    response.close()
    
def get_postdata():
    return json.loads(open(os.environ['req']).read())