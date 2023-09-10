import requests

base_url = 'http://127.0.0.1:8000/api'

def delete_person(name):
    url = base_url + f'/delete/{name}/'
    r = requests.delete(url)
    return r.text


if __name__ == '__main__':
    print(delete_person('Doyin'))