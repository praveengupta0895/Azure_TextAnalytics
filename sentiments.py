import requests
from pprint import pprint


subscription_key = "556e2d18c72c4fc3b053c9ad0f539406"
assert subscription_key

text_analytics_base_url = "https://westus2.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment"

sentiment_api_url = text_analytics_base_url
print(sentiment_api_url)

documents = {'documents' : [
  {'id': '1', 'language': 'en', 'text': 'I had a wonderful experience! The rooms were wonderful and the staff was helpful.'},
  {'id': '2', 'language': 'en', 'text': 'I had a terrible time at the hotel. The staff was rude and the food was awful.'},
  {'id': '3', 'language': 'es', 'text': 'Los caminos que llevan hasta Monte Rainier son espectaculares y hermosos.'},
  {'id': '4', 'language': 'es', 'text': 'La carretera estaba atascada. Había mucho tráfico el día de ayer.'}
]}


headers  = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(sentiment_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)
