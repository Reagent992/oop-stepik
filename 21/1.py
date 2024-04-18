class Clock:
    def __init__(self, time: int = 0) -> None:
        self.__time = time

    def set_time(self, tm):
        """для установки текущего времени"""
        if self.check_time(tm):
            self.__time = tm

    def get_time(self):
        return self.__time

    @classmethod
    def check_time(cls, tm):
        return isinstance(tm, int) and 0 <= tm <= 1000000


clock = Clock(4530)
