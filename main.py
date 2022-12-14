from flask import Flask, render_template , request
import os

app = Flask(__name__)




@app.route('/')
def hello_world():
   hostname = 'dockerdude'
   response = os.system("ping -c 1 " + hostname) 
   return f"'{response}\nПодумайте что вы умный человек. "


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
