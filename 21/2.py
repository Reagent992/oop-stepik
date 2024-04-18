class Money:
    def __init__(self, money: int) -> None:
        self.__money = money

    def set_money(self, money: int):
        if self.check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn: "Money"):
        self.__money += mn.__money

    @classmethod
    def check_money(cls, money):
        return isinstance(money, int) and money > 0


mn_1 = Money(10)
mn_2 = Money(20)
assert mn_1._Money__money == 10 and mn_2._Money__money == 20, "неверные значения в локальном приватном атрибуте __money"

mn_1.set_money(100)
mn_2.add_money(mn_1)
assert mn_1.get_money() == 100 and mn_2.get_money() == 120, "неверное количество средств: возможно некорректая работа методов set_money и/или add_money"

mn_1.set_money(-1)
assert mn_1.get_money() == 100, "неверное количество средств: некорректная работа метода set_money"