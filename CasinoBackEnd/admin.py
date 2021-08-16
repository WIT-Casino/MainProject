from typing import List

try:
    from SQL_Database import SQL_Databases
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases


class Admin:
    def __init__(self) -> None:
        self.sql = SQL_Databases()

    def get_all_players_basic_info(self) -> List:
        """Return a list of player info: PID, firstname, lastname, registration date, and cheater value"""

        return self.sql.select_from("PlayerMain", "*")

    def get_all_players_finance(self) -> List:
        """Return a list of player info: PID, balance, total amount won, and total amount loss"""

        return self.sql.select_from("PlayerFinance", "*")

def main():
    # ad = Admin()
    # for i in ad.get_all_players_finance():
    #     print(i)
    pass

if __name__=="__main__":
    main()


    