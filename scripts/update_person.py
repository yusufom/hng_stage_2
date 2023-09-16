import requests

base_url = 'https://person-nsnx.onrender.com/api'

def update_person(id, new_name):
    url = base_url + f'/{id}/'
    r = requests.put(url, {'name' : new_name})
    return r.text


if __name__ == '__main__':
    print(update_person(3, 'Doyin'))