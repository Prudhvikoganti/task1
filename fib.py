from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "welcome"

@app.route("/fib")
def fib():
    #return "hi how are you"
    n=int(input("enter how many numbers you want in this series"))
    first =0
    second = 1
    for i in range(n):
        print(first)
        temp  = first
        first = second
        second  = temp+second
    return f"the number is {temp}"
        
if __name__ == "__main__":
    app.run(debug=True,host="localhost",port=12000)