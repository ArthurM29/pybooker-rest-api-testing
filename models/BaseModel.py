import json


class BaseModel(object):
    def __init__(self):
        pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def __str__(self):
        return self.to_json()
    # TODO do I need this ?


    # TODO 2 - have customize get_json() to accept 'skip' keyword argument to skip list of elements
