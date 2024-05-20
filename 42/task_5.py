from typing import Optional


class VideoItem:
    def __init__(self, title: str, descr: str, path: str) -> None:
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:
    def __init__(self, rating: int = 0) -> None:
        self.validate(rating)
        self.__rating = rating

    @property
    def rating(self) -> Optional[int]:
        return self.__rating

    @rating.setter
    def rating(self, value: int) -> None:
        self.validate(value)
        self.__rating = value

    @staticmethod
    def validate(value: int) -> bool:
        if not isinstance(value, int) or not 0 <= value <= 5:
            raise ValueError
        return True


if __name__ == "__main__":
    vr = VideoRating(3)
    try:
        VideoRating(10)
    except ValueError:
        assert True
    else:
        assert False

    assert vr.rating == 3
    vr.rating = 0
    assert vr.rating == 0
