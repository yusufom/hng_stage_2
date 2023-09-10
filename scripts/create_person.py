import requests

base_url = 'http://127.0.0.1:8000/api'

url = base_url + '/create/'
def create_person(name):
    r = requests.post(url, {'name' : name})
    return r.text


if __name__ == '__main__':
    print(create_person('Ilebaye'))