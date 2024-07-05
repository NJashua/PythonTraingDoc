# import json
# from flask import Flask, request,redirect, jsonify
# # from flask_sqlalchemy import SQLAlchem
# app = Flask(__name__)
# app.config['DATABASE_URL_CONNECTION'] = r'empdb.db'

# SQL.ALCHEMY(app)

# import json
# from flask import Flask, request, redirect, jsonify
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empdb.db'

# db = SQLAlchemy(app)  
# class Employee(db.Model):
#     Eid = db.Column(db.Integer, primary_key=True)
#     Ename = db.Column(db.String(80), nullable=False)
#     Eemail = db.Column(db.String(120), nullable=False)
#     Esal = db.Column(db.Integer)


#     def __repr__(self):
#         return f'<Employee {self.name}>'
# with app.app_context():
#     db.create_all()
# @app.route('/')
# def home():
#     return "Welcome to the Employee Database!"

# @app.route('/employees', methods=['GET'])
# def get_employees():
#     employees = Employee.query.all()
#     return jsonify([{'id': e.id, 'name': e.name, 'position': e.position} for e in employees])

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empdb.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Employee(db.Model):
    Eid = db.Column(db.Integer, primary_key=True)
    Ename = db.Column(db.String(80), nullable=False)
    Eemail = db.Column(db.String(120), nullable=False)
    Esal = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'Eid': self.Eid,
            'Ename': self.Ename,
            'Eemail': self.Eemail,
            'Esal': self.Esal
        }

@app.before_request
def create_tables():
    db.create_all()

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.json
    new_employee = Employee(Eid = data['Eid'], Ename=data['Ename'], Eemail=data['Eemail'], Esal=data['Esal'])
    db.session.add(new_employee)
    db.session.commit()
    return jsonify({'message': 'Employee added successfully'}), 201

@app.route('/employees', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return jsonify([employee.to_dict() for employee in employees])

@app.route('/update', methods = ['PUT'])
def update_employee():
    data = request.json
    employee_id = data.get('Eid')
    employee = Employee.query.get(employee_id)
    if employee:
        employee.Ename = data.get('Ename', employee.Ename)
        employee.Eemail = data.get('Eemail', employee.Eemail)
        employee.Esal = data.get('Esal', employee.Esal)
        db.session.commit()
        return jsonify({"Message" : "Employee data updated successfully"}), 200
    else:
        return jsonify({"Message" : "Employee not found"}), 400

@app.route('/delete', methods = ['DELETE'])
def delete_employee():
    data = request.json
    employee_id = data.get('Eid')
    employee = Employee.query.get(employee_id)
    if employee:
        db.session.delete(employee)
        return jsonify({'Message': "Employee deleted successfully"}),200
    else:
        return jsonify({'Message': "No employee there with that id"}), 404
    
@app.route("/get_by_id/<int:id>", methods=['GET'])
def get_employee_id(id):
    employee = Employee.query.get(id)
    if employee:
        return jsonify(employee.to_dict()), 200
    else:
        return jsonify({'Message': "Employee not found"}), 404
if __name__ == '__main__':
    app.run(debug=True)
