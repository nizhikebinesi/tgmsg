import json

import requests

from .models.messages import Message


class TelegramClient(object):
    _tg_bot_api_url = 'https://api.telegram.org/bot'

    def __init__(self, token: str):
        if not isinstance(token, str):
            raise TypeError('token must be an instance of str')
        self.token = token
        self.first_name = self.get_me().get('first_name')
        self.text_message_processor = None

    def register_text_message_processor(self):
        def add(processor):
            self.text_message_processor = processor
            return processor

        return add

    def send_message(self, chat_id, message: Message):
        if not isinstance(chat_id, str) and not isinstance(chat_id, int):
            raise TypeError('url must be an instance of str or int')
        if not isinstance(message, Message):
            raise TypeError('message must be an instance of Message')
        msg = message.to_dict()
        msg['chat_id'] = chat_id
        self.post_request('sendMessage', json.dumps(msg))

    def set_webhook(self, url: str, max_connections: int, allowed_updates: list):
        if not isinstance(url, str):
            raise TypeError('url must be an instance of str')
        if not isinstance(max_connections, int):
            raise TypeError('max_connections must be an instance of int')
        if not isinstance(allowed_updates, list):
            raise TypeError('allowed_updates must be an instance of list')
        resp = self.post_request('setWebhook', json.dumps(
            {'url': url, 'max_connections': max_connections, 'allowed_updates': allowed_updates}))
        return resp

    def get_me(self):
        return self.post_request('getMe', '{}')

    def post_request(self, endpoint: str, data: str):
        if not isinstance(endpoint, str):
            raise TypeError('endpoint must be an instance of str')
        if not isinstance(data, str):
            raise TypeError('data must be an instance of str')
        headers = requests.utils.default_headers()
        response = requests.post(f'{self._tg_bot_api_url}{self.token}/{endpoint}', data=data, headers=headers)
        response.raise_for_status()
        return json.loads(response.text)
