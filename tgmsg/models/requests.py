class Chat(object):
    def __init__(self, id: int, type: str, **kwargs):
        self.id = id
        self.type = type
        for key in kwargs:
            setattr(self, key, kwargs[key])


class Message(object):
    def __init__(self, message_id: int, chat, **kwargs):
        self.message_id = message_id
        self.chat = Chat(**chat)
        for key in kwargs:
            setattr(self, key, kwargs[key])


class Update(object):
    def __init__(self, update_id: int, **kwargs):
        self.update_id = update_id
        for key in kwargs:
            setattr(self, key, kwargs[key])
