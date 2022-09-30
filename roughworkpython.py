from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")                                              #Defines how we access this page. Flask doesn't know where we should be going to get to this page. / means that wherever our domain is, when we use this it will automatically send us to this page
def home():
    return render_template("index.html", major_keys=["C major", "C# major", "D major", "D# major", "E major", "F major", "F# major", "G major", "G# major", "A major", "A# major", "B major"] , minor_keys=["C minor", "C# minor", "D minor", "D# minor", "E minor", "F minor", "F# minor", "G minor", "G# minor", "A minor", "A# minor", "B minor"])

######################################################################################################
"""
@app.route("/<name>") #Putting somthing in between tags grabs that value and passes it to the function as a parameter
def user(name):
    return f"Hello {name}!"

@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="Admin!"))      #When typing url/admin you get redirected to the user page but now with the name 'admin'
"""
######################################################################################################
if __name__ == "__main__":
    app.run(debug=True)