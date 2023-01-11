from flask import Flask, render_template , request
import os

app = Flask(__name__)




@app.route('/')
def hello_world():
   with open(os.environ['THINGSOURCE'],'r') as f:
      data = f.read()
   return render_template('output.html', thing = data)



if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8081')
