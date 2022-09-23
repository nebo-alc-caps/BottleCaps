import json
Filepath = r'F:\ALCBottleCaps\BottleCaps\src\square\Options.json'

with open(Filepath,'r',encoding="utf-8") as rf:
    test1 = json.loads(rf.read())
#     Loops through Sizes(Json) object and prints the values stored
    for i in test1["Sizes"]:
        print(test1["Sizes"][i])
