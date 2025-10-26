import requests
url = "https://opentdb.com/api.php?amount=5&type=multiple"

respone = requests.get(url)

if respone.status_code == 200:
    triviadata = respone.json()
    score = 0

    print(triviadata["results"][0]["question"])
    print(triviadata["results"][0]["correct_answer"])
    print(triviadata["results"][0]["incorrectw_answers"])