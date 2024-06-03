class ShopItem:
    ID_SHOP_ITEM = 0

    def __init__(self) -> None:
        super().__init__()
        ShopItem.ID_SHOP_ITEM += 1
        self._id = ShopItem.ID_SHOP_ITEM

    def get_pk(self) -> int:
        return self._id


# здесь объявляйте классы ShopGenericView и ShopUserView
class ShopGenericView:
    def __str__(self) -> str:
        return "\n".join(
            [
                f"{k}: {v}"
                for k, v in self.__dict__.items()
                if self.__dict__.items()
            ]
        )

    def __repr__(self) -> str:
        return self.__str__()


class ShopUserView:
    def __str__(self) -> str:
        return "\n".join(
            [
                f"{k}: {v}"
                for k, v in self.__dict__.items()
                if self.__dict__.items() and k != "_id"
            ]
        )

    def __repr__(self) -> str:
        return self.__str__()


class Book(ShopItem):
    def __init__(self, title, author, year) -> None:
        super().__init__()
        self._title = title
        self._author = author
        self._year = year


if __name__ == "__main__":
    assert issubclass(ShopGenericView, object)
    sgv = ShopGenericView()
    assert issubclass(ShopUserView, object)

    class T(ShopItem, ShopGenericView):
        def __init__(self, title, author, year) -> None:
            super().__init__()
            self._title = title
            self._author = author
            self._year = year

    class T2(ShopItem, ShopUserView):
        def __init__(self, title, author, year) -> None:
            super().__init__()
            self._title = title
            self._author = author
            self._year = year

    t = T("Python ООП", "Балакирев", 2022)
    assert (
        str(t) == "_id: 1\n_title: Python ООП\n_author: Балакирев\n_year: 2022"
    )
    t2 = T2("Python ООП", "Балакирев", 2022)
    assert (
        str(t2) == "_title: Python ООП\n_author: Балакирев\n_year: 2022"
    )