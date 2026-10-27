import time
import random
import requests

# ==========================================
# CONFIGURATION THINGSPEAK
# ==========================================
# Remplace par ton Write API Key et ton Channel ID réels
WRITE_API_KEY = 'xxxxxxxx'
CHANNEL_ID = 'xxxxxxxx'

# URL de l'API ThingSpeak pour l'écriture
url = f"https://api.thingspeak.com/update?api_key={WRITE_API_KEY}"

print("Début de la simulation et de l'envoi des données vers ThingSpeak...")
print("Appuie sur le bouton Stop (Carré) de Colab pour arrêter la boucle.\n")

# Simulation en boucle (par exemple, 10 envois, ou supprime la limite pour une boucle infinie)
for i in range(1, 100):
    # 1. Simulation de données réalistes
    temperature = round(random.uniform(20.0, 42.0), 2)  # Entre 20°C et 42°C
    humidity = round(random.uniform(15.0, 80.0), 2)     # Entre 15% et 80%
    luminosity = round(random.uniform(100.0, 950.0), 2) # Entre 100 et 950 Lux

    # 2. Préparation des paramètres pour ThingSpeak
    # field1 = Température, field2 = Humidité, field3 = Luminosité
    payload = {
        'field1': temperature,
        'field2': humidity,
        'field3': luminosity
    }

    try:
        # 3. Envoi de la requête HTTP GET vers ThingSpeak
        # response = requests.get(url, params=payload)
        response = requests.post(url, data=payload)

        # Vérification si l'envoi a réussi (le code 200 ou un ID d'entrée > 0 indique le succès)
        if response.status_code == 200 and response.text != '0':
            print(f"[Envoi #{i}] Succès -> Temp: {temperature}°C | Hum: {humidity}% | Lum: {luminosity} Lux (Entrée ID: {response.text})")
        else:
            print(f"[Envoi #{i}] Erreur ThingSpeak : {response.text}")

    except Exception as e:
        print(f"[Envoi #{i}] Erreur de connexion : {e}")

    # 4. Attente de 25 secondes avant le prochain envoi
    # (ThingSpeak bloque les requêtes espacées de moins de 15 secondes sur le compte gratuit)
    time.sleep(25)

print("\nSimulation terminée.")
