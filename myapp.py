from functools import partial
import requests
import json


#Code for creation

# URL="http://127.0.0.1:8000/chordcreate/"
# data={
#     'title': 'Doori',
#     'singer': 'Atif Aslam',
#     'chord': 'D'
#     }
# json_data= json.dumps(data)
# r = requests.post(url=URL, data=json_data)
# data=r.json()
# print(data)

#Code for deletion

# URL="http://127.0.0.1:8000/chorddelete/"
# data={'id':'8'}
# json_data= json.dumps(data)
# r = requests.delete(url=URL, data=json_data)
# data=r.json()
# print(data)


#Code for getting data
# def get_data(id=None):
#     data={}
#     if id is not None:
#         data={'id':id}
#     json_data=json.dumps(data)
#     r=requests.get(url=URL, data=json_data)
#     data=r.json()
#     print(data)

# get_data(1)

# Code to update data partially

# URL="http://127.0.0.1:8000/chordupdate/"
# data={'id': '3', 'title': 'Chura liya hai'}
# json_data= json.dumps(data)
# r = requests.put(url=URL, data=json_data)
# data=r.json()
# print(data)

# Code to update data fully

# URL="http://127.0.0.1:8000/chordupdate/"
# data={'id':'1',
#     'title': 'Kuch is tarah',
#     'singer': 'Atif Aslam',
#     'chord': 'F'
#     }
# json_data= json.dumps(data)
# r = requests.put(url=URL, data=json_data)
# data=r.json()
# print(data)
