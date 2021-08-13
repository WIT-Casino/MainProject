try:
    from SQL_Database import SQL_Databases
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases
    
class PlayerSkill:
    def __init__(self, ID, Skill = 1, Cheat = 1, LUCK = 1) -> None:
        self.sql = SQL_Databases()

        self._ID = f"\'{ID}\'"
        self._skill = f"{Skill}"
        self._cheat = f"{Cheat}"
        self._luck = f"{LUCK}"
        
        self.pull_cheat_from_DB()
        self.pull_luck_from_DB()
        self.pull_skill_from_DB()

        


    def get_skill(self):
        return int(self._skill)

    def get_luck(self):
        return int(self._luck)

    def get_cheat(self):
        return int(self._luck)


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

