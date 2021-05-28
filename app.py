from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Akki From Azure!  <b>hello !!</b>  <img src='https://myimagest.blob.core.windows.net/myclwimage/vimal.jpg'  width='150' height='200' />"
