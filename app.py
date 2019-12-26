from flask import Flask, jsonify, request, json

app = Flask(__name__)

desenvolvedores = [
    {'nome':'Rafael','habilidades': ['Python','Flask']},{'nome':'Borges','habilidades': ['Python','Django']}
]

# Implementa um método 'get' para devolver um desenvolvedor pelo ID
# também um método 'put' e 'delete' para alterar e deletar o desenvolvedor.
@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor ID {}, não existe.'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'Registro excluído'})

if __name__ == '__main__':
    app.run()
