import os
import json

http_in_key = "req"  # Request parameter name  
http_out_key = "res"  # Response parameter name  
output_key = "name"  # Message parameter name

name = json.loads(open(os.environ[http_in_key]).read())["name"]
with open(os.environ[http_out_key], 'w') as fp:
    fp.write("Hello {}".format(name))

with open(os.environ[output_key], 'w') as fp:
    fp.write(name)
