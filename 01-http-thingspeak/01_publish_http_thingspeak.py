import requests
import time
import random
from datetime import datetime

WRITE_API_KEY = "TON_WRITE_API_KEY"   #  Remplace ici
URL = "https://api.thingspeak.com/update"

print("Démarrage envoi vers ThingSpeak...")

for i in range(20):
    temperature = round(random.uniform(18.0, 32.0), 2)
    humidity = round(random.uniform(40.0, 85.0), 2)

    payload = {
        "api_key": WRITE_API_KEY,
        "field1": temperature,
        "field2": humidity
    }

    try:
        response = requests.get(URL, params=payload, timeout=10)
        if response.status_code == 200 and response.text != "0":
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Point {i+1}  Temp: {temperature}°C | Hum: {humidity}%")
        else:
            print(f"Erreur : {response.text}")
    except Exception as e:
        print(f"Erreur : {e}")

    if i < 19:
        time.sleep(16)

print("Terminé. Vérifie ThingSpeak.")
