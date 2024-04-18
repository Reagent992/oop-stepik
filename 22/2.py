class WindowDlg:
    def __init__(self, title: str, width: int, height: int) -> None:
        self.__title = title
        self.__width = width
        self.__height = height

    def show(self):
        print(f"{self.title}: {self.width}, {self.height}")

    @staticmethod
    def check_size(value: int):
        return isinstance(value, int) and 0 <= value <= 10000

    @property
    def title(self):
        """Заголовок окна."""
        return self.__title

    @property
    def width(self):
        """Ширина окна."""
        return self.__width

    @width.setter
    def width(self, value):
        if self.check_size(value=value):
            self.__width = value
            self.show()

    @property
    def height(self):
        """Высота окна."""
        return self.__height

    @height.setter
    def height(self, value):
        if self.check_size(value=value):
            self.__height = value
            self.show()


title = "Заголовок"
width = 450
height = 300
wnd = WindowDlg(title, width, height)
assert wnd.title is title
assert wnd.width is width
assert wnd.height is height
wnd.show()
new_width = 500
new_height = 501
wnd.width = new_width
wnd.height = new_height
assert wnd.width == new_width
assert wnd.height == new_height
wrong_width = -1
wnd.width = wrong_width
assert wnd.width != wrong_width
