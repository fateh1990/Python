from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello welcome to the flask"


app.run(host="0.0.0.0")
    