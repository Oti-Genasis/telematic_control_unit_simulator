import socket
import json
import time
import random

# Configuration du serveur TCP/IP
SERVER_HOST = '127.0.0.1'  # Adresse IP du serveur
SERVER_PORT = 65432        # Port d'écoute du serveur

update_timeout = 0.5

# Fonction pour générer des données de géolocalisation aléatoires
def generate_random_location_data():
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return {
        "latitude": latitude,
        "longitude": longitude,
        "timestamp": timestamp
    }

# Fonction pour simuler l'envoi de données de géolocalisation
def send_location_data():
    # Crée un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Établit la connexion avec le serveur
        client_socket.connect((SERVER_HOST, SERVER_PORT))
        # Simule l'envoi de données de géolocalisation
        while True:
            # Génère des données de géolocalisation aléatoires
            location_data = generate_random_location_data()
            # Convertit les données en format JSON
            json_data = json.dumps(location_data)
            # Envoie les données au serveur
            client_socket.sendall(json_data.encode('utf-8'))
            print("Données de géolocalisation envoyées :", location_data)
            # Attend un certain intervalle de temps avant d'envoyer les prochaines données
            time.sleep(update_timeout)

if __name__ == '__main__':
    send_location_data()
