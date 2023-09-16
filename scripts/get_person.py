import requests


base_url = 'https://person-nsnx.onrender.com/api'

def get_person(id):
    url = base_url + f'/{id}/'
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    print(get_person(1))