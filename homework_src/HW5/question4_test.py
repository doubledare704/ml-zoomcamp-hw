import requests

url = "http://127.0.0.1:8000/predict"

client = {"job": "unknown", "duration": 270, "poutcome": "failure"}
response = requests.post(url, json=client).json()

print(response) # {'get_card': False, 'get_card_probability': 0.14}
