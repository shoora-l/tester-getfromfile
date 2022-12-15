from flask import Flask, render_template , request
import requests
import os

app = Flask(__name__)




@app.route('/')
def hello_world():
   hostname = 'http://10.128.0.58'
   r = requests.get(url = hostname)
   return f"{str(r)}\n Судьба даст вам ответ на самый главный вопрос человечества: кто такой Валерий Яковлевич Пузанков и каковы его планы? "



if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
