

import requests
import random

MAX_PERSON_ID = 82

random_id = random.randint(1,MAX_PERSON_ID)

person = requests.get(f'https://swapi.dev/api/people/{random_id}/')
person_data = person.json()
#print(person_data.get('name', f'This {random_id} is not asociate with any person'))
print('PERSON DATA', person_data)
#with open('../persistence/starwars.txt', 'a') as file:
#    for _, v in person_data.items():
#        if not isinstance(v, list):
#        file.writelines(v)

with open('../persistence/starwars.json', 'a') as json_file:
  json.dump (person_data, json_file)

