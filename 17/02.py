from string import ascii_lowercase, digits


# здесь объявляйте классы TextInput и PasswordInput


class TextInput:
    field = "login"

    def __init__(self, name: str, size=10) -> None:
        if self.check_name(name):
            self.name = name
        else:
            raise ValueError
        self.size = size

    def get_html(self) -> str:
        return (
            f"<p class='{self.field}'>{self.name}: "
            f"<input type='text' size={self.size} />"
        )

    @classmethod
    def check_name(cls, name: str) -> bool:
        """Для проверки корректности переданного имя поля."""
        CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
        CHARS_CORRECT = CHARS + CHARS.upper() + digits
        return 3 <= len(name) <= 50 and all(
            [i.lower() in CHARS_CORRECT for i in name]
        )


class PasswordInput(TextInput):
    field = "password"


class FormLogin:
    """работы с формами ввода логин/пароль"""

    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(
            [
                '<form action="#">',
                self.login.get_html(),
                self.password.get_html(),
                "</form>",
            ]
        )


# эти строчки не менять
login = FormLogin(TextInput("Логин"), PasswordInput("Пароль"))
html = login.render_template()
#print(html)

assert isinstance(login, FormLogin)

class TextInput2:
    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type='text' size={self.size} />"


class PasswordInput2:
    def __init__(self, name, size=10):
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='password'>{self.name}: <input type='text' size={self.size} />"

f1_1 = TextInput("Login123")
f1_2 = PasswordInput("Psw")

f2_1 = TextInput2("Login123")
f2_2 = PasswordInput2("Psw")

f11 = f1_1.get_html().replace(' ', '').replace('\'', '"')
f12 = f1_2.get_html().replace(' ', '').replace('\'', '"')
f21 = f2_1.get_html().replace(' ', '').replace('\'', '"')
f22 = f2_2.get_html().replace(' ', '').replace('\'', '"')
assert f11 == f21 and f12 == f22, f"неверное возвращаемое значение методом get_html\n{f11}\n{f21}\n\n{f12}\n{f22}\n"


try:
    a = TextInput('aa')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

    
try:
    a = PasswordInput('aa')
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"