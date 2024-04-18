from typing import Dict, Tuple


class Handler:
    def __init__(self, methods: Tuple[str, ...] = ("GET",)) -> None:
        self.__methods = methods

    def get(self, func, request: Dict[str, str]) -> str:
        return f"GET: {func(request)}"

    def post(self, func, request: Dict[str, str]) -> str:
        return f"POST: {func(request)}"

    def __call__(self, func):
        """Имитирует обычный декоратор-функцию."""

        def wrapper(request: Dict[str, str]):
            method = request.get("method", "GET")
            if method in self.__methods:
                if t := self.__getattribute__(method.lower()):
                    return t(func, request)

        return wrapper


if __name__ == "__main__":

    @Handler(methods=("GET", "POST"))
    def contact(request):
        return "Сергей Балакирев"

    request = {"method": "POST", "url": "contact.html"}
    print(contact(request))
