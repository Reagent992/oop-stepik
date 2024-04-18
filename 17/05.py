from typing import Dict, Union


class Application:
    def __init__(self, name: str, blocked: bool = False) -> None:
        self.name = name
        self.blocked = blocked


class AppStore:
    APPS: Dict[str, Application] = dict()

    def add_application(self, app: Application) -> None:
        """Добавление нового приложения app в магазин."""
        self.APPS[app.name] = app

    def remove_application(self, app: Application) -> Union[Application, str]:
        """Удаление приложения app из магазина."""
        return self.APPS.pop(app.name, "Такого приложения нету в списке.")

    def block_application(self, app: Application):
        """Блокировка приложения."""
        item = self.APPS.get(app.name)
        if item:
            item.blocked = True

    def total_apps(self):
        """Общее число приложений в магазине."""
        return len(self.APPS)


store = AppStore()
app_youtube = Application("Youtube")
store.add_application(app_youtube)
store.remove_application(app_youtube)
