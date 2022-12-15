from flask import Flask, render_template , request
import requests


app = Flask(__name__)




@app.route('/')
def hello_world():
   hostname = 'http://10.2.0.2/'
   r = requests.get(url = hostname)
   return f"{str(r)}\n Может показаться, что все люди вокруг — это псы. И они действительно псы"



if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
