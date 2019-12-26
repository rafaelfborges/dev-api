from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
        'id': 0, 'nome': 'Rafael', 'habilidades': ['Python', 'Flask']
    },
    {
        'id': 1, 'nome': 'Borges', 'habilidades': ['Python', 'Django']
    }
]

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run()
