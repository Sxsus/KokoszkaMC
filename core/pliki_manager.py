import os

# Funkcja tworząca bezpieczny folder dla nowego gracza
def stworz_folder_serwera(nazwa_serwera):
    sciezka = f"./serwery_dane/{nazwa_serwera}"
    if not os.path.exists(sciezka):
        os.makedirs(sciezka)
        print(f"[Pliki Manager] Utworzono nowy folder: {sciezka}")
        
        # Minecraft wymaga akceptacji pliku EULA, więc robimy to automatycznie!
        with open(f"{sciezka}/eula.txt", "w") as plik:
            plik.write("eula=true")
    else:
        print("[Pliki Manager] Taki serwer już istnieje!")