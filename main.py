from flask import Flask, render_template , request


app = Flask(__name__)




@app.route('/')
def hello_world():
   # hostname = 'http://10.2.0.2/'
   # r = requests.get(url = hostname)
   return f"Чтобы защитить психику, вы должны стать умственно отсталым"



if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8080')
