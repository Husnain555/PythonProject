import csv

with open('/Users/talk2/Downloads/fake_gmail.csv','r') as f:
  cs_requality = csv.reader(f)
  for row in cs_requality:
        print(row)