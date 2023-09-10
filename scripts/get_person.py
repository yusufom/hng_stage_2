import requests


url = 'https://person-nsnx.onrender.com/api/'

def get_person(name):
    r = requests.get(url, data={'name': name})
    return r.text


if __name__ == '__main__':
    print(get_person('Ilebaye'))