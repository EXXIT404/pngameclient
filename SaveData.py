import json

auto=True

def Save(saveData):
    with open("Save.JSON", "w") as outfile:
        SaveDictioJson=json.dumps(saveData)
        outfile.write(SaveDictioJson)

def Load():
    with open("Save.JSON","r") as read_file:
        return json.load(read_file)

def Reset():
    with open("Save.JSON", "w") as outfile:
        SaveDictioJson=json.dumps([250,250])
        outfile.write(SaveDictioJson)
        