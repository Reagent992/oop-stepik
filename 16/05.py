# Здесь объявляется класс Factory
class Factory:
    def build_sequence(self):
        """Создание начального пустого списка."""
        return []

    def build_number(self, string):
        """Преобразования переданной в метод строки (string)
        в вещественное значение."""
        return float(string)


class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
# ld = Loader()
# s = input()
# res = ld.parse_format(s, Factory())
ld = Loader()
res = ld.parse_format("4, 5, -6.5", Factory())
assert res == [4.0, 5.0, -6.5]
