import HttpHandler
import sys

class UserNotFound(Exception):

    def __init__(self, name):
        HttpHandler.make_response(404, "Could not find user {}".format(name))
        sys.exit(0)