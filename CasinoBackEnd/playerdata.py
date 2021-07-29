from SQL_Database import SQL_Databases

class PlayerData:
    def __init__(self, ID, lastname = "TBU", firstname = "TBU", balance = 0, won = 0, lost = 0):
        # TBU = to be updated
        
        self._ID = f"\'{ID}\'"
        self._lastname = f"\'{lastname}\'"
        self._firstname = f"\'{firstname}\'"
        self._balance = balance
        self._won = won
        self._lost = lost

        self.sql = SQL_Databases()


#     def set_ID(self, new_ID): 
#         # Set ID number (int) into temp. constructor ex.
#         self._ID = new_ID        

# # <<<<<<< HEAD
#     def set_last_name(self, new_lastname):
#         # Set Last Name (str) into temp. constructor ex.
#         self._lastname = new_lastname       
    

#     def set_first_name(self, new_firstname):
#         # Set First Name (str) into temp. constructor ex.
#         self._firstname = new_firstname       
        
# # =======
#     def set_name(self, new_lastname, new_firstname):
#         # Set Last Name (str) here ex.
#         self._lastname = new_lastname
#         self._firstname = new_firstname

# # >>>>>>> 6a45be68a39b70934de3e78896f6f17973f2d685

#     def set_finance(self, new_balance, new_won, new_lost):
#         # Set Balance, Win, and Lost numbers (int, int, int) into temp. constructor ex.
#         self._balance = new_balance
#         self._won = new_won
#         self._lost = new_lost       

    def update_ID_to_db(self, new_ID):
        # pulls ID from temp player and updates the db with the temp ID
        condtn = f"PID = \'{self._ID}\'"
        self.sql.update_set_where("PlayerMain", new_ID, condtn) 
        self.sql.update_set_where("PlayerFinance", new_ID, condtn) 
        self.sql.update_set_where("Cheater", new_ID, condtn) 
        self.sql.update_set_where("MatchData", new_ID, condtn)
        self.sql.update_set_where("PlayerSkill", new_ID, condtn)  
        self._ID = new_ID
        

    def update_lastname_to_db(self, new_last):
        # pulls last name from temp player and updates the db with the temp last name
        condtn = f"Last = \'{self._lastname}\'"
        self.sql.update_set_where("PlayerMain", new_last, condtn)
        self._lastname = new_last

    def update_firstname_to_db(self, new_first):
        # pulls first name from temp player and updates the db with the temp first name
        condtn = f"First = \'{self._firstname}\'"
        self.sql.update_set_where("PlayerMain", new_first, condtn)
        self._firstname = new_first

    def update_finance_to_db(self, new_finance):
        # pulls balance, wins/losses from temp player and updates the db with the temp balance, wins/losses
        condtn = f"Balance = {self._balance}"
        self.sql.update_set_where("PlayerFinance", new_finance, condtn)
        self._balance = new_finance

    # def get_ID_from_DB(self):
    #     # go to PlayerMain table and return PID
    #     self.sql.select_from("PlayerMain", ID = self._ID)
    #     # need actual table name

    def get_firstname_from_DB(self):
        # go to PlayerMain table and return Last and First
        ID_in_quote = f"\'{self._ID}\'"
        self._firstname = self.sql.select_from_where("PlayerMain", "First", "PID", ID_in_quote)[0][0]
        
    def get_lastname_from_DB(self):
        # go to PlayerMain table and return Last and First
        ID_in_quote = f"\'{self._ID}\'"
        self._lastname = self.sql.select_from_where("PlayerMain", "Last", "PID", ID_in_quote)[0][0]

    def get_finance_from_DB(self):
        # go to PlayerMain table and return Last and First
        ID_in_quote = f"\'{self._ID}\'"
        self._balance = self.sql.select_from_where("PlayerFinance", "Balance", "PID", ID_in_quote)[0][0]

    # def update_ID_to_DB(self):
    #     # use sql's UPDATE function to update PID with new self._ID  
    #     # in the following tables
    #     # Cheater, MatchData, PlayerFinance, PlayerMain, PlayerSkill
    #     pass

    # def update_name_to_DB(self):
    #     # update Last and First in PlayerMain
    #     pass

    # def update_finance_to_DB(self):
    #     # update Balance, totalLost, and totalWon in PlayerFinance
    #     pass

    def update_all(self):
        self.update_ID_to_db()
        self.update_firstname_to_db()
        self.update_lastname_to_db()
        self.update_finance_to_db()

def main():
    pd = PlayerData("00001")
    pd.get_finance_from_DB()
    pd.get_lastname_from_DB()
    pd.get_firstname_from_DB()
    print(pd._balance)
    print(pd._firstname)
    print(pd._lastname)

if __name__ == "__main__":
    main()
