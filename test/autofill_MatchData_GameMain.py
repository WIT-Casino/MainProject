import sys
from typing import List
import datetime
import random


try:
    sys.path.append('.')
    from CasinoBackEnd.SQL_Database import SQL_Databases
except ModuleNotFoundError:
    sys.path.append('..')
    from CasinoBackEnd.SQL_Database import SQL_Databases

from CasinoBackEnd.idrule import IdRule
from CasinoBackEnd.playerdata import PlayerData
from CasinoBackEnd.gamedata import GameData


####
# go to player finance get totalWon, totalLost

# generarte random number of matches (3-25)
# randomly assigning won and loses to each match 
# so that the sum of wins and loses equal to the total amounts in playerFinance

# generate random games ID and insert it into PlayerFinance table
# also add to the GameMain total amount wins and loses

####

class autofill_MD_GM():
    def __init__(self) -> None:
        self.sql = SQL_Databases()
        self.gameID = IdRule()

    def get_player_total_win_and_loses(self)->List:
        attr = "PID, Balance, totalWon, totalLost"
        data = self.sql.select_from("PlayerFinance", attr)
        return data
    
    def fill_MatchData_and_GameMain(self):
        data = self.get_player_total_win_and_loses()
        start_date = datetime.date(2018,1,1)
        end_date = datetime.date(2021,7,1)
        
        total_won = [0]*9
        total_lost = [0] * 9

        for player in data:
            num_matches = random.randint(10,25)
            win_matches = self.paritions_in_range(player[2],num_matches)
            lose_matches = self.paritions_in_range(player[3], num_matches)

            p_id = player[0]

            
            for w, l in zip(win_matches, lose_matches):
                g_id = random.randint(1,8)
                m_id = self.gameID.create_new_match_ID(g_id)
                date = self.random_date(start_date, end_date)
                
                value = f"'{p_id}', '{m_id}', {date}, {w}, {l}"
                print(value)
                self.sql.insert_into_table_values("MatchData", value)

                total_won[g_id] = total_won[g_id] + w
                total_lost[g_id] = total_lost[g_id] + l
        
        for i, (w, l) in enumerate(zip(total_won, total_lost), start= 0):
            if i == 0:
                continue
            newInfo = f"TotalPlayerWon = '{w}', TotalPlayerLost = '{l}'"
            condt = f"GID = '00{i}'"
            print(condt, newInfo)
            self.sql.update_set_where("GameMain", newInfo, condt)

        
                



    @staticmethod
    def paritions_in_range(amount, matches):
        k = matches - 1
        p = int(amount/k)
        
        partitioned_amount = [random.randint(int(p/2), p) for _ in range(k)]
        partitioned_amount.append(amount - sum(partitioned_amount))
        
        return partitioned_amount

    @staticmethod    
    def random_date(start_date, end_date):
        range_of_dates = end_date - start_date
        days_in_between = range_of_dates.days
        random_number_of_days = random.randrange(days_in_between)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return int(random_date.strftime('%Y%m%d'))


def main():
    autofill = autofill_MD_GM()
    autofill.fill_MatchData_and_GameMain()



if __name__ == "__main__":
    main()
