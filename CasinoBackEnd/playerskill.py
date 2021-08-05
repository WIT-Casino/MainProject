try:
    from SQL_Database import SQL_Databases
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases
    
class PlayerSkill:
    def __init__(self, ID, Skill, Cheat, LUCK) -> None:
            
        self._ID = f"\'{ID}\'"
        self._skill = f"{Skill}"
        self._cheat = f"{Cheat}"
        self._luck = f"{LUCK}"


        self.sql = SQL_Databases()

    def get_skill(self):
        """Return skill"""
        return self._skill

    def get_cheat(self):
        """Return skill"""
        return self._cheat
    
    def get_luck(self):
        """Return skill"""
        return self._luck

    # def update_ID_to_db(self, new_ID):
    #     # pulls ID from temp player and updates the db with the temp ID
    #     condtn = f"PID = \'{self._ID}\'"
    #     self.sql.update_set_where("PlayerMain", new_ID, condtn) 
    #     self.sql.update_set_where("PlayerFinance", new_ID, condtn) 
    #     self.sql.update_set_where("Cheater", new_ID, condtn) 
    #     self.sql.update_set_where("MatchData", new_ID, condtn)
    #     self.sql.update_set_where("PlayerSkill", new_ID, condtn)  
    #     self._ID = new_ID

    def update_skill_to_db(self, new_skill):
        """ pulls skill from temp player and updates the db with the temp skill"""
        condtn = f"Skill = {self._skill}"
        self.sql.update_set_where("PlayerSkill", new_skill, condtn)
        self._skill = new_skill

    def update_cheat_to_db(self, new_cheat):
        """ pulls cheat from temp player and updates the db with the temp cheat"""
        condtn = f"Last = {self._cheat}"
        self.sql.update_set_where("PlayerSkill", new_cheat, condtn)
        self._cheat = new_cheat

    def update_luck_to_db(self, new_luck):
        """ pulls LUCK from temp player and updates the db with the temp LUCK """
        condtn = f"Last = {self._luck}"
        self.sql.update_set_where("PlayerSkill", new_luck, condtn)
        self._luck = new_luck


    def pull_skill_from_DB(self):
        """ go to PlayerSkill table and return Skill"""
        ID_in_quote = f"{self._ID}"
        self._skill = self.sql.select_from_where("PlayerSkill", "Skill", "PID", ID_in_quote)[0][0]
        
    def pull_cheat_from_DB(self):
        """ go to PlayerSkill table and return Cheat stat""" 
        ID_in_quote = f"{self._ID}"
        self._cheat = self.sql.select_from_where("PlayerSkill", "Cheat", "PID", ID_in_quote)[0][0]

    def pull_luck_from_DB(self):
        """ go to PlayerSkill table and return LUCK stat""" 
        ID_in_quote = f"{self._ID}"
        self._luck = self.sql.select_from_where("PlayerSkill", "LUCK", "PID", ID_in_quote)[0][0]

    
    # def update_all(self):
    #     self.update_ID_to_db()
    #     self.update_firstname_to_db()
    #     self.update_lastname_to_db()
    #     self.update_finance_to_db()
