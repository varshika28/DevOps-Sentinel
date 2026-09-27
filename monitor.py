import requests
from datetime import datetime

url = "http://127.0.0.1:5000/health"

try:
    response = requests.get(url)
    print("Time:", datetime.now())
    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("DevOps Sentinel: Application is HEALTHY")
    else:
        print("DevOps Sentinel: Application is DOWN")

except requests.exceptions.RequestException:
    print("DevOps Sentinel: Application is DOWN")