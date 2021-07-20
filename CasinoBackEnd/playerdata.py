class PlayerData:
    def __init__(self, ID, lastname, firstname, balance, won, lost) -> None:
        self._ID = ID
        self._lastname = lastname
        self._firstname = firstname
        self._balance = balance
        self._won = won
        self._lost = lost


    def set_ID(self, new_ID): 
        # Set ID number (int) here ex.
        self._ID = new_ID        
  

    def set_last_name(self, new_lastname):
        # Set Last Name (str) here ex.
        self._lastname = new_lastname       
    

    def set_first_name(self, new_firstname):
        # Set First Name (str) here ex.
        self._firstname = new_firstname       
        

    def set_finance(self, new_balance, new_won, new_lost):
        # Set Balance, Win, and Lost numbers (int, int, int) here ex.
        self._balance = new_balance
        self._won = new_won
        self._lost = new_lost       


    def get_finance(self):
        # Return List of [Balance, Won, Lost]
        pass