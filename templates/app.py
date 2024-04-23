from flask import Flask #this a flask package

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to azure and flask web app"

@app.route('/s1/api/signup')
def user_signup():
    return "sighup here"



if __name__=="__main__":
    app.run(debug=True)