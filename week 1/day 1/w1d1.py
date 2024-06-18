import pandas as pd
import requests
import json

# Specify the API endpoint URL
people = []

def get_fake_person():
    response = requests.get('https://randomuser.me/api/')
    if response.status_code == 200:
        data = response.json()
        person = {}
        person['first name'] = data['results'][0]['name']['first']
        person['last name'] = data['results'][0]['name']['last']
        person['street name'] = data['results'][0]['location']['street']['name']
        person['city'] = data['results'][0]['location']['city']
        person['state'] = data['results'][0]['location']['state']
        person['country'] = data['results'][0]['location']['country']
        person['postcode'] = data['results'][0]['location']['postcode']
        person['dob'] = data['results'][0]['dob']['date']
        person['gender'] = data['results'][0]['gender']
        person['phone'] = data['results'][0]['phone']
        person['photo'] = data['results'][0]['picture']['large']
        return person
    else:
        raise 'error'

for i in range (10):
    person = get_fake_person()
    people.append(person)

df = pd.DataFrame(people)
