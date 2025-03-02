from flask import Flask, render_template

app = Flask(__name__)

@app.get("/")
def app():
  return render_template("base.html")