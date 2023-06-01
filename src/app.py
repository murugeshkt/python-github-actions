from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    os.system('dir')
    return "Hello World!"

if __name__ == "__main__":
    app.run()
