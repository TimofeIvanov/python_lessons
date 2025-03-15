import random
import requests
def foo ():
    URL = "https://catfact.ninja/fact"
    URL_two = "https://official-joke-api.appspot.com/random_joke"
    a = random.choice([URL, URL_two])
    print(a)
    response = requests.get(a)
    data = response.json()
    if a == URL:
        print(data["fact"])
    elif a == URL_two:
        print(data["setup"], data["punchline"], sep="\n\n\t")
foo()
