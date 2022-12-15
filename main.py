from flask import Flask, render_template , request
import os

app = Flask(__name__)




@app.route('/')
def hello_world():
   hostname = '10.128.0.58'
   response = os.system("ping -c 3 " + hostname) 
   return f"{response}\n Сделайте вид, что вы – тупая лошадь, если вас заставляют работать. "


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
