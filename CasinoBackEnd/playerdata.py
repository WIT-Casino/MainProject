try:
    from SQL_Database import SQL_Databases
    
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases
    


class PlayerData:
    def __init__(self, ID, new_player=False, lastname="TBU", firstname="TBU", date=20000101, balance=0, won=0, lost=0):
        # TBU = to be updated
        self.sql = SQL_Databases()

        self._ID = f"\'{ID}\'"
        self._lastname = f"\'{lastname}\'"
        self._firstname = f"\'{firstname}\'"
        self._date = date
        self._balance = balance
        self._won = won
        self._lost = lost

        if new_player is True:
            self.add_player_to_DB()
        else:
            self.pull_firstname_from_DB()
            self.pull_lastname_from_DB()
            self.pull_reg_date_from_DB()
            self.pull_finance_from_DB()

    def get_finance(self):
        """Return balance, total amount won, and total amount lost as a tuple"""
        
        return self._balance, self._won, self._lost

    def update_ID_to_DB(self, new_ID):
        """Updates PID in DB and class's ID attribute with the new_ID"""

        # no \' because self._ID already has them (check above in init)
        condtn = f"PID = {self._ID}"
        update_info = f"PID = \'{new_ID}\'"
        self.sql.update_set_where("PlayerMain", update_info, condtn)
        self.sql.update_set_where("PlayerFinance", update_info, condtn)
        self.sql.update_set_where("Cheater", update_info, condtn)
        self.sql.update_set_where("MatchData", update_info, condtn)
        self.sql.update_set_where("PlayerSkill", update_info, condtn)

        self._ID = f"\'{new_ID}\'"

    def update_lastname_to_DB(self, new_last):
        """Updates player last name in DB and class's last name attribute with the new_last"""

        condtn = f"PID = {self._ID}"
        update_info = f"Last = \'{new_last}\'"
        self.sql.update_set_where("PlayerMain", update_info, condtn)

        self._lastname = f"\'{new_last}\'"

    def update_firstname_to_DB(self, new_first):
        """Updates player first name in DB and class's first name attribute with the new_first"""

        condtn = f"PID = {self._ID}"
        update_info = f"First = \'{new_first}\'"
        self.sql.update_set_where("PlayerMain", update_info, condtn)

        self._lastname = f"\'{new_first}\'"

    def update_finance_to_DB(self, balance, amount_won, amount_lost):
        """Updates balance, amount win, and amount lost in DB and class's attributes with the new finance info"""

        column = ["Balance", "totalWon", "totalLost"]
        finance = [balance, amount_won, amount_lost]

        condtn = f"PID = {self._ID}"
        for c, f in zip(column, finance):
            update_info = f"{c} = {f}"
            self.sql.update_set_where("PlayerFinance", update_info, condtn)

        self._balance = balance         # no \' because they are int
        self._won = amount_won
        self._lost = amount_lost

    def pull_firstname_from_DB(self):
        """Get player's first name from DB and update class attribute"""

        self._firstname = self.sql.select_from_where(
            "PlayerMain", "First", "PID", self._ID)[0][0]
        # Put single quote around it because it is a str
        self._firstname = f"\'{self._firstname}\'"

    def pull_lastname_from_DB(self):
        """Get player's last name from DB and update class attribute"""

        self._lastname = self.sql.select_from_where(
            "PlayerMain", "Last", "PID", self._ID)[0][0]
        # Put single quote around it because it is a str
        self._lastname = f"\'{self._lastname}\'"

    def pull_reg_date_from_DB(self):
        """Get player's regitrastion from DB and update class attribute"""

        self._date = self.sql.select_from_where(
            "PlayerMain", "RegistationDate", "PID", self._ID)[0][0]

    def pull_finance_from_DB(self):
        """Get player's finance from DB and update class attributes"""

        self._balance = self.sql.select_from_where(
            "PlayerFinance", "Balance", "PID", self._ID)[0][0]
        self._lost = self.sql.select_from_where(
            "PlayerFinance", "totalLost", "PID", self._ID)[0][0]
        self._won = self.sql.select_from_where(
            "PlayerFinance", "totalWon", "PID", self._ID)[0][0]

    def add_player_to_DB(self):
        """Add all the new class attributes to DB as a new player"""

        last_id = self.sql.get_last_rowID("PlayerMain")

        if int(self._ID.strip('\'')) < last_id:
            raise Exception(
                f"Player is already in the database. Player ID: {self._ID}. Last ID: {last_id}")
        else:
            val = f"{self._ID}, {self._lastname}, {self._firstname}, {self._date}, 0"
            self.sql.insert_into_table_values("PlayerMain", val)

            val = f"{self._ID}, {self._balance}, {self._lost}, {self._won}"
            self.sql.insert_into_table_values("PlayerFinance", val)


    def get_all_matches(self):
        """Return (MatchID, won, lost amounts, date) of all games played by the player"""

        # Match PID column in MatchData table to find matches
        return self.sql.select_from_where(
            "MatchData", "*", "PID", self._ID)
    
    def get_matches_from_game(self, gameID):
        """Return (MatchID, won, lost amounts, date) of a game played by this player"""

        # Use MatchData table
        # Match PID and parial match between argument gameID and MID column
        all_matches = self.get_all_matches()
        temp_array = []
        for match in all_matches:
            if match[1][0:3] == gameID:
                temp_array.append(match)   
        return temp_array

def main():
    ## BETA TEST USE PLAYER: 00001, Smith, Liam, 20201218, 0 
   # Test 1:
    # player = PlayerData("00001")
    # print(player.get_finance())

    ##############################
   # Test 2: Update Lastname Ex: Smith -> Larry 
    # Lastname_change = "Smith"
    # player.update_lastname_to_DB(Lastname_change)

    ##############################
   # Test 3: Update Firstname Ex: Liam -> Jerry 
    # Firstname_change = "Liam"
    # player.update_firstname_to_DB(Firstname_change)

    ##############################
   # Test 4: Get all matches; Should show all games player has played
    # print(player.get_all_matches())

    ##############################
   # Test 5: Get a match; Should show a game player has played 
    # Gamble_ID = "004"
    # print(player.get_matches_from_game(Gamble_ID))

    ##############################
   # Test 7: Update ID Ex: 00001 -> 01110 
    # ID_change = "01110"
    # player.update_ID_to_DB(ID_change)
    pass

if __name__ == "__main__":
    main()

###################################################
#   Set functions

#     def set_ID(self, new_ID):
#         # Set ID number (int) into temp. constructor ex.
#         self._ID = new_ID

#     def set_last_name(self, new_lastname):
#         # Set Last Name (str) into temp. constructor ex.
#         self._lastname = new_lastname


#     def set_first_name(self, new_firstname):
#         # Set First Name (str) into temp. constructor ex.
#         self._firstname = new_firstname

#     def set_name(self, new_lastname, new_firstname):
#         # Set Last Name (str) here ex.
#         self._lastname = new_lastname
#         self._firstname = new_firstname

#     def set_finance(self, new_balance, new_won, new_lost):
#         # Set Balance, Win, and Lost numbers (int, int, int) into temp. constructor ex.
#         self._balance = new_balance
#         self._won = new_won
#         self._lost = new_lost
#
###################################################
