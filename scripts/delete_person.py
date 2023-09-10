import requests

base_url = 'https://person-nsnx.onrender.com/api'

def delete_person(name):
    url = base_url + f'/{name}/'
    r = requests.delete(url)
    return r.text


if __name__ == '__main__':
    print(delete_person('Doyin'))