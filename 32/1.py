from typing import Any
import random


class RandomPassword:
    def __init__(
        self, psw_chars: str, min_length: int, max_length: int
    ) -> None:
        self.psw_chars = psw_chars
        self.min_length = min_length
        self.max_length = max_length

    def __call__(self, *args: Any, **kwds: Any) -> str:
        range_ = random.randrange(self.min_length, self.max_length)
        return "".join([random.choice(self.psw_chars) for _ in range(range_)])


rnd = RandomPassword("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", 5, 20)
lst_pass = [rnd() for _ in range(3)]
# print(random.choices("qwertyuiopasdfghjklzxcvbnm0123456789!@#$%&*", k=10))
