import requests
response = requests.get("http://api.open-notify.org/astros.json")  
json = response.json()  

print ('There are', json['number'], 'people in space right now:')

for person in json['people']:
    print(person['name'], 'is on the', person['craft'])
