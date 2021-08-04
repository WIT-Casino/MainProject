from enum import Enum

try:
    from SQL_Database import SQL_Databases
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases
    
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
        
        self.matchID = f"\'{matchID}\'"
        self.amountWon = amountWon
        self.amountLost = amountLost
        self.date = date

    def pull_data_from_DB(self):
        # retrive amount won,  amount lost, and date in MatchData table by matching self.ID with MID
        self.amountWon = self.sql.select_from_where("MatchData", "Won", "MID", self.matchID)[0][0]
        self.amountLost = self.sql.select_from_where("MatchData", "Lost", "MID", self.matchID)[0][0]
        self.date = self.sql.select_from_where("MatchData", "Date", "MID", self.matchID)[0][0]

    def update_data_to_DB(self, new_amountWon, new_amountLost, new_date):
        # Find the difference between class amount won and lost VS stored amount won and lost in the DB
        # then update the amounts appropriately to the MatchData, PlayerFinance, and GameMain tables
        # GID is the first 3 digits of MID
        stored_Won = self.sql.select_from_where("MatchData", "Won", "MID", self.matchID)[0][0]
        stored_Lost = self.sql.select_from_where("MatchData", "Lost", "MID", self.matchID)[0][0]
        
        if stored_Won == 0 and stored_Lost == 0:
            self.sql.update_set_where("MatchData", "Won", "PID", self.amountWon)
            self.sql.update_set_where("MatchData", "Lost", "PID", self.amountLost)
            self.sql.update_set_where("MatchData", "Date", "PID", self.date)

        self.amountWon = new_amountWon
        self.amountLost = new_amountLost
        self.date = new_date

class GameData:
    PrefixID: GamePrefixID
    
    def __init__(self, gameID) -> None:
        self.sql = SQL_Databases()
        self.gameID = gameID
        self.totalPlayerWon = 0
        self.totalPlayerLost = 0

    def pull_data_from_DB(self):
        # from GameMain
        self.totalPlayerWon = self.sql.select_from_where("GameMain", "TotalPlayerWon", "GID", self.gameID)[0][0]
        self.totalPlayerLost = self.sql.select_from_where("GameMain", "TotalPlayerLost", "GID", self.gameID)[0][0]

    def update_data_to_DB(self, new_playerWon, new_playerLost):
        # Find the difference between class amount won and lost VS stored amount won and lost in the DB
        # then update the amounts appropriately to the MatchData, PlayerFinance, and GameMain tables
        # GID is the first 3 digits of MID
        stored_Won = self.sql.select_from_where("GameMain", "TotalPLayerWon", "GID", self.gameID)[0][0]
        stored_Lost = self.sql.select_from_where("GameMain", "TotalPlayerLost", "GID", self.gameID)[0][0]
        
        if stored_Won == 0 and stored_Lost == 0:
            self.sql.update_set_where("GameMain", "TotalPlayerWon", "GID", self.totalPlayerWon)
            self.sql.update_set_where("GameMain", "TotalPlayerLost", "GID", self.totalPlayerLost)
  
        self.totalPlayerWon = new_playerWon
        self.totalPlayerLost = new_playerLost

class G_BlackJack(MatchData, GameData):
    """Black Jack- try to get 21, number cars = value ace can be 1 or 11 face cards are 10, bust if hit over 21"""
    PrefixID = GamePrefixID.BlackJack

class G_Craps(MatchData, GameData):
    """Craps- """
    PrefixID = GamePrefixID.Craps

class G_Roulette(GameData):
    """Roulette- 1 to 10 and 19 to 28, odd numbers are red and even are black. In ranges from 11 to 18 and 29 to 36, odd numbers are black and even are red"""
    PrefixID = GamePrefixID.Roulette

class G_Slots(GameData):
    """Slots- Pull"""
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

