try:
    from SQL_Database import SQL_Databases
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases

class IdRule():
    max_player_ID_num = 5
    max_game_ID_num = 3
    max_match_ID_num = 7

    def __init__(self) -> None:
        self.sql = SQL_Databases()

    def create_new_player_ID(self):
        """Return the new player ID in the list"""
        try:
            ID = self.sql.get_last_rowID("PlayerMain") + 1
            return str(ID).zfill(IdRule.max_player_ID_num)
            
        except TypeError:
            print("The table is empty")
            return str(1).zfill(IdRule.max_player_ID_num)
            
        
    
    def create_new_match_ID(self, gameID: int):
        """Return the new match ID in the list"""

        try:
            last_ID = self.sql.get_last_rowID("MatchData") + 1
            
            matchID = str(gameID).zfill(IdRule.max_game_ID_num) + str(last_ID).zfill(IdRule.max_match_ID_num)
            return matchID

        except TypeError:
            print("The table is empty")
            matchID = str(gameID).zfill(IdRule.max_game_ID_num) + str(1).zfill(IdRule.max_match_ID_num)
            return matchID

        
