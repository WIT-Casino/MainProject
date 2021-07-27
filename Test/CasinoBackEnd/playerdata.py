from SQL_Database import SQL_Databases

class PlayerData:
    def __init__(self, ID, lastname = "TBU", firstname = "TBU", balance = 0, won = 0, lost = 0):
        # TBU = to be updated
        
        self._ID = ID
        self._lastname = lastname
        self._firstname = firstname
        self._balance = balance
        self._won = won
        self._lost = lost

        self.sql = SQL_Databases()


    def set_ID(self, new_ID): 
        # Set ID number (int) here ex.
        self._ID = new_ID        
  

    def set_name(self, new_lastname, new_firstname):
        # Set Last Name (str) here ex.
        self._lastname = new_lastname
        self._firstname = new_firstname


    def set_finance(self, new_balance, new_won, new_lost):
        # Set Balance, Win, and Lost numbers (int, int, int) here ex.
        self._balance = new_balance
        self._won = new_won
        self._lost = new_lost       


    def get_ID_from_DB(self):
        # go to PlayerMain table and return PID
        pass

    def get_name_from_DB(self):
        # go to PlayerMain table and return Last and First
        pass

    def get_finance_from_DB(self):
        # go to PlayerMain table and return Last and First
        pass

    def update_ID_to_DB(self):
        # use sql's UPDATE function to update PID with new self._ID  
        # in the following tables
        # Cheater, MatchData, PlayerFinance, PlayerMain, PlayerSkill
        pass

    def update_name_to_DB(self):
        # update Last and First in PlayerMain
        pass

    def update_finance_to_DB(self):
        # update Balance, totalLost, and totalWon in PlayerFinance
        pass

    def update_all(self):
        self.update_ID_to_DB()
        self.update_name_to_DB()
        self.update_finance_to_DB()

    def add_player_to_DB(self, date):
        last_id = self.sql.get_last_rowID("PlayerMain")
        if int(self._ID) < last_id:
            raise Exception(f"Player is already in the database. Player ID: {self._ID}. Last ID: {last_id}")
        else:
            val = f"\'{self._ID}\', \'{self._lastname}\', \'{self._firstname}\', {date}, 0"
            print(val)
            self.sql.insert_into_table_values("PlayerMain", val)

            val = f"\'{self._ID}\', {self._balance}, {self._lost}, {self._won}"
            self.sql.insert_into_table_values("PlayerFinance", val)

        

