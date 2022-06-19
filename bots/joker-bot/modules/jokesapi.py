import os
import requests
import json

def get_random_joke():
    response=requests.get('https://api.chucknorris.io/jokes/random')
    json_data=json.loads(response.text)
    return(json_data['value'])

