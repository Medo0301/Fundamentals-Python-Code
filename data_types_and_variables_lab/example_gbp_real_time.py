import requests
import time

gbp = f"https://open.er-api.com/v6/latest/GBP"

while True:
    try:
        print(requests.get(gbp, timeout=6).json()['rates']['USD'])
    except Exception as e:
        print("Error!", e)
    time.sleep(5)