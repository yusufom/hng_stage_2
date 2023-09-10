import requests


base_url = 'https://person-nsnx.onrender.com/api'

def get_person(name):
    url = base_url + f'?name={name}'
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    print(get_person('Ilebaye'))