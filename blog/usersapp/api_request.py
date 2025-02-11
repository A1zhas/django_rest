import requests
import pprint


# response = requests.get('http://127.0.0.1:8000/api/v0/tags/', auth=('login', 'password'))

# pprint.pprint(response.json())


token = '7ad77f64df24030403c3ad8795c79ee02fa5cc49'
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v0/tags/', headers=headers)
# response = requests.get('http://127.0.0.1:8000/api/v0/tags/')
pprint.pprint(response.json())