from flask import Flask, render_template

james = Flask(__name__)

@james.route("/")
def get_james_greetings():
    print("M1 clear anttagaaaa!!")
    return render_template('james.html')

if __name__ == "__main__":
    james.run(debug=True)