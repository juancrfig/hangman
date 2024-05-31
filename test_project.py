import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from project import get_random_word, game_engine, initial_message

def test_get_random_word():
    assert get_random_word('easy') in ['APPLE', 'BRAIN', 'FLOOR', 'ISSUE', 'MONEY']
    
def test_game_engine():
    with pytest.raises(TypeError):
        game_engine(123)

def test_initial_message():
    assert initial_message() == 0