from threading import active_count
import pytest

from guessing_game.game import GuessingGame



def test_player_name():
    player = GuessingGame('ibrahim')
    actual = player.player
    expected = "ibrahim"
    assert actual == expected


def test_random_num():
    player=GuessingGame('ehab')
    actual=player.number
    excepted=actual > 0 and actual <21
    assert excepted

def test_game_score():

    player=GuessingGame('ehab')
    actual=player.score
    excepted=0
    assert excepted == actual


def test_guessed_num():

    player=GuessingGame('ehab')
    actual=player.guessed_number
    excepted=''
    assert excepted == actual

def test_input():
    player =GuessingGame('hani')
    player.guessed_number=10
    player.number=10
    actual=player.guess_number()
    excepted =  print(f'congrats ! , You win the number is {player.number} and your score is : 10 ')  

    assert excepted == actual
