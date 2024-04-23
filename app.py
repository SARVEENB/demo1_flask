from flask import Flask , render_template #this a flask package

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/s1/api/signup')
def user_signup():
    return "sighup here"

@app.route('/s1/api/login')
def user_login():
    return "login here"

@app.route('/s1/api/blog')
def blog():
    return "write a content here"

@app.route('/s1/api/about')
def about():
    return "about us"

@app.route('/s1/api/contact')
def contact():
    return " contact us"



if __name__=="__main__":
    app.run(debug=True)