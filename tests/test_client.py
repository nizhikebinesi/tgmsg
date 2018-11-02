import pytest
import requests_mock

from tgmsg.tg_client import TelegramClient


@requests_mock.Mocker(kw='mock')
class TestClient:
    _tg_bot_api_url = 'https://api.telegram.org/bot'

    def test_client(self, **kw):
        mock = kw['mock']
        mock.register_uri('POST', self._tg_bot_api_url + 'test/getMe',
                          json={'first_name': 'qqq'})

        with pytest.raises(TypeError):
            TelegramClient(1)
        c = TelegramClient('test')
        assert c.first_name == 'qqq'
        with pytest.raises(AttributeError):
            c.process_json({'update_id': 228068639, 'message': {'message_id': 1072, 'from': {'id': 386257722, 'is_bot': False, 'first_name': 'Денис', 'username': 'runotwo', 'language_code': 'ru-ru'}, 'chat': {'id': 386257722, 'first_name': 'Денис', 'username': 'runotwo', 'type': 'private'}, 'date': 1541164811, 'text': 'Вов'}})
        with pytest.raises(AttributeError):
            c.process_json({'update_id': 228068641, 'callback_query': {'id': '1658964284142171204', 'from': {'id': 386257722, 'is_bot': False, 'first_name': 'Денис', 'username': 'runotwo', 'language_code': 'en-US'}, 'message': {'message_id': 1071, 'from': {'id': 436104927, 'is_bot': True, 'first_name': 'TestAppveloxAir', 'username': 'TestAppveloxAirBot'}, 'chat': {'id': 386257722, 'first_name': 'Денис', 'username': 'runotwo', 'type': 'private'}, 'date': 1540942253, 'text': 'hello'}, 'chat_instance': '3854070547539966290', 'data': 'callback'}})

        @c.register_message_processor()
        def fo(request):
            return

        @c.register_callback_query_processor()
        def f(request):
            return

        c.process_json({'update_id': 228068639, 'message': {'message_id': 1072, 'from': {'id': 386257722, 'is_bot': False, 'first_name': 'Денис', 'username': 'runotwo', 'language_code': 'ru-ru'}, 'chat': {'id': 386257722, 'first_name': 'Денис', 'username': 'runotwo', 'type': 'private'}, 'date': 1541164811, 'text': 'Вов'}})
        c.process_json({'update_id': 228068641, 'callback_query': {'id': '1658964284142171204', 'from': {'id': 386257722, 'is_bot': False, 'first_name': 'Денис', 'username': 'runotwo', 'language_code': 'en-US'}, 'message': {'message_id': 1071, 'from': {'id': 436104927, 'is_bot': True, 'first_name': 'TestAppveloxAir', 'username': 'TestAppveloxAirBot'}, 'chat': {'id': 386257722, 'first_name': 'Денис', 'username': 'runotwo', 'type': 'private'}, 'date': 1540942253, 'text': 'hello'}, 'chat_instance': '3854070547539966290', 'data': 'callback'}})

        with pytest.raises(Exception):
            c.process_json({})
