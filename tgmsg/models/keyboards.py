class InlineKeyboardButton(object):
    def __init__(self, text: str, url: str, callback_data: str, *args, **kwargs):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if not isinstance(url, str):
            raise TypeError('url must be an instance of str')
        if not isinstance(callback_data, str):
            raise TypeError('callback_data must be an instance of str')
        self.text = text
        self.url = url
        self.callback_data = callback_data

    def to_dict(self):
        return {'text': self.text, 'url': self.url, 'callback_data': self.callback_data}


class InlineKeyboard(object):
    def __init__(self, button_rows: list = None):
        self.button_rows = []
        if button_rows is not None:
            if not isinstance(button_rows, list):
                raise TypeError('button_rows must be an instance of str')
            for row in button_rows:
                if not isinstance(row, list):
                    raise TypeError('row must be an instance of str')
                for button in row:
                    if not isinstance(button, InlineKeyboardButton):
                        raise TypeError('button must be an instance of InlineKeyboardButton')
            self.button_rows = button_rows

    def row(self, button_row: list):
        if not isinstance(button_row, list):
            raise TypeError('button_row must be an instance of str')
        for button in button_row:
            if not isinstance(button, InlineKeyboardButton):
                raise TypeError('button must be an instance of InlineKeyboardButton')
        self.button_rows.append(button_row)

    def to_dict(self):
        return {'inline_keyboard': [[button.to_dict() for button in row] for row in self.button_rows]}


class KeyboardButton(object):
    def __init__(self, text: str, request_contact: bool = False, request_location: bool = False):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        if not isinstance(request_contact, bool):
            raise TypeError('request_contact must be an instance of str')
        if not isinstance(request_location, bool):
            raise TypeError('request_location must be an instance of str')
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

    def to_dict(self):
        return {
            'text': self.text,
            'request_contact': self.request_contact,
            'request_location': self.request_location
        }


class ReplyKeyboard(object):
    def __init__(self, button_rows: list = None, resize_keyboard: bool = False, one_time_keyboard: bool = False,
                 selective: bool = False):
        self.button_rows = []
        if button_rows is not None:
            if not isinstance(resize_keyboard, bool):
                raise TypeError('resize_keyboard must be an instance of str')
            if not isinstance(one_time_keyboard, bool):
                raise TypeError('one_time_keyboard must be an instance of str')
            if not isinstance(selective, bool):
                raise TypeError('selective must be an instance of str')
            if not isinstance(button_rows, list):
                raise TypeError('button_rows must be an instance of str')
            for row in button_rows:
                if not isinstance(row, list):
                    raise TypeError('row must be an instance of str')
                for button in row:
                    if not isinstance(button, KeyboardButton):
                        raise TypeError('button must be an instance of KeyboardButton')
            self.button_rows = button_rows

    def row(self, button_row: list):
        if not isinstance(button_row, list):
            raise TypeError('button_row must be an instance of str')
        for button in button_row:
            if not isinstance(button, KeyboardButton):
                raise TypeError('button must be an instance of KeyboardButton')
        self.button_rows.append(button_row)

    def to_dict(self):
        return {'inline_keyboard': [[button.to_dict() for button in row] for row in self.button_rows]}
