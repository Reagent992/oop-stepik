from typing import List


class Message:
    def __init__(self, text: str, fl_like: bool = False) -> None:
        self.text = text
        self.fl_like = fl_like


class Viber:
    __messages__: List[Message] = list()

    @classmethod
    def add_message(cls, msg: Message) -> None:
        """Добавление нового сообщения в список сообщений."""
        cls.__messages__.append(msg)

    @classmethod
    def remove_message(cls, msg: Message):
        """Удаление сообщения из списка."""
        cls.__messages__.remove(msg)

    @classmethod
    def set_like(cls, msg: Message):
        """Поставить/убрать лайк для сообщения msg."""
        if msg.fl_like:
            msg.fl_like = False
        else:
            msg.fl_like = True

    @classmethod
    def show_last_message(cls, amount: int):
        """Отображение последних сообщений."""
        print(*cls.__messages__)

    @classmethod
    def total_messages(cls):
        """Возвращает общее число сообщений."""
        return len(cls.__messages__)


msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))
Viber.set_like(msg)
Viber.remove_message(msg)