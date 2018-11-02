import json

import requests

from .models.messages import Message
from .models.requests import Update
from .errors import TelegramError


class TelegramClient(object):
    _tg_bot_api_url = 'https://api.telegram.org/bot'

    def __init__(self, token: str):
        if not isinstance(token, str):
            raise TypeError('token must be an instance of str')
        self.token = token
        self.first_name = self.get_me().get('first_name')
        self._message_processor = None
        self._callback_query_processor = None

    def register_message_processor(self):
        def add(processor):
            self._text_message_processor = processor
            return processor

        return add

    def register_callback_query_processor(self):
        def add(processor):
            self._callback_query_processor = processor
            return processor

        return add

    def process_json(self, msg: dict):
        if not isinstance(msg, dict):
            raise TypeError('msg must be an instance of dict')
        update = Update(**msg)
        if hasattr(update, 'callback_query'):
            if not self._callback_query_processor:
                raise AttributeError('_callback_query_processor not declared')
            self._callback_query_processor(update)
            return None
        elif hasattr(update, 'message'):
            if not self._message_processor:
                raise AttributeError('_message_processor not declared')
            self._message_processor(update)
            return None
        else:
            raise Exception('Now available just message and callback_query')

    def send_message(self, chat_id, message: Message):
        if not isinstance(chat_id, str) and not isinstance(chat_id, int):
            raise TypeError('url must be an instance of str or int')
        if not isinstance(message, Message):
            raise TypeError('message must be an instance of Message')
        msg = message.to_dict()
        msg['chat_id'] = chat_id
        self.post_request('sendMessage', json.dumps(msg))

    def set_webhook(self, url: str, max_connections: int = None, allowed_updates: list = None):
        if not isinstance(url, str):
            raise TypeError('url must be an instance of str')
        if max_connections is not None:
            if not isinstance(max_connections, int):
                raise TypeError('max_connections must be an instance of int')
        if allowed_updates is not None:
            if not isinstance(allowed_updates, list):
                raise TypeError('allowed_updates must be an instance of list')
        res = {'url': url}
        if max_connections is not None:
            res['max_connections'] = max_connections
        if allowed_updates is not None:
            res['allowed_updates'] = allowed_updates
        resp = self.post_request('setWebhook', json.dumps(res))
        return resp

    def get_me(self):
        return self.post_request('getMe', '{}')

    def post_request(self, endpoint: str, data: str):
        if not isinstance(endpoint, str):
            raise TypeError('endpoint must be an instance of str')
        if not isinstance(data, str):
            raise TypeError('data must be an instance of str')
        headers = requests.utils.default_headers()
        headers['Content-Type'] = 'application/json'
        response = requests.post(f'{self._tg_bot_api_url}{self.token}/{endpoint}', data=data, headers=headers)
        if response.status_code == 400:
            msg = response.json()
            raise TelegramError(msg['error_code'], msg['description'])
        response.raise_for_status()
        return json.loads(response.text)

