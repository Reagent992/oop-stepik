from typing import Dict


class GeneralView:
    allowed_methods = ("GET", "POST", "PUT", "DELETE")

    def verify_method(self, request: Dict[str, str]) -> bool:
        if (
            request.get("method")
            and request["method"].upper() not in self.allowed_methods
        ):
            raise TypeError
        return True

    def render_request(self, request: Dict[str, str]) -> None:
        self.verify_method(request)
        return getattr(self, request["method"].lower())(request)


if __name__ == "__main__":
    assert issubclass(GeneralView, object)
    assert hasattr(GeneralView, "allowed_methods")
    assert GeneralView.allowed_methods == ("GET", "POST", "PUT", "DELETE")
    assert hasattr(GeneralView, "render_request")
    request = {"url": "/", "method": "GET"}
    g = GeneralView()
    g.render_request(request)
    try:
        request = {"url": "/", "method": "TRACE"}
        GeneralView().render_request(request=request)
    except TypeError:
        assert True
    else:
        assert False
