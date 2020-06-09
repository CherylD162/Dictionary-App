#direct word translation
import json

data=json.load(open("Interactive_Dict/data.json"))

def translate(word):
    return data[word]

w=input("Enter word ")
print(translate(w))