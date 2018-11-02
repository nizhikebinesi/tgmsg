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

        @c.register_message_processor()
        def fo():
            return

        @c.register_callback_query_processor()
        def f():
            return

        with pytest.raises(Exception):
            c.process_json({})

        c.process_json()
        c.process_json()