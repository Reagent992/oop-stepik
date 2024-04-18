from typing import List, Optional


def type_check_tree_obj(*values: "TreeObj") -> bool:
    result = []
    for value in values:
        if type(value) is TreeObj:
            result.append(True)
        else:
            raise ValueError(f"{value} не является объектом TreeObj.")
    return all(result)


def vector_type_check(vector: List[int]) -> bool:
    """Проверка вектора на содержание только целых чисел."""
    result = []
    for number in vector:
        if isinstance(number, int):
            result.append(True)
        else:
            raise ValueError(f"{number} не является целым числом.")
    return all(result)


class TreeObj:
    """Объект дерева."""

    def __init__(self, indx: int, value: Optional[str] = None) -> None:
        """
        indx:  проверяемый в вершине дерева индекс.
        value: значение.
        """
        self.indx = indx
        self.value = value
        self.__left: Optional["TreeObj"] = None
        self.__right: Optional["TreeObj"] = None

    @property
    def left(self) -> Optional["TreeObj"]:
        """Левый объект дерева."""
        return self.__left

    @left.setter
    def left(self, value: "TreeObj") -> None:
        if type_check_tree_obj(value):
            self.__left = value

    @property
    def right(self) -> Optional["TreeObj"]:
        """Правый объект дерева."""
        return self.__right

    @right.setter
    def right(self, value: "TreeObj") -> None:
        if type_check_tree_obj(value):
            self.__right = value


class DecisionTree:
    """Решающее дерево."""

    @classmethod
    def predict(cls, root: TreeObj, x: list) -> Optional[str]:
        """Построение прогноза(прохода по решающему дереву)
        для вектора x из корневого узла дерева root."""
        type_check_tree_obj(root)
        vector_type_check(x)
        cur_node: Optional["TreeObj"] = root
        cur_index = root.indx
        cur_value: Optional[str] = None
        while cur_node:
            if x[cur_index]:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
            if cur_node:
                cur_value = cur_node.value
                cur_index = cur_node.indx
        return cur_value

    @classmethod
    def add_obj(
        cls, obj: TreeObj, node: Optional["TreeObj"] = None, left: bool = True
    ) -> TreeObj:
        """Добавления вершин в решающее дерево.
        obj - новый, добавляемый объект.
        node - объект, к которому присоединяется obj.
        left - True - к левой ветви; False - к правой ветви.
        """
        type_check_tree_obj(obj)
        if node:
            if left:
                node.left = obj
            else:
                node.right = obj
        return obj


root = DecisionTree.add_obj(TreeObj(0))  # Любит python
v_11 = DecisionTree.add_obj(TreeObj(1), root)  # Понимает ООП
v_12 = DecisionTree.add_obj(TreeObj(2), root, False)  # Любит "кунг-фу панда"
DecisionTree.add_obj(TreeObj(-1, "будет программистом"), v_11)
DecisionTree.add_obj(TreeObj(-1, "будет кодером"), v_11, False)
DecisionTree.add_obj(TreeObj(-1, "не все потеряно"), v_12)
DecisionTree.add_obj(TreeObj(-1, "безнадежен"), v_12, False)

x = [1, 1, 0]  # 1 - да, 0 - нет.
res = DecisionTree.predict(root, x)  # будет программистом
print(res)
