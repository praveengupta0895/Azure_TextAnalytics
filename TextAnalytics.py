import requests
from pprint import pprint


subscription_key = "556e2d18c72c4fc3b053c9ad0f539408"
assert subscription_key

text_analytics_base_url = "https://westus2.api.cognitive.microsoft.com/text/analytics/v2.0/"

language_api_url = text_analytics_base_url + "languages"
print(language_api_url)

documents = { 'documents': [
    { 'id': '1', 'text': 'This is a document written in English.' },
    { 'id': '2', 'text': 'Este es un document escrito en Español.' },
    { 'id': '3', 'text': '这是一个用中文写的文件' }
]}

headers  = {"Ocp-Apim-Subscription-Key": subscription_key}
response  = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)


