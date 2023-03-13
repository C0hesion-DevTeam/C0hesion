from flask import Flask, send_file, request
import csv
app = Flask(__name__)
header_list=['ruid','studentname','teamtype','peoplenum','description','needpeople']
import os
def auth0(uname,pwd):
    #到时候需要真的验证
    return 1


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
            with open('ruid.txt','r',encoding='utf-8') as f:
                nowid=int(f.read())
            with open('ruid.txt','w',encoding='utf-8',newline='') as f:
                f.write(str(nowid+1))
            with open('teams_request.csv','a',encoding='utf-8',newline='') as f:
                
                writer = csv.DictWriter(f, fieldnames=header_list)
                #writer.writeheader()
                data_list={'ruid':nowid,'studentname':studentname,'teamtype':teamtype,'peoplenum':peoplenum,'description':description,'needpeople':int(peoplenum)-1}
                
                writer.writerow(data_list)
                f.close()
            
                filename = 'team\\'+str(nowid)+'.txt'
                with open(filename, 'w', encoding='utf-8', newline='') as f:
                    f.write(username)
                

                filename = 'stuc\\'+username+'.txt'

                if not os.path.exists(filename):
                    with open(filename, 'w+', encoding='utf-8', newline='') as f:
                        f.write(str(nowid))
                else:
                  with open(filename, 'a', encoding='utf-8', newline='') as f:
                   f.write(','+str(nowid))

            return '0'
        else :
            return 'invalid session'
    else:
        return 'Method not allowed'

@app.route('/')
def index():
    with open('testpost.html',encoding='utf-8',mode='r') as f:
        return f.read()
@app.route('/jointest')
def joinhtml():
    with open('testjoin.html',encoding='utf-8',mode='r') as f:
        return f.read()
@app.route('/jointeam',methods=['POST'])
def jointeam():
    if request.method == 'POST':
        username = request.form['username']#学号
        studentname = request.form['studentname']#学生名字 HTML escaped
        password = request.form['password']#md5 hased
        tarruid=int(request.form['ruid'])
        if(not auth0(username,password)):
            return "invalid session"
        with open('team//'+str(tarruid)+'.txt', 'r', newline='') as file:
            curuser=file.read()
            if username in curuser:
                return('you are already in the team')
        with open('teams_request.csv', 'r') as file:
            reader = csv.DictReader(file)
            data = list(reader)
        with open('ruid.txt','r',encoding='utf-8') as f:
                nowid=int(f.read())
        l=0
        r=nowid
        while(r>=l):
            mid=int((l+r)/2)
            if int(data[mid]['ruid'])<tarruid:
                l=mid+1
            if int(data[mid]['ruid'])>tarruid:
                r=mid-1
            if int(data[mid]['ruid'])==tarruid:
                break

        row=mid
        column = 'needpeople'
        
        if(data[row][column]=='0'):
            return "too late"
        data[row][column] =  int(data[row][column])-1
        with open('teams_request.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=header_list)
            writer.writeheader()
            writer.writerows(data)
        with open('team//'+str(tarruid)+'.txt', 'a', newline='') as file:
            file.write(','+username)






        filename = 'stuj\\'+username+'.txt'
        if(1):
                if not os.path.exists(filename):
                    with open(filename, 'w+', encoding='utf-8', newline='') as f:
                        f.write(str(tarruid))
                else:
                  with open(filename, 'a', encoding='utf-8', newline='') as f:
                   f.write(','+str(tarruid))





                   
        return 'success'
    else :
        return "method unsupported"

@app.route('/teamtable')
def teamtable():
    with open('teams_request.csv',encoding='utf-8',mode='r') as f:
        return f.read()


@app.route('/viewteam')
def viewteam():
    with open('team\\'+request.args["ruid"]+'.txt',encoding='utf-8',mode='r') as f:
        return f.read()

@app.route('/viewstuc')
def viewstuc():
    if(auth0(request.args["un"],request.args["pwd"])):#pwd is md5 hashed
     with open('stuc\\'+request.args["un"]+'.txt',encoding='utf-8',mode='r') as f:
        return f.read()
    else :
        return ('invalid session')

@app.route('/viewstuj')
def viewstuj():
    if(auth0(request.args["un"],request.args["pwd"])):#pwd is md5 hashed
     with open('stuj\\'+request.args["un"]+'.txt',encoding='utf-8',mode='r') as f:
        return f.read()
    else :
        return ('invalid session')
@app.errorhandler(404)
def page_not_found(error):
    return "404: Page not found. Maybe try checking under the couch cushions?", 404

app.run(host='0.0.0.0', port=80)
