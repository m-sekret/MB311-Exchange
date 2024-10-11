import requests
import random
import time

url = 'http://localhost:5000/update'

def generate_currency_data():
    data = {
        "Gold": round(random.uniform(1800, 2000), 2),
        "Platinum": round(random.uniform(800, 1000), 2),
        "Silver": round(random.uniform(20, 30), 2)
    }
    return data

while True:
    data = generate_currency_data()
    response = requests.post(url, json=data)
    print(f"Sent data: {data}, Response: {response.status_code}")
    time.sleep(5)
