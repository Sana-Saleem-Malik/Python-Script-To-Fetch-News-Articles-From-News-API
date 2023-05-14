import requests

# your own News API key
api_key = input("API KEY: ")

# your desired search query
query = input("QUERY: ")

# your desired language (e.g. "en" for English)
language = input("LANGUAGE: ")

# your desired page size (e.g. 20)
page_size = int(input("PAGE SIZE: "))

# your desired page number (e.g. 1 for the first page)
page_number = int(input("PAGE NUMBER: "))

# your desired news source (e.g. "cnn")
# Aljazeera: "al-jazeera-english"
# CNN: "cnn"
# BBC News: "bbc-news"
# The New York Times: "the-new-york-times"
# The Washington Post: "the-washington-post"

source = input("SOURCE: ")

url = f"https://newsapi.org/v2/everything?q={query}&language={language}&sources={source}&pageSize={page_size}&page={page_number}&apiKey={api_key}"

response = requests.get(url)

articles = response.json()["articles"]

for article in articles:
    title = article["title"]
    description = article["description"]
    url = article["url"]
    source = article["source"]["name"]

    print(f"Page# {page_number}\n\nTitle: {title}\n\n Description: {description}\n\n URL: {url}\n\n Source: {source}\n")
    print("--------------------------------------")
