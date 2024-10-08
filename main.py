# main.py
from colors_game import ColorsGame
from numbers_game import NumbersGame

if __name__ == "__main__":
    while True:
        game_type = input("Möchtest du Zahlen oder Farben raten? (number/color) oder tippe 'exit', um zu beenden: ").lower()
        
        if game_type == "color":
            game = ColorsGame()
            game.guess_color()
        elif game_type == "number":
            game = NumbersGame()
            game.guess_number()
        elif game_type == "exit":
            print("Das Spiel wird beendet. Danke fürs Spielen!")
            break
        else:
            print("Ungültige Auswahl. Bitte 'number', 'color' oder 'exit' eingeben.")
