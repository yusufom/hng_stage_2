import requests

url = 'https://person-nsnx.onrender.com/api'

def create_person(name):
    r = requests.post(url, {'name' : name})
    return r.text


if __name__ == '__main__':
    print(create_person('Ilebaye'))