import os
import json
from Exceptions import *

class UserMgr:

    def __init__(self, path="users.json"):
        self.__path = path
        with open(path) as fp:
            content = fp.read()
            print(content)
        self.users = json.loads(content)
    
    def update_age(self, name, age):
        if name not in self.users:
            raise UserNotFound(name)
        self.users[name] = age
        self.__save()
        return {name: self.users[name]}

    def __save(self):
        with open(self.__path, "wb") as fp:
            fp.write(json.dumps(self.users))
            