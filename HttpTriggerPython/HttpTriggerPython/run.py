import os
import json

"""
output
    {
        "data": "",
        "method": "GET"
    }
or
    {
        "data": "{\"name\": \"userA\"}",
        "method": "POST"
    }

"""
def make_response(content):
    response = open(os.environ['res'], 'w')
    json_data = {
        "body": content,
        "headers": {
            "Content-Type": "application/json"
        }
    }
    response.write(json.dumps(content))
    response.close()
    
method = os.environ.get('REQ_METHOD')
data = open(os.environ['req']).read()
content = {
    "method": method,
    "data": data
}
make_response(content)

