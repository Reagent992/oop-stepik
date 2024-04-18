class RenderList:
    def __init__(self, type_list: str) -> None:
        if type_list in ("ul", "ol"):
            self.type_list = type_list
        else:
            self.type_list = "ul"

    def __call__(self, list_=None) -> str:
        start = f"<{self.type_list}>"
        end = f"</{self.type_list}>"
        if list_:
            mid = "\n".join([f"<li>{i}</li>" for i in list_])
            return start + "\n" + mid + "\n" + end
        else:
            return start + "\n" + end


if __name__ == "__main__":
    lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
    type_list = "ul"
    render = RenderList(type_list)
    print(render(lst))
    print("####################################")
    print(render())
