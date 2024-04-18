import random
from typing import Dict, List, Optional


class Data:
    """Пакет информации"""

    def __init__(self, data: str, ip: int) -> None:
        self.data = data
        self.ip = ip


class Server:
    """Описание работы серверов в сети."""

    ips: list = list()

    @staticmethod
    def generate_random_ip() -> int:
        """Создание уникального, случайного ip."""
        ip = random.randrange(1, 255)
        while ip in Server.ips:
            ip = random.randrange(1, 255)
        Server.ips.append(ip)
        return ip

    def __init__(
        self,
        ip: Optional[int] = None,
        router: Optional["Router"] = None,
    ) -> None:
        self.ip = ip if ip else self.generate_random_ip()
        self.router = router
        self.buffer: list = list()

    def send_data(self, data: Data):
        """Отправка пакета data: Data с указанным IP-адресом получателя
        (пакет отправляется роутеру и сохраняется в его буфере -
        локальном свойстве buffer)"""
        if self.router:
            self.router.buffer.append(data)
        else:
            print("Сервер не подключен к роутеру.")

    def get_data(self):
        """Возвращает список принятых пакетов и очищает входной буфер."""
        result = self.buffer.copy()
        self.buffer = list()
        return result

    def get_ip(self):
        """Возвращает свой IP-адрес."""
        return self.ip


class Router:
    """Роутер. Всего один."""

    obj = None
    servers: Dict[int, Server] = dict()
    buffer: List[Data] = list()

    def __new__(cls):
        """Singleton."""
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj
    
    def link(self, server: Server) -> None:
        """Присоединение сервера к роутеру."""
        self.servers[server.ip] = server
        server.router = self

    @classmethod
    def unlink(cls, server: Server) -> None:
        """Отсоединения сервера server от роутера."""
        cls.servers.pop(server.ip)

    def send_data(self):
        """для отправки всех пакетов (объектов класса Data)
        из буфера роутера соответствующим серверам
        (после отправки буфер должен очищаться)."""
        for package in self.buffer:
            obj = self.servers.get(package.ip)
            if obj:
                obj.buffer.append(package)
        self.buffer.clear()



assert hasattr(Router, 'link') and hasattr(Router, 'unlink') and hasattr(Router, 'send_data'), "в классе Router присутсвутю не все методы, указанные в задании"
assert hasattr(Server, 'send_data') and hasattr(Server, 'get_data') and hasattr(Server, 'get_ip'), "в классе Server присутсвутю не все методы, указанные в задании"

router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

assert len(router.buffer) == 0, "после отправки сообщений буфер в роутере должен очищаться"
assert len(sv_from.buffer) == 0, "после получения сообщений буфер сервера должен очищаться"

assert len(msg_lst_to) == 2, "метод get_data вернул неверное число пакетов"

assert msg_lst_from[0].data == "Hi" and msg_lst_to[0].data == "Hello", "данные не прошли по сети, классы не функционируют должным образом"

assert hasattr(router, 'buffer') and hasattr(sv_to, 'buffer'), "в объектах классов Router и/или Server отсутствует локальный атрибут buffer"

router.unlink(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
router.send_data()
msg_lst_to = sv_to.get_data()
assert msg_lst_to == [], "метод get_data() вернул неверные данные, возможно, неправильно работает метод unlink()"