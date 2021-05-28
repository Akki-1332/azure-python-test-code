from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Akki From Azure!  <b>hello</b>  <img src='https://myimglw.blob.core.windows.net/mytest/IMG_20200309_193503-01.jpg'  width='150' height='200' /> !!"
