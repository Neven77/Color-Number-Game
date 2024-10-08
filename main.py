import random

class GuessGame:
    def __init__(self):
        # Initialisiert das Spiel
        self.colors = ['red', 'blue', 'green', 'yellow']
    
    def guess_color(self):
        # Wählt eine zufällige Farbe
        correct_color = random.choice(self.colors)
        guess = input("Rate eine Farbe (red, blue, green, yellow): ").lower()
        if guess == correct_color:
            print("Richtig geraten!")
        else:
            print(f"Falsch! Die richtige Farbe war {correct_color}.")
    
    def guess_number(self):
        # Wählt eine zufällige Zahl
        correct_number = random.randint(1, 10)
        guess = int(input("Rate eine Zahl zwischen 1 und 10: "))
        if guess == correct_number:
            print("Richtig geraten!")
        else:
            print(f"Falsch! Die richtige Zahl war {correct_number}.")

if __name__ == "__main__":
    game = GuessGame()
    
    while True:
        # Spieler wählt Spielmodus
        mode = input("Möchtest du Zahlen oder Farben raten? (number/color) oder tippe 'exit', um zu beenden: ").lower()
        
        if mode == "color":
            game.guess_color()
        elif mode == "number":
            game.guess_number()
        elif mode == "exit":
            print("Das Spiel wird beendet. Danke fürs Spielen!")
            break
        else:
            print("Ungültige Auswahl. Bitte 'number', 'color' oder 'exit' eingeben.")
