from flask import Flask, request, json
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

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID {}, não existe.'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return dados

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluído'}

api.add_resource(Desenvolvedor, '/dev/<int:id>/')


if __name__ == '__main__':
    app.run()
