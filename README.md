\# 📡 Formation IoT pour Étudiants



\### Monitoring de données simulées (Température \& Humidité) avec \*\*HTTP\*\* + \*\*MQTT\*\*



!\[GitHub repo size](https://img.shields.io/github/repo-size/JellaliZakia/iot-formation-etudiants)

!\[GitHub last commit](https://img.shields.io/github/last-commit/JellaliZakia/iot-formation-etudiants)

!\[License](https://img.shields.io/badge/license-MIT-blue)



\---



\## 🎯 Objectifs pédagogiques



\- Comprendre les protocoles \*\*HTTP\*\* et \*\*MQTT\*\*

\- Envoyer des données simulées (température \& humidité) vers \*\*ThingSpeak\*\*

\- Visualiser les données en temps réel

\- Appliquer de la \*\*logique floue\*\* via MATLAB Analysis

\- Utiliser un broker MQTT public (\*\*HiveMQ\*\*)

\- Stocker les données dans \*\*InfluxDB\*\*



\---



\## 🏗️ Architecture de la formation



Code Colab (Publisher)  ──HTTP──►  ThingSpeak
(Visualisation + Fuzzy Logic)Code Colab (Publisher)  ──MQTT──►  HiveMQ Broker
│
▼
Code Colab (Subscriber)
│
▼
InfluxDB




\---




\## 📁 Structure du projet



| Dossier | Description |

|---------|-------------|

| `01-http-thingspeak` | Publication des données via \*\*HTTP\*\* vers ThingSpeak |

| `02-matlab-analysis-fuzzy` | Code \*\*MATLAB Analysis\*\* (logique floue) |

| `03-mqtt-hivemq-publisher` | Publication des données via \*\*MQTT\*\* vers HiveMQ |

| `04-mqtt-subscriber-influxdb` | Abonnement MQTT + stockage dans \*\*InfluxDB\*\* |

| `docs` | Documentation complémentaire |



\---



\## ⚙️ Prérequis



\- Compte Google (pour Google Colab)

\- Compte gratuit \[ThingSpeak](https://thingspeak.com)

\- Compte gratuit \[InfluxDB Cloud](https://cloud2.influxdata.com)

\- Broker public HiveMQ : `broker.hivemq.com` (port 1883)



\---



\## 🚀 Ordre recommandé de la formation



1\. \*\*Partie 1\*\* → HTTP + ThingSpeak  

&#x20;  `01-http-thingspeak/`



2\. \*\*Partie 2\*\* → Logique floue  

&#x20;  `02-matlab-analysis-fuzzy/`



3\. \*\*Partie 3\*\* → MQTT Publisher  

&#x20;  `03-mqtt-hivemq-publisher/`



4\. \*\*Partie 4\*\* → MQTT Subscriber + InfluxDB  

&#x20;  `04-mqtt-subscriber-influxdb/`



\---



\## 👩‍💻 Auteur



Formation préparée pour les étudiants — 2025/2026  

\*\*Jellali Zakia\*\*

