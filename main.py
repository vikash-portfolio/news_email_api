import requests

api_key = "032282d428b1453baed8fde4578038dc"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2022-12-26&sortBy=publishedAt&apiKey=032282d428" \
      "b1453baed8fde4578038dc"

request = requests.get(url)
# data = request.text
# The above method returns a string. We need something more structured to access the data
data = request.json()

for article in data['articles']:
    print("Title: " + article['title'])
    print("Description: " + article['description'])

print(data)
