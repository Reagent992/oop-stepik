from typing import Any, List


class Course:
    def __init__(self, name: str) -> None:
        self.name = name
        self.modules: List[Module] = list()

    def add_module(self, modules: "Module") -> None:
        self.modules.append(modules)

    def remove_module(self, index_) -> None:
        self.modules.pop(index_)


class Module:
    def __init__(self, name: str) -> None:
        self.name = name
        self.lessons: List[LessonItem] = list()

    def add_lesson(self, lesson: "LessonItem") -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, index_) -> None:
        self.lessons.pop(index_)


class LessonItem:
    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, name: str, value: Any) -> None:
        """Валидация."""
        if name in ("title") and isinstance(value, str):
            super().__setattr__(name, value)
        elif name in ("practices", "duration") and isinstance(value, int):
            if 0 < value:
                super().__setattr__(name, value)
            else:
                raise TypeError(
                    f"Значение {name} - {value} должно быть положительным."
                )
        else:
            raise TypeError("Неверный тип присваиваемых данных.")

    def __getattr__(self, name) -> bool:
        """Обращение к несуществующему атрибуту."""
        return False

    def __delattr__(self, __name: str) -> None:
        """Запрещено удалять атрибуты."""
        if __name in ("title", "practices", "duration"):
            raise AttributeError(f"Удаление атрибута {__name} - Запрещено.")
        else:
            super().__delattr__(__name)


if __name__ == "__main__":
    course = Course("Python ООП")
    module_1 = Module("Часть первая")
    module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
    module_1.add_lesson(LessonItem("Урок 3", 5, 800))
    course.add_module(module_1)
    module_2 = Module("Часть вторая")
    module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
    module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
    course.add_module(module_2)
