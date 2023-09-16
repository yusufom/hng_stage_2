import requests

base_url = 'https://person-nsnx.onrender.com/api'

def delete_person(id):
    url = base_url + f'/{id}/'
    r = requests.delete(url)
    return r.text


if __name__ == '__main__':
    print(delete_person(3))