import json
import time
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# ==========================================
# CONFIGURATION INFLUXDB CLOUD (À MODIFIER)
# ==========================================
INFLUX_URL = "https://us-east-1-1.aws.cloud2.influxdata.com" # Votre URL Cloud
INFLUX_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"    # Votre Token d'accès
INFLUX_ORG = "IoT"                              # Votre Organization
INFLUX_BUCKET = "mon_bucket_iot"                               # Votre Bucket

# Connexion à InfluxDB Cloud
try:
    influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
    write_api = influx_client.write_api(write_options=SYNCHRONOUS)
    print("Connecté à InfluxDB Cloud avec succès !")
except Exception as e:
    print(f"Erreur de connexion à InfluxDB : {e}")

# ==========================================
# CONFIGURATION HIVEMQ (MQTT)
# ==========================================
BROKER_HOST = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC = "formation/IoT/fst"

# Fonction appelée automatiquement à chaque réception de message MQTT
def on_message(client, userdata, msg):
    try:
        # Décoder le message JSON reçu
        payload_str = msg.payload.decode('utf-8')
        payload = json.loads(payload_str)
        print(f"\n[MQTT Reçu] Topic: {msg.topic} -> Données : {payload}")
        
        # Extraire les données (en s'adaptant à la structure envoyée par votre Publisher)
        device_id = payload.get("device_id", "inconnu")
        temperature = float(payload.get("temperature_c", 0.0))
        humidity = float(payload.get("humidity_percent", 0.0))
        
        # Préparer le point pour InfluxDB
        point = Point("environnement") \
            .tag("device_id", device_id) \
            .field("temperature", temperature) \
            .field("humidite", humidity)
            
        # Envoyer dans InfluxDB Cloud
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        print("-> [InfluxDB] Données enregistrées dans le cloud avec succès !")
        
    except Exception as e:
        print(f"Erreur lors du traitement du message : {e}")

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print(f"Connecté au broker MQTT {BROKER_HOST} !")
        client.subscribe(TOPIC)
        print(f"Abonné au topic : {TOPIC}")
    else:
        print(f"Échec de connexion MQTT, code : {rc}")

# Initialisation du client MQTT (version 2.x de paho-mqtt)
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="colab_influx_bridge")
client.on_connect = on_connect
client.on_message = on_message

try:
    # Connexion au broker
    client.connect(BROKER_HOST, BROKER_PORT, keepalive=60)
    
    # Démarrage de la boucle en arrière-plan
    client.loop_start()
    
    print("\n--- Passerelle active ---")
    print("La cellule va écouter les messages pendant 30 minutes (ou cliquez sur Stop pour arrêter).")
    
    # Laisse tourner la passerelle pendant 3 minutes (180 secondes) sur Colab
    time.sleep(1800)  # 1800 secondes = 30 minutes

except Exception as e:
    print(f"Une erreur est survenue : {e}")

finally:
    # Nettoyage et déconnexion propre
    client.loop_stop()
    client.disconnect()
    influx_client.close()
    print("\nPasserelle arrêtée et déconnectée.")
