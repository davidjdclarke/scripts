import requests


def get():
    r = requests.get('http://127.0.0.1:8000/')
    # print(r.text)

def post():
    pload = {'username': 'davidjc', 'password': '12345678'}
    r = requests.post('http://127.0.0.1:8000/', data=pload)
    print(r)


if __name__ == "__main__":
    get()
    post()
