# numbers_game.py
from game_base import GameBase
import random

class NumbersGame(GameBase):
    def __init__(self):
        super().__init__()
    
    def guess_number(self):
        # Wählt eine zufällige Zahl zwischen 1 und 99
        correct_number = random.randint(1, 99)
        attempts = 10  # Du hast jetzt 10 Versuche
        used_attempts = 0  # Zählt die tatsächlichen Versuche

        print("Du hast 10 Versuche, die richtige Zahl zwischen 1 und 99 zu erraten.")

        for attempt in range(attempts):
            used_attempts += 1
            try:
                guess = int(input(f"Versuch {attempt + 1}: Rate eine Zahl: "))

                if guess == correct_number:
                    print(f"Richtig geraten! Die Zahl war {correct_number}.")
                    break
                elif guess < correct_number:
                    print("Die gesuchte Zahl ist höher.")
                else:
                    print("Die gesuchte Zahl ist niedriger.")
            except ValueError:
                print("Bitte gib eine gültige Zahl ein.")

        # Wenn die Zahl nicht erraten wurde und alle 10 Versuche verbraucht sind
        if used_attempts == attempts:
            print(f"Du hast alle {attempts} Versuche aufgebraucht. Die richtige Zahl war {correct_number}.")

        # Statistiken basierend auf den tatsächlichen Versuchen aktualisieren
        self.track_game(used_attempts)

        # Zeige Statistiken nach jedem Spiel an
        self.show_stats()
