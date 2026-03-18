import requests



query = input("what type of news  you want to read :")
api= "41f1eace068845f78ec2bd97e7e3bc1c"

url = "https://newsapi.org/v2/everything?q=tesla&from=2026-01-16&sortBy=publishedAt&apiKey=41f1eace068845f78ec2bd97e7e3bc1c"
print(url)
r  =  requests.get(url)

data = r.json()

articles = data["articles"]
for index ,  article in  enumerate(articles):
    print(index+1,article["title"],article["url"])
    print("\n****************************************************\n")
    