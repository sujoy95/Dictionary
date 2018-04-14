import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn =="Y" or yn =="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn =="N" or yn =="n":
            return "The word doesn't exist."
        else:
            return "Invalid entry"
    else:
        return "The word doesn't exist.Please double check it."

word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
