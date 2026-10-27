# Formation IoT pour Étudiants

Monitoring de données simulées (Température & Humidité) avec HTTP + MQTT

## Objectifs pédagogiques

- Comprendre les protocoles HTTP et MQTT
- Envoyer des données simulées vers ThingSpeak
- Visualiser les données en temps réel
- Appliquer de la logique floue via MATLAB Analysis
- Utiliser un broker MQTT public (HiveMQ)
- Stocker les données dans InfluxDB

## Structure du projet

| Dossier | Contenu |
|---------|---------|
| 01-http-thingspeak | Publication HTTP vers ThingSpeak |
| 02-matlab-analysis-fuzzy | Logique floue (MATLAB Analysis) |
| 03-mqtt-hivemq-publisher | Publication MQTT vers HiveMQ |
| 04-mqtt-subscriber-influxdb | Abonnement MQTT + InfluxDB |
| docs | Documentation |

## Prérequis

- Compte Google (Colab)
- Compte ThingSpeak (gratuit)
- Compte InfluxDB Cloud (gratuit)
- Broker HiveMQ : broker.hivemq.com (port 1883)

## Ordre de la formation

1. Partie 1  HTTP + ThingSpeak
2. Partie 2  Logique floue
3. Partie 3  MQTT Publisher
4. Partie 4  MQTT Subscriber + InfluxDB
