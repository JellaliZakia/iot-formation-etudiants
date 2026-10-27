import paho.mqtt.client as mqtt
import time
import random
import json
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "formation/iot/etudiants/temperature_humidity"  #  Change ce topic
CLIENT_ID = f"publisher-{random.randint(1000,9999)}"

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connecté à HiveMQ !")
    else:
        print(f"Erreur connexion : {rc}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
client.on_connect = on_connect
client.connect(BROKER, PORT, 60)
client.loop_start()

print(f"Publication sur : {TOPIC}")

try:
    for i in range(30):
        temperature = round(random.uniform(18.0, 32.0), 2)
        humidity = round(random.uniform(40.0, 85.0), 2)

        payload = {
            "temperature": temperature,
            "humidity": humidity,
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "sensor": "simulation"
        }

        client.publish(TOPIC, json.dumps(payload), qos=1)
        print(f"[{datetime.now().strftime('%H:%M:%S')}]  Temp: {temperature}°C | Hum: {humidity}%")
        time.sleep(5)
except KeyboardInterrupt:
    print("Arrêt")

client.loop_stop()
client.disconnect()
