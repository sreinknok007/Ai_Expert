import requests
from requests import api

API_KEY = "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"

api_url = "https://api-inference.huggingface.co/models/nlptown/bert-base-multilingual-uncased-sentiment"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

text = "I think Dollar will lose shinr"

response = requests.post(api_url,headers=headers,json={'inputs':text})

if response.status_code == 200:
    
    classification = response.json()

# print(classification)

    print("Predicted label:", classification[0][0]['label'])

    print("Confidence:", classification[0][0]['score'])

else:

 print(f"Error: {response.status_code}")