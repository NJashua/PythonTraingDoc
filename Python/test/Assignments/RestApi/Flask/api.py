# from flask import Flask
# from flask_restful import Resource, Api

# james_bond = Flask(__name__)
# james_bond_api = Api(james_bond)

# class Hey_james(Resource):
#     def hey(self):
#         return {"Name": "James Bond"}

# james_bond_api.add_resource(Hey_james, '/')


# if __name__ == "__main__":
#     james_bond.run(debug=True)

from flask import Flask
from flask_restful import Resource, Api
help = Flask(__name__)
api = Api(help)

class Hello_Ravan(Resource):
    def get(self):
        return {"Ravan feel": "Ravan mawa feeling like there is no one like me...!"}
    
api.add_resource(Hello_Ravan, '/')
if __name__ == "__main__":
    help.run(debug=True)