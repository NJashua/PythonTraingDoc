from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todo_list = {}
class TodoData(Resource):
    def get(self, todo_id):
        if todo_id in todo_list:
            return {todo_id: todo_list[todo_id]}
        else:
            return {'error': 'Todo not found'}, 404

    def post(self, todo_id):
        todo_list[todo_id] = request.form['data']
        return {todo_id: todo_list[todo_id]}, 201

api.add_resource(TodoData, '/todo/<string:todo_id>')

if __name__ == "__main__":
    app.run(debug=True)



# from flask import Flask, request
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# todos = {}

# class TodoSimple(Resource):
#     def get(self, todo_id):
#         return {todo_id: todos[todo_id]}

#     def put(self, todo_id):
#         todos[todo_id] = request.form['data']
#         return {todo_id: todos[todo_id]}

# api.add_resource(TodoSimple, '/<string:todo_id>')

# if __name__ == '__main__':
#     app.run(debug=True)