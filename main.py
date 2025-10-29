import requests

def grf():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    responce = requests.get(url)
    if responce.status_code == 200:
        d = responce.json()
        print("Not Funny Facts")
        print(d["text"])
    else:
        print("Not Working Slow internet")
grf()