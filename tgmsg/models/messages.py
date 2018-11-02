from .keyboards import Keyboard


class Message(object):
    def to_dict(self):
        return {}


class TextMessage(Message):
    def __init__(self, text: str, parse_mode: str = None, reply_markup: Keyboard = None,
                 disable_web_page_preview: bool = None, disable_notification: bool = None,
                 reply_to_message_id: int = None):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if parse_mode is not None:
            if not isinstance(parse_mode, str):
                raise TypeError('parse_mode must be an instance of str')
        if reply_markup is not None:
            if not isinstance(reply_markup, Keyboard):
                raise TypeError('reply_markup must be an instance of Keyboard')
        if disable_web_page_preview is not None:
            if not isinstance(disable_web_page_preview, bool):
                raise TypeError('disable_web_page_preview must be an instance of bool')
        if disable_notification is not None:
            if not isinstance(disable_notification, bool):
                raise TypeError('disable_notification must be an instance of bool')
        if reply_to_message_id is not None:
            if not isinstance(reply_to_message_id, int):
                raise TypeError('reply_to_message_id must be an instance of int')

        self.text = text
        self.parse_mode = parse_mode
        self.reply_markup = reply_markup
        self.disable_web_page_preview = disable_web_page_preview
        self.disable_notification = disable_notification
        self.reply_to_message_id = reply_to_message_id

    def to_dict(self):
        res = {'text': self.text}
        if self.parse_mode is not None:
            res['parse_mode'] = self.parse_mode
        if self.reply_markup is not None:
            res['reply_markup'] = self.reply_markup.to_dict()
        if self.disable_web_page_preview is not None:
            res['disable_web_page_preview'] = self.disable_web_page_preview
        if self.disable_notification is not None:
            res['disable_notification'] = self.disable_notification
        if self.reply_to_message_id is not None:
            res['reply_to_message_id'] = self.reply_to_message_id
        return res
