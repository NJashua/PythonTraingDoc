from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def page():
    return render_template("page.html")

@app.route('/emp', methods=['POST'])
def add_employee():
    eid = request.form.get('eid')
    ename = request.form.get('ename')
    esal = request.form.get('esal')
    eData = {'eid': eid, 'ename': ename, 'esal': esal}
    return render_template('emp.html', e=eData)

if __name__ == "__main__":
    app.run(debug=True)
