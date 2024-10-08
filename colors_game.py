# colors_game.py
from game_base import GameBase
import random

class ColorsGame(GameBase):
    def __init__(self):
        super().__init__()
        self.colors = ['rot', 'blau', 'grün', 'gelb']
    
    def guess_color(self):
        correct_color = random.choice(self.colors)
        guess = input("Rate eine Farbe (rot, blau, grün, gelb): ").lower()
        if guess == correct_color:
            print("Richtig geraten!")
        else:
            print(f"Falsch! Die richtige Farbe war {correct_color}.")
