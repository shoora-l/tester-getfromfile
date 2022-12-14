from flask import Flask, render_template , request

app = Flask(__name__)




@app.route('/')
def hello_world():
   return "Помните, что все окружающие вас люди обладают психическим расстройством."


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
