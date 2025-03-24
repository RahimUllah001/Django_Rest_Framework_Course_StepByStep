import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"


#get data endpoint
def get_data(id=None):
    params = {}
    if id is not None:
        params = {'id': id}  # Use params for query parameters
    
    # Correctly use params instead of data for GET requests
    r = requests.get(url=URL, params=params)  # Pass params here
    data = r.json()
    print(data)

# get_data()  # Fetch the student with id 1
# get_data(1)  # Fetch the student with id 1

# post data endpoint
def post_data():
    data = {
        'name':'rabd',
        'roll':344,
        'city':'wazir'
    }

    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.post(url = URL, headers= headers, data = json_data)
    data = r.json()
    print(data)
# post_data()


# update data endpoint
def update_data():
    data = {
        'id':1,
        'name':'Muhammad  wazir',
        'roll':1104,
        'city':'bannu'
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.put(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
# update_data()


# delete data endpoint
def delete_data():
    data = {
        'id':1
    }
    headers = {'content-Type':'application/json'}


    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers = headers,data  = json_data)
    data = r.json()
    print(data)
delete_data()