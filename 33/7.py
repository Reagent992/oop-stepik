class Clock:
    """Хранение текущего времени."""

    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self) -> int:
        """Вывод текущего времени в секундах."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds


class DeltaClock:
    """Вычисление разницы времен."""

    def __init__(self, clock1: Clock, clock2: Clock) -> None:
        self.clock1 = clock1
        self.clock2 = clock2

    def __str__(self) -> str:
        """Возвращает строку разницы времен clock1 - clock2."""
        difference = self.__len__()
        hours = difference // 3600
        minutes = difference % 3600 // 60
        seconds = difference % 3600 % 60
        return f"{hours:02}: {minutes:02}: {seconds:02}"

    def __len__(self) -> int:
        """Возвращает разницу в секундах."""
        first_time = self.clock1.get_time()
        second_time = self.clock2.get_time()
        difference = first_time - second_time
        return difference if difference > 0 else 0


if __name__ == "__main__":
    dt = DeltaClock(Clock(2, 45, 0), Clock(1, 15, 0))
    print(dt)
    len_dt = len(dt)  # 5400
    print(len_dt)
