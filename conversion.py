import csv
import json
# eight catagories in the classes
with open("file.json","r")as fileName:
    fls=fileName.read()
    
#syrup, puree, fruit,other, freeze is a list


# things the classes need

#    ITEM, ITEM_VARIATION, MODIFIER, MODIFIER_LIST, CATEGORY, DISCOUNT, TAX, IMAGE, QUANTITY 


#modifiers is a list 
class Cata:
    def __init__(self,base,modifier):
        self.base=base
        self.modifier=modifier


        #converter
csvfile = open('file.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ()
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')
with open('file.json', 'r') as fs:
    line=fs.readlines()
    print(line)
    
    
