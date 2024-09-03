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

@app.route('/results/<int:mark>')
def result(mark):
    
    if mark>50 :
        return "passed"
    else:
        return "failed"
   
if __name__=='__main__':
    app.run(debug=True)
