import pytest

from tgmsg.models.keyboards import InlineKeyboardButton, InlineKeyboard, KeyboardButton, ReplyKeyboard, Keyboard
from tgmsg.models.messages import Message, TextMessage


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
