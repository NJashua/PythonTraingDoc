from flask import Flask

hey_var = Flask(__name__)

@hey_var.route("/user/<username>")
def hey_user(username):
    return f"user is {username}"

if __name__== "__main__":
    hey_var.run(debug=True)