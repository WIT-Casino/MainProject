class IdRule():
    max_player_ID_num = 5
    max_game_ID_num = 3
    max_match_ID_num = 7

    def get_new_player_ID(self, ID):
        return str(ID).zfill(IdRule.max_player_ID_num)

    def get_new_game_ID(self, ID):
        return str(ID).zfill(IdRule.max_game_ID_num)
    
    def get_new_match_ID(self, gameID, matchID):
        return self.get_new_game_ID(gameID) + str(matchID).zfill(IdRule.max_match_ID_num)

        
