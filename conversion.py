import csv
import json

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
