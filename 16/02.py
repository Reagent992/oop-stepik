from typing import List


class SingletonFive:
    __CONSANT = 5
    objects: List["SingletonFive"] = []
    __index = 0

    def __new__(cls, *args, **kwargs):
        if len(cls.objects) < cls.__CONSANT:
            obj = super().__new__(cls)
            cls.objects.append(obj)
            return obj
        return cls.objects[4]

    #     elif cls.__index <= 4:
    #         obj = cls.objects[cls.__index]
    #         cls.__index += 1
    #         return obj
    #     else:
    #         cls.__index = 0
    #         return cls.objects[cls.__index]

    def __init__(self, name) -> None:
        self.name = name


objs = [SingletonFive(str(n)) for n in range(10)]
t = "t"
assert objs[4] == objs[5]
