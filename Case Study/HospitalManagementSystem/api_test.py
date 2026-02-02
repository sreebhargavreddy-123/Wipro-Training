import requests

url = "http://127.0.0.1:5000/api/patients"

payload = {
    "name": "Ravi",
    "age": 30,
    "gender": "Male",
    "contact": "9999",
    "disease": "Flu",
    "doctor": "Dr Rao"
}

response = requests.post(url, json=payload)
print(response.status_code)
print(response.json())


bad_payload = {"age": 40}
response = requests.post(url, json=bad_payload)
print(response.status_code)   # should be 400
