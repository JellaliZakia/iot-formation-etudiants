import paho.mqtt.client as mqtt
import json
import random
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from datetime import datetime

BROKER = "broker.hivemq.com"
PORT = 1883
TOPIC = "formation/iot/etudiants/temperature_humidity"
CLIENT_ID = f"subscriber-{random.randint(1000,9999)}"

INFLUX_URL    = "https://eu-central-1-1.aws.cloud2.influxdata.com"
INFLUX_TOKEN  = "TON_TOKEN"
INFLUX_ORG    = "TON_ORG"
INFLUX_BUCKET = "iot_formation"

influx_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = influx_client.write_api(write_options=SYNCHRONOUS)

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("Connecté à HiveMQ")
        client.subscribe(TOPIC, qos=1)
    else:
        print(f"Erreur : {rc}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print(f"Reçu  {data}")

        point = (Point("sensor_data")
            .tag("source", data.get("sensor", "unknown"))
            .field("temperature", float(data["temperature"]))
            .field("humidity", float(data["humidity"])))

        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        print(" Écrit dans InfluxDB")
    except Exception as e:
        print(f"Erreur : {e}")

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id=CLIENT_ID)
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

print("En attente de messages...")
client.loop_forever()
