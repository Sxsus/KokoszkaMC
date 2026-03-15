import sqlite3

def inicjalizuj_baze():
    # Tworzymy połączenie z plikiem bazy danych
    polaczenie = sqlite3.connect('kokoszka.db')
    kursor = polaczenie.cursor()

    # Tabela 1: Rejestracja i logowanie (Konta)
    kursor.execute('''
        CREATE TABLE IF NOT EXISTS uzytkownicy (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazwa_konta TEXT UNIQUE NOT NULL,
            haslo TEXT NOT NULL
        )
    ''')

    # Tabela 2: Ustawienia serwerów graczy (Silnik, port, nazwa)
    kursor.execute('''
        CREATE TABLE IF NOT EXISTS serwery (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            wlasciciel_id INTEGER NOT NULL,
            nazwa_serwera TEXT UNIQUE NOT NULL,
            silnik TEXT DEFAULT 'vanilla',
            wersja TEXT DEFAULT '1.20.4',
            port INTEGER UNIQUE NOT NULL,
            FOREIGN KEY (wlasciciel_id) REFERENCES uzytkownicy (id)
        )
    ''')

    polaczenie.commit()
    polaczenie.close()
    print("Sukces! Baza danych kokoszka.db jest gotowa do działania.")

# Ta linijka pozwala nam przetestować plik
if __name__ == '__main__':
    inicjalizuj_baze()
