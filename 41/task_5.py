from typing import Any


class Validator:
    def _is_valid(self, data) -> bool:
        return True

    def __call__(self, data: Any) -> Any:
        if not self._is_valid(data):
            raise ValueError("данные не прошли валидацию")
        return self._is_valid(data)


class IntegerValidator(Validator):
    def __init__(self, min_value: int, max_value: int) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data) -> bool:
        return (
            isinstance(data, int)
            and self.min_value <= data <= self.max_value
        )


class FloatValidator(Validator):
    def __init__(self, min_value: float, max_value: float) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def _is_valid(self, data) -> bool:
        return (
            isinstance(data, float)
            and self.min_value <= data <= self.max_value
        )
