import json
import csv

flag = input("what was the flag? \n")
with open(flag+".json", 'r') as f:
  flagdict = json.load(f)

csvf = open(flag+'.csv','w')
csvwriter = csv.writer(csvf)
count = 0
for flag in flagdict:
  if count == 0:
    header = flag.keys()
    csvwriter.writerow(header)
    count += 1
  csvwriter.writerow(flag.values())

csvf.close()