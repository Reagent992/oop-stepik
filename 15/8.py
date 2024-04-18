# class ListObject:
#     def __init__(self, data, next_obj=None) -> None:
#         self.data = data
#         self.next_obj = next_obj

#     def link(self, obj):
#         self.next_obj = obj


class ListObject:
    next_obj = None

    def __init__(self, data):
        self.data = data[0]
        if len(data[1:]) != 0:
            self.link(ListObject(data[1:]))

    def link(self, obj):
        self.next_obj = obj


lst_in = [
    "1. Первые шаги в ООП",
    "1.1 Как правильно проходить этот курс",
    "1.2 Концепция ООП простыми словами",
    "1.3 Классы и объекты. Атрибуты классов и объектов",
    "1.4 Методы классов. Параметр self",
    "1.5 Инициализатор init и финализатор del",
    "1.6 Магический метод new. Пример паттерна Singleton",
    "1.7 Методы класса (classmethod) и статические методы (staticmethod)",
]

head_obj = ListObject(lst_in)

# head_obj = None
# for i in lst_in[::-1]:
#     new_node = ListObject(i, head_obj)
#     head_obj = new_node

# t = head_obj
# while t != None:
#     print(t.data)
#     t = t.next_obj
