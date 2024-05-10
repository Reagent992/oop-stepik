class Singleton:
    __instance_base = None
    __instance = None

    def __new__(cls, *arg, **kwargs):
        if cls == Singleton:
            if cls.__instance_base is None:
                cls.__instance_base = super().__new__(cls)
            return cls.__instance_base
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Singleton.__instance = None


class Game(Singleton):
    def __init__(self, name: str) -> None:
        if "name" not in self.__dict__:
            self.name = name

if __name__ == "__main__":
    sing_obj = Singleton()
    second_obj = Singleton()
    assert sing_obj == second_obj
    del sing_obj
    del second_obj
    var = "PS2"
    game = Game(var)
    assert game.name == var
