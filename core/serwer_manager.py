import psutil

# Ta funkcja w przyszłości uruchomi plik .jar w tle (24/7)
def uruchom_serwer(nazwa_serwera, port):
    print(f"[Serwer Manager] Uruchamianie serwera {nazwa_serwera} na porcie {port}...")
    # Tutaj dodamy komendę 'java -jar server.jar'
    return True

# Ta funkcja sprawdza zużycie pamięci RAM Twojego komputera
def sprawdz_ram():
    zuzycie = psutil.virtual_memory().percent
    return zuzycie