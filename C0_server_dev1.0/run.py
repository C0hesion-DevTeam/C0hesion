from flask import Flask,send_file, request
app = Flask(__name__)
@app.route('/novelexplorer')
def index1():
	    with open('_index.html',encoding='utf-8',mode='r') as f:
       		 return f.read()


@app.route('/')
def index():
	    with open('shining-text-animation-effects/dist/index.html',encoding='utf-8',mode='r') as f:
       		 return f.read()
@app.route('/image2.jpg')
def image2():
    filename = 'image2.jpg'  # specify the path to your image file
    return send_file(filename, mimetype='image/jpg')

@app.route('/paperline.jpg')
def paperline():
    filename = 'paperline.jpg'  # specify the path to your image file
    return send_file(filename, mimetype='image/jpg')

@app.route('/AaYangGuanQu-2.ttf')
def AaYangGuanQu():
    filename = 'AaYangGuanQu-2.ttf'  # specify the path to your image file
    return send_file(filename)








app.run(host='0.0.0.0', port=80)
