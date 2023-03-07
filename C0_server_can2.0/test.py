import html
import csv
print(html.escape('1一'))
with open('teams_request.csv','r',encoding='utf-8')as fp:
    reader = csv.DictReader(fp)
    for i in reader:
        print(html.unescape(i['studentname']))
