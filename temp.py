
import json
import csv

row1=list()
with open('C:\\Users\\Shubham Mittal\\Desktop\\Book1.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row,idx in enumerate(reader):
        if row != 0:
          row1.append(idx)  
            
print(json.dumps(row1))
print("Done")     