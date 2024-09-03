from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my channel"

@app.route('/pass/<int:mark>')
def success(mark):
    return "You are passed"+str(mark)

@app.route('/fail/<int:mark>')
def fail(mark):
    return "You are failed"+str(mark)
if __name__=='__main__':
    app.run(debug=True)
