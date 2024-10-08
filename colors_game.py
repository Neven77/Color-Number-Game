# colors_game.py
from game_base import GameBase
import random

class ColorsGame(GameBase):
    def __init__(self):
        super().__init__()
        self.colors = ['red', 'blue', 'green', 'yellow']
    
    def guess_color(self):
        correct_color = random.choice(self.colors)
        guess = input("Rate eine Farbe (red, blue, green, yellow): ").lower()
        if guess == correct_color:
            print("Richtig geraten!")
        else:
            print(f"Falsch! Die richtige Farbe war {correct_color}.")
