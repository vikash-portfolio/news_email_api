import requests

api_key = "032282d428b1453baed8fde4578038dc"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2022-12-26&sortBy=publishedAt&apiKey=032282d428" \
      "b1453baed8fde4578038dc"

request = requests.get(url)
data = request.json()

print(type(data))