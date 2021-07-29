from SQL_Database import SQL_Databases

class IdRule():
    max_player_ID_num = 5
    max_game_ID_num = 3
    max_match_ID_num = 7

    def __init__(self) -> None:
        self.sql = SQL_Databases()

    def create_new_player_ID(self):
        try:
            ID = self.sql.get_last_rowID("PlayerMain") + 1
            return str(ID).zfill(IdRule.max_player_ID_num)
            
        except TypeError:
            print("The table is empty")
            return str(1).zfill(IdRule.max_player_ID_num)
            
        
    
    def create_new_match_ID(self, gameID: int):
        try:
            matchID = self.sql.get_last_rowID("MatchDetails") + 1
            matchID = str(gameID).zfill(IdRule.max_game_ID_num) + str(matchID).zfill(IdRule.max_match_ID_num)
            return matchID

        except TypeError:
            print("The table is empty")
            matchID = str(gameID).zfill(IdRule.max_game_ID_num) + str(1).zfill(IdRule.max_match_ID_num)
            return matchID

        
