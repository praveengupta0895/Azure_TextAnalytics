import requests
from pprint import pprint
import json


subscription_key = "ec198c4f660d"
assert subscription_key

text_analytics_base_url = "https://westus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

sentiment_api_url = text_analytics_base_url
#print(sentiment_api_url)


fear = input("What is your greatest fear?")
type(fear)
happy = input("What is your happiest moment?")
type(happy)


documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': fear},
  {'id': '2', 'language': 'en', 'text': happy},
]}


headers  = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
languages = response.json()
#print(type(languages['documents']))

#data = json.dumps(languages)
#loaded_data = json.loads(data)
#loaded_data['documents']
#type(data)
#type(loaded_data)
#print(type(data))
#print(type(loaded_data))

for person in languages['documents']:
    score=(person['score'])
    score = float(score)
    score = score*100
    print(score)
