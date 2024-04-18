from abc import ABCMeta, abstractmethod


class MontyPython(metaclass=ABCMeta):
    @abstractmethod
    def joke(self):
        pass

    @abstractmethod
    def punchline(self):
        pass


class ArgumentClinic(MontyPython):
    def joke(self):
        return "Hahahahahah"


c = ArgumentClinic()
