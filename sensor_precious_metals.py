import requests
import random
import time

url = 'http://localhost:5000/update'

while True:
    data = {
        "euro_to_usd": round(random.uniform(1.05, 1.15), 4),  # Курс EUR/USD
        "pound_to_usd": round(random.uniform(1.20, 1.35), 4), # Курс GBP/USD
        "usd_to_jpy": round(random.uniform(110, 115), 2)      # Курс USD/JPY
    }
    response = requests.post(url, json=data)
    print(f"Sent data: {data}, Response: {response.status_code}")
    time.sleep(5)  # Відправляємо дані кожні 5 секунд
