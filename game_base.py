# game_base.py
class GameBase:
    def __init__(self):
        self.total_games = 0  # Zählt die Gesamtzahl der gespielten Spiele
        self.total_attempts = 0  # Zählt die Gesamtzahl der Versuche
    
    def start_game(self):
        print("Willkommen zum Spiel!")
    
    def track_game(self, attempts):
        # Spiel- und Versuchsstatistiken aktualisieren
        self.total_games += 1
        self.total_attempts += attempts
    
    def show_stats(self):
        # Zeigt die Durchschnittswerte der gespielten Spiele an
        if self.total_games > 0:
            average_attempts = self.total_attempts / self.total_games
            print(f"Du hast bisher {self.total_games} Spiel(e) gespielt.")
            print(f"Durchschnittliche Anzahl von Versuchen pro Spiel: {average_attempts:.2f}")
        else:
            print("Es wurden noch keine Spiele gespielt.")
