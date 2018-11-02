class Keyboard(object):
    def to_dict(self):
        return {}


class InlineKeyboardButton(Keyboard):
    def __init__(self, text: str, url: str = None, callback_data: str = None, *args, **kwargs):
        if not isinstance(text, str):
            raise TypeError('text must be an instance of str')
        self.text = text
        if url is not None:
            if not isinstance(url, str):
                raise TypeError('url must be an instance of str')
        self.url = url
        if callback_data is not None:
            if not isinstance(callback_data, str):
                raise TypeError('callback_data must be an instance of str')
        self.callback_data = callback_data

    def to_dict(self):
        res = {'text': self.text}
        if self.url is not None:
            res['url'] = self.url
        if self.callback_data is not None:
            res['callback_data'] = self.callback_data
        return res


class InlineKeyboard(Keyboard):
    def __init__(self, button_rows: list = None):
        self.button_rows = []
        if button_rows is not None:
            if not isinstance(button_rows, list):
                raise TypeError('button_rows must be an instance of list')
            for row in button_rows:
                if not isinstance(row, list):
                    raise TypeError('row must be an instance of list')
                for button in row:
                    if not isinstance(button, InlineKeyboardButton):
                        raise TypeError('button must be an instance of InlineKeyboardButton')
            self.button_rows = button_rows

    def row(self, button_row: list):
        if not isinstance(button_row, list):
            raise TypeError('button_row must be an instance of list')
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
            raise TypeError('request_contact must be an instance of bool')
        if not isinstance(request_location, bool):
            raise TypeError('request_location must be an instance of bool')
        self.text = text
        self.request_contact = request_contact
        self.request_location = request_location

    def to_dict(self):
        return {
            'text': self.text,
            'request_contact': self.request_contact,
            'request_location': self.request_location
        }


class ReplyKeyboard(Keyboard):
    def __init__(self, button_rows: list = None, resize_keyboard: bool = True, one_time_keyboard: bool = False,
                 selective: bool = False):
        self.button_rows = []
        if not isinstance(resize_keyboard, bool):
            raise TypeError('resize_keyboard must be an instance of bool')
        if not isinstance(one_time_keyboard, bool):
            raise TypeError('one_time_keyboard must be an instance of bool')
        if not isinstance(selective, bool):
            raise TypeError('selective must be an instance of bool')
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard
        self.selective = selective

        if button_rows is not None:
            if not isinstance(button_rows, list):
                raise TypeError('button_rows must be an instance of list')
            for row in button_rows:
                if not isinstance(row, list):
                    raise TypeError('row must be an instance of list')
                for button in row:
                    if not isinstance(button, KeyboardButton):
                        raise TypeError('button must be an instance of KeyboardButton')
            self.button_rows = button_rows

    def row(self, button_row: list):
        if not isinstance(button_row, list):
            raise TypeError('button_row must be an instance of list')
        for button in button_row:
            if not isinstance(button, KeyboardButton):
                raise TypeError('button must be an instance of KeyboardButton')
        self.button_rows.append(button_row)

    def to_dict(self):
        return {
            'keyboard': [[button.to_dict() for button in row] for row in self.button_rows],
            'resize_keyboard': self.resize_keyboard,
            'one_time_keyboard': self.one_time_keyboard,
            'selective': self.selective
        }
