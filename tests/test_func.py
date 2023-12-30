from src.func import *


def test_get_user_operations():
    assert len(get_user_operations()) == 5
