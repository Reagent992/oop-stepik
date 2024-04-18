from typing import List, Union


class Video:
    def create(self, name: str) -> str:
        """задания имени текущего видео"""
        self.name = name
        return self.name

    def play(self) -> None:
        """воспроизведения видео"""
        return print(f"воспроизведение видео {self.name}")


class YouTube:
    videos: List[Video] = list()

    @classmethod
    def add_video(cls, *video: Video) -> List[Video]:
        """для добавления нового видео"""
        for i in video:
            if isinstance(i, Video):
                cls.videos.append(i)
        return cls.videos

    @classmethod
    def play(cls, video_indx: int) -> Union[None, str]:
        """для проигрывания видео из списка по указанному индексу"""
        if isinstance(video_indx, int) and 0 <= video_indx <= len(cls.videos):
            cls.videos[video_indx].play()
            return None
        else:
            return "Индекс находится вне диапазона списка"


v1 = Video()
v1.create("Python")
v2 = Video()
v2.create("Python ООП")
[YouTube.add_video(i) for i in (v1, v2)]
[YouTube.play(i) for i in (0, 1)]
