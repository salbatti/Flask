from flask import Flask
app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my website"

@app.route('/members')
def members():
    return "Welcome to my members"

if __name__=="__main__":
    app.run(debug=True)
