
import json

filename="testjson.txt"
myfile=open(filename, mode='w', encoding='Latin-1')

user1 = {
    'name': "Sergo",
    'family': "Lisunkov"
}

user2 = {
    'name': "Paxa",
    'family': "Skahkov"
}

myplayers = []
myplayers.append(user1)
myplayers.append(user2)

json.dump(myplayers, myfile)
myfile.close()
