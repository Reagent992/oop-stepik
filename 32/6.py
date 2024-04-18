class HandlerGET:
    """Обработка GET-запросов, на стороне сервера."""

    def __init__(self, func) -> None:
        self.func = func

    def get(self, func, request: dict, *args, **kwargs):
        method = request.get("method", "GET")
        if method == "GET":
            result = func(request, *args, **kwargs)
            return f"{method}: {result}"

    def __call__(self, request: dict, *args, **kwargs):
        return self.get(self.func, request, *args, **kwargs)


if __name__ == "__main__":
    request = {"method": "GET", "url": "contact.html"}

    @HandlerGET
    def contact(request):
        return "Сергей Балакирев"

    print(contact(request))


@HandlerGET
def index(request):
    return "главная страница сайта"


res = index({"method": "GET"})
assert (
    res == "GET: главная страница сайта"
), "декорированная функция вернула неверные данные"
res = index({"method": "POST"})
assert res is None, "декорированная функция вернула неверные данные"
res = index({"method": "POST2"})
assert res is None, "декорированная функция вернула неверные данные"

res = index({})
assert (
    res == "GET: главная страница сайта"
), "декорированная функция вернула неверные данные"
