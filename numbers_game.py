# numbers_game.py
from game_base import GameBase
import random

class NumbersGame(GameBase):
    def __init__(self):
        super().__init__()
    
    def guess_number(self):
        correct_number = random.randint(1, 10)
        guess = int(input("Rate eine Zahl zwischen 1 und 10: "))
        if guess == correct_number:
            print("Richtig geraten!")
        else:
            print(f"Falsch! Die richtige Zahl war {correct_number}.")
