from enum import Enum
from SQL_Database import SQL_Databases

class GamePrefixID(Enum):
    BlackJack = 1
    Craps = 2
    Roulette =3 
    Slots = 4
    Keno = 5
    Poker = 6
    Baccarat = 7
    BigSix = 8

class MatchData:

    def __init__(self, matchID, date, amountWon = 0, amountLost = 0) -> None:
        self.sql = SQL_Databases()
        
        self.matchID = matchID
        self.amountWon = amountWon
        self.amountLost = amountLost
        self.date = date


    def set_amount(self, amountWon, amountLost):
        # set the two ammount attributes
        pass

    def set_date(self, date):
        # set date attributes
        pass

    def get_data_from_DB(self):
        # retrive amount won,  amount lost, and date in MatchData table by matching self.ID with MID
        pass    

    def update_data_to_DB(self):
        # Find the difference between class amount won and lost VS stored amount won and lost in the DB
        # then update the amounts appropriately to the MatchData, PlayerFinance, and GameMain tables
        # GID is the first 3 digits of MID
        pass

class GameData:
    PrefixID: GamePrefixID
    
    def __init__(self, gameID) -> None:
        self.gameID = gameID
        self.totalPlayerWon = 0
        self.totalPlayerLost = 0

    def set_amount_won(self, amountWon):
        # set to class attribute
        pass

    def set_amount_lost(self, amountLost):
        # set to class attribute
        pass

    def get_amount_from_DB(self):
        # from GameMain
        pass
    

class G_BlackJack(MatchData, GameData):
    """Black Jack- try to get 21, number cars = value ace can be 1 or 11 face cards are 10, bust if hit over 21"""
    PrefixID = GamePrefixID.BlackJack

class G_Craps(MatchData, GameData):
    """Craps- """
    PrefixID = GamePrefixID.Craps

class G_Roulette(MatchData, GameData):
    """Roulette"""
    PrefixID = GamePrefixID.Roulette

class G_Slots(MatchData, GameData):
    """Slots"""
    PrefixID = GamePrefixID.Slots

class G_Keno(MatchData, GameData):
    """Keno- Player pick 20 numbers fro 1-80, numbers picked payout on how many right numbers picked """
    PrefixID = GamePrefixID.Keno

class G_Poker(MatchData, GameData):
    """Poker"""
    PrefixID = GamePrefixID.Poker

class G_Baccarat(MatchData, GameData):
    """Baccarat- played against dealer 2-9 cards are value ace is 1, rest=0, add hand take ones place number as score 0-9"""
    PrefixID = GamePrefixID.Baccarat

class G_BigSix(MatchData, GameData):
    """Big Six, Wheel of Fortune- """
    PrefixID = GamePrefixID.BigSix
    