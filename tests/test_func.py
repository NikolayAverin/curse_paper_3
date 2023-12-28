from src.func import get_user_operations


def test_get_user_operations():
    assert len(get_user_operations()) == 5