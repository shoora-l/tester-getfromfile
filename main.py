from flask import Flask, render_template , request

app = Flask(__name__)




@app.route('/')
def hello_world():
   return "Вечер звезды советуют провести в компании симпатичных крыс."


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
