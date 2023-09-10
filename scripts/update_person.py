import requests

base_url = 'http://127.0.0.1:8000/api'

def update_person(prev_name, new_name):
    url = base_url + f'/update/{prev_name}/'
    r = requests.put(url, {'name' : new_name})
    return r.text


if __name__ == '__main__':
    print(update_person('Ilebaye', 'Doyin'))