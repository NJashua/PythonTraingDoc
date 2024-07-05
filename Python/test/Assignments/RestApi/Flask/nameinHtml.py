from flask import Flask, render_template

name = Flask(__name__)

@name.route("/name/<nameval>")
def enter_name(nameval):
    return render_template("name.html", nameval = nameval)

if __name__ == "__main__":
    name.run(debug=True)