from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
todo = {}

class TodoData(Resource):
    def get(self, todo_id):
        if todo_id in todo:
            return {todo_id: todo[todo_id]}
        return {"error": "Todo item not found"}, 404

    def post(self, todo_id):
        if request.is_json:
            data = request.get_json()
            if 'data' in data:
                todo[todo_id] = data['data']
                return {todo_id: todo[todo_id]}, 201
            return {"error": "Invalid JSON data"}, 400
        return {"error": "Request must be JSON"}, 400

api.add_resource(TodoData, '/<string:todo_id>')

if __name__ == "__main__":
    app.run(debug=True)
