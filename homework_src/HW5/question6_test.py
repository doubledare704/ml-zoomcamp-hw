import requests

url = "http://localhost:8001/predict"

client = {"job": "retired", "duration": 445, "poutcome": "success"}
response = requests.post(url, json=client).json()

print(response)  # {'get_card': True, 'get_card_probability': 0.902}
