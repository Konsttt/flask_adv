import requests

# # POST создание user
# resp = requests.post('http://127.0.0.1:5000/user/', json={'email': 'some9@mail.ru', 'password': '123'})
# print(resp.status_code)
# print(resp.text)

# Delete user
resp = requests.delete('http://127.0.0.1:5000/user/7/')
print(resp.status_code)
print(resp.text)

# # POST создание объявления
# resp = requests.post('http://127.0.0.1:5000/adv/', json={'title': 'Title777', 'message': 'Message message777',
#                                                          'owner': 'User7', 'owner_id': 7})
# print(resp.status_code)
# print(resp.text)
#
# # GET - все записи/объявления
# resp = requests.get('http://127.0.0.1:5000/adv/')
# print(resp.status_code)
# print(resp.text)
#
# # GET - по id объявления
# resp = requests.get('http://127.0.0.1:5000/adv/5/')
# print(resp.status_code)
# print(resp.text)
#
# # PATCH объявления
# resp = requests.patch('http://127.0.0.1:5000/adv/2/', json={'title': 'Title222', 'message': 'Message message222',
#                                                             'owner': 'User222'})
# print(resp.status_code)
# print(resp.text)
#
# # DELETE объявление
# resp = requests.delete('http://127.0.0.1:5000/adv/6/')
# print(resp.status_code)
# print(resp.text)