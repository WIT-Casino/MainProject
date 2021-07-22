from enum import Enum
from SQL_Database import SQL_Databases
from idrule import IdRule

class GamePrefixID(Enum):
    BlackJack = 1
    Craps = 2
    Roulette =3 
    Slots = 4
    Keno = 5
    Poker = 6
    Baccarat = 7
    BigSix = 8
     

    # TODO: 
    # Fill in more games


class GameData():
    PrefixID: GamePrefixID

    def __init__(self, matchID, newMatch = False) -> None:
        self.sql = SQL_Databases()
        
        self.matchID = matchID
        self.amountWon = 0
        self.amountLost = 0
        self.date = 0

        if not newMatch:
            #get_data_from_database
            #set_data
            pass
        

    def set_data(self):
        #
        pass

    def get_data_from_database(self):
        pass

    def update_date_to_database(self):
        pass


class G_BlackJack(GameData):
    """Black Jack- try to get 21, number cars = value ace can be 1 or 11 face cards are 10, bust if hit over 21"""
    PrefixID = GamePrefixID.BlackJack

class G_Craps(GameData):
    """Craps- """
    PrefixID = GamePrefixID.Craps

class G_Roulette(GameData):
    """Roulette"""
    PrefixID = GamePrefixID.Roulette

class G_Slots(GameData):
    """Slots"""
    PrefixID = GamePrefixID.Slots

class G_Keno(GameData):
    """Keno- Player pick 20 numbers fro 1-80, numbers picked payout on how many right numbers picked """
    PrefixID = GamePrefixID.Keno

class G_Poker(GameData):
    """Poker"""
    PrefixID = GamePrefixID.Poker

class G_Baccarat(GameData):
    """Baccarat- played against dealer 2-9 cards are value ace is 1, rest=0, add hand take ones place number as score 0-9"""
    PrefixID = GamePrefixID.Baccarat

class G_BigSix(GameData):
    """Big Six, Wheel of Fortune- """
    PrefixID = GamePrefixID.BigSix
    