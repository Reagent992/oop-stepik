from typing import Optional


class Layer:
    def __init__(self) -> None:
        self.next_layer: Optional["Layer"] = None
        self.name = "Layer"

    def __call__(self, new_obj: "Layer") -> "Layer":
        self.next_layer = new_obj
        return new_obj


class Input(Layer):
    def __init__(self, inputs: int) -> None:
        super().__init__()
        self.inputs = inputs
        self.name = "Input"


class Dense(Layer):
    def __init__(self, inputs: int, outputs: int, activation: str) -> None:
        super().__init__()
        self.inputs = inputs
        self.inputs = inputs
        self.outputs = outputs
        self.activation = activation
        self.name = "Dense"


class NetworkIterator:
    """Iterator of layers for neural network."""

    def __init__(self, network: Layer) -> None:
        self.network = network

    def __iter__(self):
        layer = self.network
        while layer:
            yield layer
            layer = layer.next_layer


if __name__ == "__main__":
    first_layer = Layer()
    second_layer = first_layer(Layer())
    assert first_layer.next_layer == second_layer

    nt = Input(12)
    layer = nt(Dense(nt.inputs, 1024, "relu"))
    layer = layer(Dense(layer.inputs, 2048, "relu"))
    layer = layer(Dense(layer.inputs, 10, "softmax"))

    n = 0
    for x in NetworkIterator(nt):
        assert isinstance(
            x, Layer
        ), "итератор должен возвращать объекты слоев с базовым классом Layer"
        n += 1

    assert n == 4, "итератор перебрал неверное число слоев"
