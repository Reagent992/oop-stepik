class Model:
    def __init__(self):
        self.storage = {}

    def query(self, **kwargs):
        self.storage = kwargs

    def __str__(self) -> str:
        if self.storage:
            list_ = [f"{k} = {v}" for k, v in self.storage.items()]
            result = ", ".join(list_)
            return f"Model: {result}"
        else:
            return "Model"


if __name__ == "__main__":
    model = Model()
    model.query(id=1, fio="Sergey", old=33)
    print(model)
