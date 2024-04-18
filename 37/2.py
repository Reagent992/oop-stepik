import sys
from typing import List


class MailItem:

    def __init__(self, mail_from: str, title: str, content: str) -> None:
        self.mail_from = mail_from
        self.title = title
        self.content = content
        self.is_read = False

    def set_read(self, fl_read: bool = True) -> None:
        if fl_read:
            self.is_read = True
        else:
            self.is_read = False

    def __bool__(self) -> bool:
        return self.is_read


class MailBox:
    def __init__(self) -> None:
        self.inbox_list: List[MailItem] = []

    def receive(self):
        """Получение почты."""
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        for string in lst_in:
            mail_from, title, content = string.split("; ")
            self.inbox_list.append(MailItem(mail_from, title, content))


if __name__ == "__main__":
    mail = MailBox()
    mail.receive()
    mail.inbox_list[0].set_read()
    mail.inbox_list[-1].set_read()

    inbox_list_filtered = list(filter(bool, mail.inbox_list))
