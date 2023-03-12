from flask import Flask, send_file, request
import csv
app = Flask(__name__)
header_list=['studentname','teamtype','peoplenum','description','needpeople']

def auth0(uname,pwd):
    print(uname)
    print (pwd)
    return 1

'''
with open('teams_request.csv','w',encoding='utf-8',newline='') as f:
    writer = csv.DictWriter(f, fieldnames=header_list)
    writer.writeheader()
'''

@app.route('/submitnewteam', methods=['POST'])
def submit():
    if request.method == 'POST':
        username = request.form['username']#学号
        studentname = request.form['studentname']#学生名字 HTML escaped
        password = request.form['password']#md5 hased
        teamtype=request.form['teamtype']# html escaped
        peoplenum=request.form['peoplenum']
        description=request.form['description']# html escaped
        if(auth0(username,password)):
            with open('teams_request.csv','a',encoding='utf-8',newline='') as f:
                
                writer = csv.DictWriter(f, fieldnames=header_list)
                #writer.writeheader()
                data_list={'studentname':studentname,'teamtype':teamtype,'peoplenum':peoplenum,'description':description,'needpeople':int(peoplenum)-1}
                
                writer.writerow(data_list)
                f.close()
            return '0'
        else :
            return 'invalid session'
    else:
        return 'Method not allowed'

@app.route('/')
def index():
    with open('testpost.html',encoding='utf-8',mode='r') as f:
        return f.read()
@app.route('/join')
def joinhtml():
    with open('testjoin.html',encoding='utf-8',mode='r') as f:
        return f.read()
@app.route('/jointeam',methods=['POST'])
def jointeam():
    if request.method == 'POST':
        username = request.form['username']#学号
        studentname = request.form['studentname']#学生名字 HTML escaped
        password = request.form['password']#md5 hased
        ruid=request.form['ruid']# html escaped
        with open('teams_request.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        row = int(ruid)
        column = 'needpeople'
        if(data[row][column]==0):
            return "too late"
        data[row][column] =  int(data[row][column])-1
        with open('teams_request.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header_list)
            writer.writeheader()
            writer.writerows(data)

        return 'success'
    else :
        return "method unsupported"

@app.route('/teamtable')
def teamtable():
    with open('teams_request.csv',encoding='utf-8',mode='r') as f:
        return f.read()

app.run(host='0.0.0.0', port=80)
