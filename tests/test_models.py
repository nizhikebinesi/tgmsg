import pytest

from tgmsg.models.keyboards import InlineKeyboardButton, InlineKeyboard, KeyboardButton, ReplyKeyboard, Keyboard
from tgmsg.models.messages import Message, TextMessage
from tgmsg.models.requests import IncomingMessage, User, CallbackQuery, Update, Chat
from tgmsg.errors import TelegramError


class TestKeyboards:
    def test_Keyboard(self):
        k = Keyboard()
        assert k.to_dict() == {}

    def test_KeyboardButton(self):
        b = KeyboardButton('hello')
        assert b.to_dict() == {
            'text': 'hello',
            'request_contact': False,
            'request_location': False
        }
        with pytest.raises(TypeError):
            KeyboardButton(1, False, False)
        with pytest.raises(TypeError):
            KeyboardButton('test', 'test', False)
        with pytest.raises(TypeError):
            KeyboardButton('test', False, '')

    def test_ReplyKeyboard(self):
        b = KeyboardButton('hello')
        k = ReplyKeyboard([[b]])
        k.row([b])
        assert k.to_dict() == {
            'keyboard': [
                [{
                    'text': 'hello',
                    'request_contact': False,
                    'request_location': False
                }],
                [{
                    'text': 'hello',
                    'request_contact': False,
                    'request_location': False
                }]
            ],
            'resize_keyboard': True,
            'one_time_keyboard': False,
            'selective': False
        }
        with pytest.raises(TypeError):
            ReplyKeyboard([[b]], '', True, True)
        with pytest.raises(TypeError):
            ReplyKeyboard([[b]], True, '', True)
        with pytest.raises(TypeError):
            ReplyKeyboard([[b]], True, True, '')
        with pytest.raises(TypeError):
            ReplyKeyboard('hello', True, True, True)
        with pytest.raises(TypeError):
            ReplyKeyboard(['hello'], True, True, True)
        with pytest.raises(TypeError):
            ReplyKeyboard([['hello']], True, True, True)
        with pytest.raises(TypeError):
            k.row('hello')
        with pytest.raises(TypeError):
            k.row(['hello'])

    def test_InlineKeyboardButton(self):
        b = InlineKeyboardButton('hello', 'hello', 'hello')
        assert b.to_dict() == {
            'text': 'hello',
            'url': 'hello',
            'callback_data': 'hello'
        }
        with pytest.raises(TypeError):
            InlineKeyboardButton(1, 'hello', 'hello')
        with pytest.raises(TypeError):
            InlineKeyboardButton('hello', 1, 'hello')
        with pytest.raises(TypeError):
            InlineKeyboardButton('hello', 'hello', 1)

    def test_InlineKeyboard(self):
        b = InlineKeyboardButton('hello', 'hello', 'hello')
        k = InlineKeyboard([[b]])
        assert k.to_dict() == {'inline_keyboard': [[{
            'text': 'hello',
            'url': 'hello',
            'callback_data': 'hello'
        }
        ]]}
        k.row([b])
        with pytest.raises(TypeError):
            k.row('hello')
        with pytest.raises(TypeError):
            k.row(['hello'])
        with pytest.raises(TypeError):
            InlineKeyboard('hello')
        with pytest.raises(TypeError):
            InlineKeyboard(['hello'])
        with pytest.raises(TypeError):
            InlineKeyboard([['hello']])


class TestMessages:
    def test_Message(self):
        m = Message()
        assert m.to_dict() == {}

    def test_TextMessage(self):
        b = InlineKeyboardButton('hello', 'hello', 'hello')
        k = InlineKeyboard([[b]])
        m = TextMessage('test', 'test', k, True, True, 1)
        assert m.to_dict() == {
            'text': 'test',
            'parse_mode': 'test',
            'reply_markup': {'inline_keyboard': [[{
                'text': 'hello',
                'url': 'hello',
                'callback_data': 'hello'
            }
            ]]},
            'disable_web_page_preview': True,
            'disable_notification': True,
            'reply_to_message_id': 1
        }
        with pytest.raises(TypeError):
            TextMessage(1, 'test', k, True, True, 1)
        with pytest.raises(TypeError):
            TextMessage('test', 1, k, True, True, 1)
        with pytest.raises(TypeError):
            TextMessage('test', 'test', 1, True, True, 1)
        with pytest.raises(TypeError):
            TextMessage('test', 'test', k, '', True, 1)
        with pytest.raises(TypeError):
            TextMessage('test', 'test', k, True, '', 1)
        with pytest.raises(TypeError):
            TextMessage('test', 'test', k, True, True, '')


class TestRequests:
    def test_User(self):
        u = User(1)

    def test_Chat(self):
        c = Chat(1, 'sdf')

    def test_IncomingMessage(self):
        m = IncomingMessage(**{'message_id': 1, 'chat': {'id': 1, 'type': 'sdf'}, 'from': {'id': 1}})

    def test_CallbackQuery(self):
        CallbackQuery(**{'id': 1, 'message': {'message_id': 1, 'chat': {'id': 1, 'type': 'sdf'}, 'from': {'id': 1}},
                         'from': {'id': 1}})

    def test_Update(self):
        Update(**{'update_id': 1, 'callback_query': {'id': 1,
                                                     'message': {'message_id': 1, 'chat': {'id': 1, 'type': 'sdf'},
                                                                 'from': {'id': 1}},
                                                     'from': {'id': 1}}})
        Update(**{'update_id': 1, 'message': {'message_id': 1, 'chat': {'id': 1, 'type': 'sdf'}, 'from': {'id': 1}}})

class TestError:
    def test_Error(self):
        TelegramError(100, 'asd')