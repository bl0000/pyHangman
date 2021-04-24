import json

def creator():
    data = []
    name = input("Type the name you want the wordlist to be called (without a file extension)\n")
    print('Type "CANCEL" at any time to stop the loop. ')
    while True:
        inp = input("Enter word: ")
        if inp == "CANCEL":
            break
        data.append(inp)
    name = name + ".json"
    with open(name, "w") as f:
        json.dump(data, f)
    return name

