import csv
import json

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
class Cata:
    def __init__(self,base,modifier):
