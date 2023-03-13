import requests

# POST создание user
resp = requests.post('http://127.0.0.1:5000/user/', json={'email': 'some10@mail.ru', 'password': '123456789'})
print(resp.status_code)
print(resp.text)

# POST создание объявления1
resp = requests.post('http://127.0.0.1:5000/adv/', json={'title': 'Title1', 'message': 'Message message1',
                                                         'owner': 'User1', 'owner_id': 10})
print(resp.status_code)
print(resp.text)

# POST создание объявления2
resp = requests.post('http://127.0.0.1:5000/adv/', json={'title': 'Title2', 'message': 'Message message2',
                                                         'owner': 'User1', 'owner_id': 10})
print(resp.status_code)
print(resp.text)

# GET - все записи/объявления
resp = requests.get('http://127.0.0.1:5000/adv/')
print(resp.status_code)
print(resp.text)

# GET - по id объявления
resp = requests.get('http://127.0.0.1:5000/adv/1/')
print(resp.status_code)
print(resp.text)

# PATCH объявления
resp = requests.patch('http://127.0.0.1:5000/adv/2/', json={'title': 'Title222', 'message': 'Message message222',
                                                            'owner': 'User1'})
print(resp.status_code)
print(resp.text)

# DELETE объявление
resp = requests.delete('http://127.0.0.1:5000/adv/1/')
print(resp.status_code)
print(resp.text)

# POST создание объявления3
resp = requests.post('http://127.0.0.1:5000/adv/', json={'title': 'Title3', 'message': 'Message message3',
                                                         'owner': 'User1', 'owner_id': 10})
print(resp.status_code)
print(resp.text)

# Delete user
resp = requests.delete('http://127.0.0.1:5000/user/10/')
print(resp.status_code)
print(resp.text)