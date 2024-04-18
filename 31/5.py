class SmartPhone:
    def __init__(self, model: str) -> None:
        self.model = model
        self.apps = list()

    def add_app(self, app) -> None:
        if app.name not in [x.name for x in self.apps]:
            self.apps.append(app)

    def remove_app(self, app) -> None:
        self.apps.remove(app)


class AppVK:
    def __init__(self, name: str = "ВКонтакте") -> None:
        self.name = name


class AppYouTube:
    def __init__(self, memory_max: int = 1024) -> None:
        self.name = "YouTube"
        self.memory_max = memory_max


class AppPhone:
    def __init__(self, phone_list: dict, name: str = "Phone") -> None:
        self.phone_list = phone_list
        self.name = name
