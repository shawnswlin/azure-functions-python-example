import os
import HttpHandler
from UserMgr import UserMgr

method = os.environ.get('REQ_METHOD')
usermgr = UserMgr()

if method == HttpHandler.GET:    
    status, msg = 200, usermgr.users

elif method == HttpHandler.POST:
    postreqdata = HttpHandler.get_postdata()
    res = usermgr.update_age(postreqdata.get("name"), postreqdata.get("age"))
    status, msg = 201, res
    
else:
    status, msg = 404, "This method is not support yet"

HttpHandler.make_response(status, msg)
