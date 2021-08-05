import sys
from typing import List
import random


try:
    sys.path.append('.')
    from CasinoBackEnd.SQL_Database import SQL_Databases
except ModuleNotFoundError:
    sys.path.append('..')
    from CasinoBackEnd.SQL_Database import SQL_Databases


def main():

    sql =SQL_Databases()
    p_id = sql.select_from("PlayerMain", "PID")

    for id in p_id:
        skill = random.randint(1,10)
        cheat = random.randint(0,5)
        luck = random.randint(1,3)

        value = f"'{id[0]}', {skill}, {cheat}, {luck}"
        print(value)
        sql.insert_into_table_values("PlayerSkill", value)



if __name__ == "__main__":
    main()
