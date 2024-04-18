class LoginForm:
    def __init__(self, name, validators=None):
        self.name = name  # это заголовок формы
        self.validators = validators  # список из валидаторов
        self.login = ""
        self.password = ""

    def post(self, request):
        """
        request это словарь с ключами 'login' и 'password'
        и значениями (строками) для логина и пароля соответственно.
        """
        self.login = request.get("login", "")
        self.password = request.get("password", "")

    def is_validate(self):
        if not self.validators:
            return True

        for v in self.validators:
            if not v(self.login) or not v(self.password):
                return False

        return True


class LengthValidator:
    def __init__(self, min_length, max_length):
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, value):
        return self.min_length <= len(value) <= self.max_length


class CharsValidator:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, value):
        return set(value) <= set(self.chars)
