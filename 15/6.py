from typing import List


class CPU:
    def __init__(self, name: str, fr: int) -> None:
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name: str, volume: int) -> None:
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name: str, cpu: CPU, mem_slots: List[Memory]) -> None:
        self.total_mem_slots = 4
        self.name = name
        self.cpu = cpu
        self.mem_slots = mem_slots

    def get_config(self) -> List[str]:
        m = [
            f"{obj.name} - {obj.volume}"
            for index, obj in enumerate(self.mem_slots)
            if index <= self.total_mem_slots
        ]
        return [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
            "Память: " + "; ".join(m),
        ]


mem1 = Memory("ДядяАли1", 9999)
mem2 = Memory("ДядяАли2", 9999)
mem3 = Memory("ДядяАли3", 9999)
mem4 = Memory("ДядяАли4", 9999)
cpu = CPU("Intel", 4000)
mb = MotherBoard("Gigabyte", cpu, [mem1, mem2, mem3, mem4])

# cpu = CPU("asus", 1333)
# mem1, mem2 = Memory("Kingstone", 4000), Memory("Kingstone", 4000)
# mb = MotherBoard("Asus", cpu, [mem1, mem2])
# print(mb.get_config())

print("\n".join(mb.get_config()))

assert isinstance(mb, MotherBoard) and hasattr(MotherBoard, "get_config")


def get_config():
    mem_str = "; ".join([f"{x.name} - {x.volume}" for x in mb.mem_slots])

    return [
        f"Материнская плата: {mb.name}",
        f"Центральный процессор: {mb.cpu.name}, {mb.cpu.fr}",
        f"Слотов памяти: {mb.total_mem_slots}",
        f"Память: {mem_str}",
    ]


res1 = ("".join(mb.get_config())).replace(" ", "")
res2 = ("".join(get_config())).replace(" ", "")
assert res1 == res2, "метод get_config возвратил неверные данные"
