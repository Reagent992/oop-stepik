from typing import Dict, Tuple


class GenericView:
    def __init__(self, methods: Tuple[str, ...] = ("GET",)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetailView(GenericView):
    def render_request(self, request: Dict[str, str], method: str) -> str:
        self.validate_methods(method)
        self.validate_request(request)
        return getattr(self, method.lower())(request)

    def get(self, request) -> str:
        return f"url: {request['url']}"

    def validate_request(self, request: Dict[str, str]) -> bool:
        if not isinstance(request, dict):
            raise TypeError("request не является словарем")
        if not request.get("url"):
            raise TypeError("request не содержит обязательного ключа url")
        return True

    def validate_methods(self, method: str) -> bool:
        if method not in self.methods:
            raise TypeError("данный запрос не может быть выполнен")
        return True


if __name__ == "__main__":
    dr = DetailView()
    html = dr.render_request({"url": "ya.ru"}, "GET")
    print(html)
