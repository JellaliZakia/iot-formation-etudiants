# !pip install paho-mqtt

import json
import random
import time
import paho.mqtt.client as mqtt

# 1. Configuration du Broker HiveMQ (ici le broker public de test)
BROKER_HOST ="broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "xxxxxxxxxxxxxxxxxxxxxxxx"

# Callback exécuté lors de la connexion
def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connecté avec succès au broker HiveMQ !")
    else:
        print(f"Échec de la connexion, code d'erreur : {rc}")

# Initialisation du client (version 2.x de paho-mqtt)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="colab_sensor_publisher")
client.on_connect = on_connect

# (Optionnel) Si vous utilisez HiveMQ Cloud sécurisé :
# client.username_pw_set("votre_utilisateur", "votre_mot_de_passe")
# client.tls_set()
# BROKER_PORT = 8883

try:
    # Connexion au broker
    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
    
    # Démarrage de la boucle réseau en arrière-plan
    client.loop_start()
    
    print(f"Publication des données sur le topic '{TOPIC}' (Appuyez sur Stop dans Colab pour arrêter)...\n")
    
    # Simulation en continu (par exemple, 10 mesures espacées de 3 secondes)
    for i in range(1, 1000):
        # Simulation de valeurs aléatoires
        temperature = round(random.uniform(20.0, 30.0), 2)  # Entre 20°C et 30°C
        humidity = round(random.uniform(40.0, 70.0), 1)     # Entre 40% et 70%
        
        # Création d'un dictionnaire de données
        payload_data = {
            "device_id": "capteur_colab_01",
            "temperature_c": temperature,
            "humidity_percent": humidity,
            "timestamp": int(time.time())
        }
        
        # Conversion du dictionnaire en chaîne JSON
        payload_json = json.dumps(payload_data)
        
        # Publication sur le topic MQTT
        result = client.publish(TOPIC, payload_json, qos=1)
        
        if result.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"[{i}] Données envoyées -> Temp: {temperature}°C | Humidité: {humidity}%")
        else:
            print(f"[{i}] Erreur d'envoi")
            
        # Attendre 3 secondes avant la prochaine simulation
        time.sleep(3)


except Exception as e:
    print(f"Une erreur est survenue : {e}")

finally:
    # Nettoyage et déconnexion propre
    client.loop_stop()
    client.disconnect()
    print("\nSimulation terminée et déconnecté du broker.")
