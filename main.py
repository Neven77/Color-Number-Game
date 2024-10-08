# main.py
from colors_game import ColorsGame
from numbers_game import NumbersGame

def show_menu():
    print("*******************************")
    print(" Willkommmen zum Ratespiel!")
    print("*******************************")
    print("1. Zahlen raten")
    print("2. Farben raten")
    print("3. Spiel beenden")
    print("*******************************")

if __name__ == "__main__":
    while True:
        # Menü anzeigen
        show_menu()

        # Benutzereingabe
        choice = input("Bitte wähle eine Option (1, 2 oder 3): ")

        if choice == "1":
            game = NumbersGame()
            game.start_game()  # Begrüssung anzeigen
            game.guess_number()
        elif choice == "2":
            game = ColorsGame()
            game.start_game()  # Begrüssung anzeigen
            game.guess_color()
        elif choice == "3":
            print("Das Spiel wird beendet. Danke fürs Spielen!")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3.")
