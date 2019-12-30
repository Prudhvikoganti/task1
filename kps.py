from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return f"i am on port 12000"

@app.route("/hello")
def hello():
    return f"hello i am on port 12000"


if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=12000)
    