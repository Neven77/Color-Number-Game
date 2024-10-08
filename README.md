# Color and Number Guessing Game

Dieses Projekt besteht aus einem einfachen Spiel, bei dem der Benutzer entweder Farben oder Zahlen raten kann. Das Projekt zeigt den Einsatz von objektorientierter Programmierung (OOP) und Vererbung in Python.

## Projektstruktur

- **game_base.py**: Enthält die Basisklasse `GameBase`, von der sowohl das Farben- als auch das Zahlenraten-Spiel erben.
- **colors_game.py**: Enthält die Logik für das Farbenraten. Diese Klasse erbt von `GameBase`.
- **numbers_game.py**: Enthält die Logik für das Zahlenraten. Diese Klasse erbt ebenfalls von `GameBase`.
- **main.py**: Die Hauptdatei, die das Spiel startet. Der Benutzer kann zwischen dem Farbenraten und dem Zahlenraten wählen.

## Spielanleitung

1. Beim Start des Programms wird der Benutzer gefragt, ob er Zahlen oder Farben raten möchte.
2. Der Benutzer kann `number` eingeben, um eine Zahl zwischen 1 und 10 zu raten, oder `color`, um eine Farbe zu raten (rot, blau, grün oder gelb).
3. Nach jedem Spiel hat der Benutzer die Möglichkeit, das Spiel zu wiederholen oder es zu beenden, indem er `exit` eingibt.

## Anforderungen

Um das Spiel auszuführen, müssen die folgenden Python-Pakete installiert sein:

- Python Standardbibliotheken (wie `random`)

Es ist keine zusätzliche Installation von Paketen notwendig. Stelle jedoch sicher, dass du ein virtuelles Environment verwendest, um deine Umgebung zu isolieren.

## Installation

1. Klone das Repository:
   ```bash
   git clone https://github.com/dein-username/Color-Number-Game.git