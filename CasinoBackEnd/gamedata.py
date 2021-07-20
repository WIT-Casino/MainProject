from enum import Enum

class GamePrefixID(Enum):
    BlackJack = 1
    Craps = 2

    # TODO: 
    # Fill in more games


class GameData():
    PrefixID: GamePrefixID

    def __init__(self) -> None:
        pass

class G_BlackJack(GameData):
    PrefixID = GamePrefixID.BlackJack