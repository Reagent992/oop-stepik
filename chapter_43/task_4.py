from typing import Callable, Dict, Optional, Type


class Router:
    app: Dict[str, Callable] = {}

    @classmethod
    def get(cls, path: str) -> Optional[Callable]:
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path: str, func: Callable) -> None:
        cls.app[path] = func


class Callback:
    def __init__(self, path: str, router: Type[Router]) -> None:
        self.path = path
        self.router = router

    def __call__(self, func: Callable) -> None:
        self.router.add_callback(self.path, func)


if __name__ == "__main__":

    @Callback("/", Router)
    def index():
        return "<h1>Главная</h1>"

    route = Router.get("/")
    if route:
        ret = route()
        print(ret)
