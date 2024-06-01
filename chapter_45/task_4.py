from abc import ABC, abstractmethod
from uuid import uuid4


class Model(ABC):
    @abstractmethod
    def get_pk(self):
        pass

    def get_info(self) -> str:
        return "Базовый класс Model"


class ModelForm(Model):
    def __init__(self, login: str, password: str) -> None:
        self._id = uuid4().int
        self._login = login
        self._password = password

    def get_pk(self) -> int:
        return self._id


if __name__ == "__main__":
    assert issubclass(Model, ABC)
    assert hasattr(Model, "get_pk")
    assert hasattr(Model, "get_info")

    assert issubclass(ModelForm, Model)
    i = ModelForm("login", "password")
    assert i._login == "login"
    assert i._password == "password"
    assert isinstance(i._id, int)
    assert hasattr(i, "get_pk")
    assert i.get_pk() == i._id
