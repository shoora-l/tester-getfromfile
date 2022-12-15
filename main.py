from flask import Flask, render_template , request
import requests
import os

app = Flask(__name__)




# @app.route('/')
# def hello_world():
#    hostname = '10.128.0.58'
#    response = os.system("ping -c 3 " + hostname) 
#    return f"{response}\n Если вам грустно – не грустите :)"


@app.route('/')
def hello_world():
   hostname = 'http://10.128.0.58'
   r = requests.get(url = hostname)
   return f"{str(r)}\n Гороскоп советует попытаться достичь половой зрелости, но не до конца. "



if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
