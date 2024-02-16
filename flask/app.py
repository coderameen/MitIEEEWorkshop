from flask import Flask,render_template,request,redirect
#initialize flask app
app = Flask(__name__)

#GET Api
@app.route("/")
def home():
    # return "Hey ALL MITians"
    return render_template("home.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/service")
def service():
    return render_template("service.html")

if __name__=="__main__":
    app.run(debug=True)