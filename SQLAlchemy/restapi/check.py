from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Hey_nithin(Resource):
    def get(self):
        return{"Name":"Nithin Jashua"}

api.add_resource(Hey_nithin, '/')
if __name__ == "__main__":
    app.run(debug=True)