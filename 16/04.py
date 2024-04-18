class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def clone(self):
        obj = super().__new__(Point)
        obj.x = self.x
        obj.y = self.y
        return obj


pt = Point(1, 2)
pt_clone = pt.clone()
assert pt != pt_clone
assert pt.x == pt_clone.x
