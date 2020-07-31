import requests
import json
class Authentication:

    uri = "http://localhost:1337"

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        data = {
            "identifier": "brian@brian.com",
            "password": "admin123"
        }
        response = requests.post(self.uri + "/auth/local", json=data)
        print(response.json()["jwt"])
        return response.json()["jwt"]