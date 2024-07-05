# from flask import Flask, render_template, redirect, jsonify
# from flask_restful import Resource, Api

# james_bond = Flask(__name__)
# api = Api(james_bond)

# class Hey_james(Resource):
#     def get(self):
#         return{"Hello": "James Bond", redirect: "index.html"}
    
# api.add_resource(Hey_james, '/')

# if __name__ == "__main__":
#     james_bond.run(debug=True)

# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask
from flask_restful import request, Api, Resource

simple_todo = Flask(__name__)
todo_api = Api(simple_todo)
list_todo = {}
# todo_id = None
class Hey_Simple_Todo(Resource):
    def get(self, todo_id):
        # return list_todo[todo_id]
        if todo_id in list_todo:
            return {todo_id: list_todo[todo_id]}
        else:
            return {"No todo id is there"}, 404
    
    def post(self, todo_id):
        list_todo[todo_id] = request.form['data']
        return {todo_id: list_todo[todo_id]}, 201
    
todo_api.add_resource(Hey_Simple_Todo, '/data/<string:todo_id>')

if __name__ == "__main__":
    simple_todo.run(debug=True)



#     def post(self, todo_id):
#         todo_list[todo_id] = request.form['data']
#         return {todo_id: todo_list[todo_id]}, 201

# api.add_resource(TodoData, '/todo/<string:todo_id>')