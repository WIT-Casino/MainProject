import sys
import pytest

try:
    sys.path.append('.')
    from CasinoBackEnd.SQL_Database import SQL_Databases
except ModuleNotFoundError:
    sys.path.append('..')
    from CasinoBackEnd.SQL_Database import SQL_Databases



class TestCases():
    pass