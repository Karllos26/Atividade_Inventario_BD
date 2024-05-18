from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
import os

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
client = MongoClient(MONGO_URI)
db = client['inventario_db']
collection = db['funcionarios']

@app.route('/api/funcionarios', methods=['POST'])
def add_funcionario():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Nenhum dado enviado!'}), 400

    cpf = data.get('cpf')
    nome = data.get('nome')

    if not cpf or not nome:
        return jsonify({'message': 'CPF e Nome são obrigatórios!'}), 400

    if collection.find_one({'cpf': cpf}):
        return jsonify({'message': 'Funcionário com este CPF já existe!'}), 400

    novo_funcionario = {
        "cpf": cpf,
        "nome": nome,
        "notebook": None,
        "monitor1": None,
        "monitor2": None,
        "teclado": None,
        "mouse": None,
        "nobreak": None,
        "desktop": None,
        "headset": None,
        "celular": None,
        "acessorios": None
    }
    collection.insert_one(novo_funcionario)

    return jsonify({'message': 'Funcionário adicionado com sucesso!'}), 201


@app.route('/api/funcionarios', methods=['GET'])
def get_funcionarios():
    funcionarios = list(collection.find({}, {'_id': 0}))
    return jsonify(funcionarios)


@app.route('/api/funcionarios/<cpf>', methods=['GET'])
def get_funcionario(cpf):
    funcionario = collection.find_one({'cpf': cpf}, {'_id': 0})
    if funcionario:
        return jsonify(funcionario)
    else:
        return jsonify({'message': 'Funcionário não encontrado!'}), 404


@app.route('/api/funcionarios/<cpf>', methods=['PUT'])
def update_funcionario(cpf):
    data = request.get_json()
    updated = collection.update_one({'cpf': cpf}, {'$set': {'nome': data.get('nome')}})
    if updated.matched_count:
        return jsonify({'message': 'Funcionário atualizado com sucesso!'}), 200
    return jsonify({'message': 'Funcionário não encontrado!'}), 404


@app.route('/api/funcionarios/<cpf>/<asset>', methods=['PUT'])
def update_asset(cpf, asset):
    valid_assets = ["notebook", "monitor1", "monitor2", "teclado", "mouse", "nobreak", "desktop", "headset", "celular", "acessorios"]
    if asset not in valid_assets:
        return jsonify({'message': 'Ativo inválido!'}), 400

    data = request.get_json()
    updated = collection.update_one({'cpf': cpf}, {'$set': {asset: data.get(asset)}})
    if updated.matched_count:
        return jsonify({'message': f'{asset} atualizado com sucesso!'}), 200
    return jsonify({'message': 'Funcionário não encontrado!'}), 404


@app.route('/api/funcionarios/<cpf>/<asset>', methods=['DELETE'])
def delete_asset(cpf, asset):
    valid_assets = ["notebook", "monitor1", "monitor2", "teclado", "mouse", "nobreak", "desktop", "headset", "celular", "acessorios"]
    if asset not in valid_assets:
        return jsonify({'message': 'Ativo inválido!'}), 400

    updated = collection.update_one({'cpf': cpf}, {'$set': {asset: None}})
    if updated.matched_count:
        return jsonify({'message': f'{asset} removido com sucesso!'}), 200
    return jsonify({'message': 'Funcionário não encontrado!'}), 404


@app.route('/api/funcionarios/<cpf>', methods=['DELETE'])
def delete_funcionario(cpf):
    funcionario = collection.find_one({'cpf': cpf})
    if funcionario:
        if any(funcionario[asset] for asset in funcionario if asset != 'cpf' and asset != 'nome'):
            return jsonify({'message': 'Funcionário possui ativos e não pode ser excluído!'}), 400

        collection.delete_one({'cpf': cpf})
        return jsonify({'message': 'Funcionário excluído com sucesso!'}), 200

    return jsonify({'message': 'Funcionário não encontrado!'}), 404


if __name__ == '__main__':
    app.run(debug=True)