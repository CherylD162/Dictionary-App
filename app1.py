#direct word translation
import json

data=json.load(open("Interactive_Dict/data.json"))

def translate(word):
    word=word.lower()
    if word not in data:
        print("Word does not exist")
    return data[word]

w=input("Enter word ")
print(translate(w))
