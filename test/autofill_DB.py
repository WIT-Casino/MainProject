import sys
sys.path.append('../')

from CasinoBackEnd import SQL_Database
# from idrule import IdRulepyth
# from playerdata import PlayerData
# from gamedata import GameData


import datetime
from datetime import date, timedelta
import random

def main():
    ID = IdRule()

    with open("names.txt", 'r') as f:
        full_names = [name.strip('\n') for name in f]

    start_date = datetime.date(2018,1,1)
    end_date = datetime.date(2021,7,1)
    range_of_dates = end_date - start_date
    days_in_between = range_of_dates.days
    
    for full_name in full_names:
        fname, lname = full_name.split()
        new_p_id = ID.create_new_player_ID()
        print(new_p_id)

        money = random.randint(0, 5000)
        amount_won = random.randint(0, 5000)
        amount_lost = random.randint(0, 8000)

        random_number_of_days = random.randrange(days_in_between)
        random_date = start_date + timedelta(days=random_number_of_days)
        date_in_int = int(random_date.strftime('%Y%m%d'))
        player = PlayerData(ID=new_p_id, lastname=lname, firstname=fname, balance=money, won=amount_won, lost=amount_lost)
        player.add_player_to_DB(date_in_int)

if __name__ == "__main__":
    main()