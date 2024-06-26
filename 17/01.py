# Здесь объявляется класс Factory
class Factory:
    @staticmethod
    def build_sequence():
        """создания пустого списка"""
        return list()

    @staticmethod
    def build_number(string):
        """преобразования строки (string) в целое число"""
        return int(string)


class Loader:
    @staticmethod
    def parse_format(string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


# эти строчки не менять!
res = Loader.parse_format("1, 2, 3, -5, 10", Factory)
