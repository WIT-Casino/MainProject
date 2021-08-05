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
        return self.sql.select_from("PlayerMain", "*")

    def get_all_players_finance(self) -> List:
        return self.sql.select_from("PlayerFinance", "*")

def main():
    # ad = Admin()
    # for i in ad.get_all_players_finance():
    #     print(i)
    pass

if __name__=="__main__":
    main()


    