try:
    from SQL_Database import SQL_Databases
except ModuleNotFoundError:
    import sys
    sys.path.append(".")
    from CasinoBackEnd.SQL_Database import SQL_Databases
    
class PlayerSkill:
        def __init__(self, playerID, skill, cheat, luck) -> None:
            pass