import requests

r = requests.get('https://reqres.in/api/users')
data= r.json()
for data in datas:
    for key, value in data.items():
        print(key, value)
    print("\n")
