class FileAcceptor:
    def __init__(self, *ext: str) -> None:
        self._ok_ext = ext

    def __call__(self, ext) -> bool:
        for ok_ext in self._ok_ext:
            if ext[-len(ok_ext) :] == ok_ext:
                return True
        return False

    def __add__(self, obj: "FileAcceptor") -> "FileAcceptor":
        return FileAcceptor(*self._ok_ext + obj._ok_ext)


if __name__ == "__main__":
    fa1 = FileAcceptor("jpg", "jpeg")
    assert fa1("test.jpg") is True
    assert fa1("test.png") is False
    fa2 = FileAcceptor("txt", "doc")
    fa3 = fa1 + fa2
    assert fa3._ok_ext == ("jpg", "jpeg", "txt", "doc")

    # filter
    filenames = [
        "boat.jpg",
        "ans.web.png",
        "text.txt",
        "www.python.doc",
        "my.ava.jpg",
        "forest.jpeg",
        "eq_1.png",
        "eq_2.xls",
    ]
    assert list(filter(fa3, filenames)) == [
        "boat.jpg",
        "text.txt",
        "www.python.doc",
        "my.ava.jpg",
        "forest.jpeg",
    ]
