import pytest
import sys

try:
    sys.path.append('.')
    from CasinoBackEnd.SQL_Database import SQL_Databases
except ModuleNotFoundError:
    sys.path.append('..')
    from CasinoBackEnd.SQL_Database import SQL_Databases

from CasinoBackEnd.playerdata import PlayerData

@pytest.fixture
def player_00001():
    player = PlayerData("00001")
    yield player
    del player

def test_get_finance(player_00001):
    finance = player_00001.get_finance()
    assert finance[0] == 2747
    assert finance[1] == 7299
    assert finance[2] == 1896



