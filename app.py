from flask import Flask, render_template
import database

app = Flask(__name__)

# Gdy ktoś wejdzie na główną stronę, pokaż nasz nowy pomarańczowy panel!
@app.route('/')
def strona_glowna():
    return render_template('panel.html')

if __name__ == '__main__':
    database.inicjalizuj_baze()
    print("Uruchamianie serwera KokoszkaMC...")
    app.run(debug=True, port=5000)
