class SoftList(list):
    def __getitem__(self, index: int):
        if -len(self) <= index <= len(self) - 1:
            return super().__getitem__(index)
        return False


if __name__ == "__main__":
    sl = SoftList("python")
    assert sl[0] == "p"
    assert sl[-1] == "n"
    assert sl[6] is False
    assert sl[-7] is False
