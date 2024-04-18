import sys


class Player:
    def __init__(self, name: str, old: int, score: int) -> None:
        self.name = name
        self.old = old
        self.score = score

    def __bool__(self) -> bool:
        return self.score > 0


if __name__ == "__main__":
    Test = True
    if Test:
        lst_in = """
    Балакирев; 34; 2048
    Mediel; 27; 0
    Влад; 18; 9012
    Nina P; 33; 0
    """.strip().split(
            "\n"
        )
    else:
        lst_in = list(map(str.strip, sys.stdin.readlines()))

    players = []
    for string in lst_in:
        name, old, score = string.split("; ")
        players.append(Player(str(name), int(old), int(score)))

    players_filtered = list(filter(bool, players))
