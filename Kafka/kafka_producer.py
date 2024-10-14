import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

# Function to generate random player behavior data
def generate_player_data():
    player_data = {
        "player_id": random.randint(1000, 9999),
        "login_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "session_duration": random.randint(30, 3600),  # seconds
        "game_played": random.choice(["Blackjack", "Poker", "Roulette", "Slots"]),
        "win_loss": random.choice([0, 1]),  # 0 for loss, 1 for win
        "amount_bet": round(random.uniform(5, 500), 2)
    }
    return player_data

# Kafka Producer Configuration
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Ensure this matches your setup
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Send data continuously to Kafka
if __name__ == "__main__":
    while True:
        player_data = generate_player_data()
        print(f"Sending player data: {player_data}")
        producer.send('test_topic', player_data)
        time.sleep(2)  # Wait 2 seconds before sending the next message