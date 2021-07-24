from SQL_Database import SQL_Databases

sql = SQL_Databases()

cheaters = sql.select_from("MatchDetails", "*")

for cheater in cheaters:
    print(cheater)