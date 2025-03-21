import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}  # Use params for query parameters
    
    # Correctly use params instead of data for GET requests
    r = requests.get(url=URL, params=params)  # Pass params here
    data = r.json()
    print(data)

# get_data()  # Fetch the student with id 1


def post_data():
    data = {
        'name':'abd',
        'roll':104,
        'city':'Dhaband'

    json_data = json.dumps(data)
    r = requests.post(url = URL, data   = json_data)
    data = r.json()
    print(data)
# post_data()

def update_data():
    data = {
        'id':2 ,
        'name':'Muhammad  wazir',
        'roll':1104,
        'city':'bannu'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL, data  = json_data)
    data = r.json()
    print(data)
# update_data()

def delete_data():
    data = {
        'id':3 
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL, data  = json_data)
    data = r.json()
    print(data)
# delete_data()