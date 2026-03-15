from flask import Flask
import database # Importujemy nasz plik z bazą danych

# Inicjalizujemy stronę internetową
app = Flask(__name__)

# To się stanie, gdy ktoś wejdzie na główny adres panelu
@app.route('/')
def strona_glowna():
    return "Witaj w KokoszkaMC! 🐔 Panel w budowie. Za chwilę dodamy tu piękny pomarańczowy wygląd!"

if __name__ == '__main__':
    # 1. Zanim włączymy stronę, upewniamy się, że baza danych istnieje
    database.inicjalizuj_baze()
    
    # 2. Uruchamiamy serwer (będzie widoczny w przeglądarce)
    print("Uruchamianie serwera KokoszkaMC...")
    app.run(debug=True, port=5000)
