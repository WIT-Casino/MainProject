from SQL_Database import SQL_Databases

class PlayerData:
    def __init__(self, ID, lastname, firstname, balance, won, lost) -> None:
        self._ID = ID
        self._lastname = lastname
        self._firstname = firstname
        self._balance = balance
        self._won = won
        self._lost = lost

        self.sql = SQL_Databases()


    def set_ID(self, new_ID): 
        # Set ID number (int) into temp. constructor ex.
        self._ID = new_ID        

    def set_last_name(self, new_lastname):
        # Set Last Name (str) into temp. constructor ex.
        self._lastname = new_lastname       
    

    def set_first_name(self, new_firstname):
        # Set First Name (str) into temp. constructor ex.
        self._firstname = new_firstname       
        

    def set_finance(self, new_balance, new_won, new_lost):
        # Set Balance, Win, and Lost numbers (int, int, int) into temp. constructor ex.
        self._balance = new_balance
        self._won = new_won
        self._lost = new_lost       

    def update_ID_to_db(self):
        # pulls ID from temp player and updates the db with the temp ID
        pass

    def update_lastname_to_db(self):
        # pulls last name from temp player and updates the db with the temp last name
        pass

    def update_firstname_to_db(self):
        # pulls first name from temp player and updates the db with the temp first name
        pass
    
    def update_finance_to_db(self):
        # pulls balance, wins/losses from temp player and updates the db with the temp balance, wins/losses
        pass

    def get_finance(self):
        # Return List of [Balance, Won, Lost]
        pass

    def get_player_info(self):
        # Return List of [ID, First Name, Last Name]
        pass