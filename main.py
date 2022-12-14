from flask import Flask, render_template , request
import os

app = Flask(__name__)




@app.route('/')
def hello_world():
   hostname = 'http://10.128.0.58:8080'
   r = requests.get(url = hostname)
   return f"{r}\nМожно сделать себе татуировку «Я ебанулся». "


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
