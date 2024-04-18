from typing import List


class Recipe:
    def __init__(self, *ingredients: "Ingredient") -> None:
        self.__ingredients: List["Ingredient"] = []
        if self.validate(*ingredients):
            self.__ingredients += list(ingredients)

    def add_ingredient(self, *ingredients: "Ingredient") -> None:
        """Добавить ингредиенты в рецепт."""
        if self.validate(*ingredients):
            for i in ingredients:
                self.__ingredients.append(i)

    def remove_ingredient(self, ingredient: "Ingredient") -> None:
        """Удалить ингредиент из рецепта."""
        try:
            self.__ingredients.remove(ingredient)
        except ValueError:
            pass

    def get_ingredients(self) -> List["Ingredient"]:
        """Список ингредиентов."""
        return self.__ingredients

    def __len__(self) -> int:
        """Длина списка ингредиентов."""
        return len(self.__ingredients)

    @staticmethod
    def validate(*ingredients) -> bool:
        return all([type(i) is Ingredient for i in ingredients])


class Ingredient:
    def __init__(self, name: str, volume: int, measure: str) -> None:
        self.name = name if isinstance(name, str) else ""
        self.volume = volume if isinstance(volume, int) else 0
        self.measure = measure if isinstance(measure, str) else ""

    def __str__(self) -> str:
        return f"{self.name}: {self.volume}, {self.measure}"


if __name__ == "__main__":
    ing = Ingredient("Соль", 1, "столовая ложка")
    assert str(ing) == "Соль: 1, столовая ложка"

    recipe = Recipe()
    assert recipe.get_ingredients() == []
    ing1 = Ingredient("Соль", 1, "столовая ложка")
    ing2 = Ingredient("Мука", 1, "кг")
    ing3 = Ingredient("Мясо баранины", 10, "кг")
    recipe.add_ingredient(ing1)
    assert recipe.get_ingredients() == [ing1]
    recipe.add_ingredient(ing2)
    recipe.add_ingredient(ing3)
    ingredients = recipe.get_ingredients()
    assert ingredients == [ing1, ing2, ing3]
    assert len(recipe) == 3
    recipe.remove_ingredient(ing2)
    assert recipe.get_ingredients() == [ing1, ing3]
    assert len(recipe) == 2

    recipe2 = Recipe(ing1, ing2)
    assert recipe2.get_ingredients() == [ing1, ing2]

    try:
        recipe3 = Recipe("abs")  # type: ignore
    except ValueError:
        True
    assert recipe3.get_ingredients() == []
    recipe3.remove_ingredient(ing1)
    assert recipe3.get_ingredients() == []
