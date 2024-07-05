# from flask_restful import reqparse

# parser = reqparse.RequestParser()
# parser.add_argument('rate', type=int, help='Rate to charge for this resource')
# args = parser.parse_args()


from flask_restful import fields, marshal_with, Resource, Api
from flask import Flask, url_for

app = Flask(__name__)
api = Api(app)

resource_fields = {
    'task': fields.String,
    'uri': fields.Url('todo'),
    # 'status': "Response code 200ok"
}

class TodoDao(object):
    def __init__(self, todo_id, task):
        self.todo_id = todo_id
        self.task = task
        self.status = 'active'

class Todo(Resource):
    @marshal_with(resource_fields)
    def get(self, todo_id):
        return TodoDao(todo_id=todo_id, task='Remember the milk')

api.add_resource(Todo, '/todo/<string:todo_id>', endpoint='todo')

if __name__ == "__main__":
    app.run(debug=True)
