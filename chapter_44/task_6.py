from typing import Optional

CURRENT_OS = "windows"  # 'windows', 'linux'


class WindowsFileDialog:
    def __init__(self, title, path, exts) -> None:
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


class LinuxFileDialog:
    def __init__(self, title, path, exts) -> None:
        self.__title = title  # заголовок диалогового окна
        self.__path = path  # начальный каталог с файлами
        self.__exts = exts  # кортеж из отображаемых расширений файлов


# здесь объявляйте класс FileDialogFactory
class FileDialogFactory:
    @classmethod
    def create_windows_filedialog(cls, *args, **kwargs) -> WindowsFileDialog:
        return WindowsFileDialog(*args, **kwargs)

    @classmethod
    def create_linux_filedialog(cls, *args, **kwargs) -> LinuxFileDialog:
        return LinuxFileDialog(*args, **kwargs)

    def __new__(
        cls, *args, **kwargs
    ) -> Optional[Union[WindowsFileDialog, LinuxFileDialog]]:
        if CURRENT_OS == "windows":
            return cls.create_windows_filedialog(*args, **kwargs)
        if CURRENT_OS == "linux":
            return cls.create_linux_filedialog(*args, **kwargs)

if __name__ == "__main__":
    dlg = FileDialogFactory(
        "Изображения", "d:/images/", ("jpg", "gif", "bmp", "png")
    )
    assert type(dlg) == WindowsFileDialog
