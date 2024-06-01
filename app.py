from flask import Flask, request, jsonify
from pymongo import MongoClient
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
        "notebook": {
            "modelo": data.get('notebook_modelo'),
            "tag": data.get('notebook_tag'),
            "versao": data.get('notebook_versao'),
            "caracteristicas": data.get('notebook_caracteristicas')
        },
        "monitor1": {
            "modelo": data.get('monitor1_modelo')
        },
        "monitor2": {
            "modelo": data.get('monitor2_modelo')
        },
        "teclado": {
            "modelo": data.get('teclado_modelo')
        },
        "mouse": {
            "modelo": data.get('mouse_modelo')
        },
        "nobreak": {
            "modelo": data.get('nobreak_modelo')
        },
        "desktop": {
            "modelo": data.get('desktop_modelo'),
            "tag": data.get('desktop_tag'),
            "versao": data.get('desktop_versao'),
            "caracteristicas": data.get('desktop_caracteristicas')
        },
        "headset": {
            "modelo": data.get('headset_modelo')
        },
        "celular": {
            "modelo": data.get('celular_modelo'),
            "numero": data.get('celular_numero')
        },
        "acessorios": data.get('acessorios')
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
    fields_to_update = {key: value for key, value in data.items() if key in ['nome']}
    updated = collection.update_one({'cpf': cpf}, {'$set': fields_to_update})
    if updated.matched_count:
        return jsonify({'message': 'Funcionário atualizado com sucesso!'}), 200
    return jsonify({'message': 'Funcionário não encontrado!'}), 404

@app.route('/api/funcionarios/<cpf>/<asset>', methods=['PUT'])
def update_asset(cpf, asset):
    valid_assets = [
        "notebook", "monitor1", "monitor2", "teclado", "mouse", "nobreak", 
        "desktop", "headset", "celular", "acessorios"
    ]
    if asset not in valid_assets:
        return jsonify({'message': 'Ativo inválido!'}), 400

    data = request.get_json()
    if asset in ["notebook", "desktop"]:
        fields_to_update = {f"{asset}.{key}": value for key, value in data.items() if key in ['modelo', 'tag', 'versao', 'caracteristicas']}
    elif asset in ["monitor1", "monitor2", "teclado", "mouse", "nobreak", "headset"]:
        fields_to_update = {f"{asset}.modelo": data.get('modelo')}
    elif asset == "celular":
        fields_to_update = {f"{asset}.{key}": value for key, value in data.items() if key in ['modelo', 'numero']}
    else:
        fields_to_update = {asset: data.get(asset)}

    updated = collection.update_one({'cpf': cpf}, {'$set': fields_to_update})
    if updated.matched_count:
        return jsonify({'message': f'{asset} atualizado com sucesso!'}), 200
    return jsonify({'message': 'Funcionário não encontrado!'}), 404

@app.route('/api/funcionarios/<cpf>/<asset>', methods=['DELETE'])
def delete_asset(cpf, asset):
    valid_assets = [
        "notebook", "monitor1", "monitor2", "teclado", "mouse", "nobreak", 
        "desktop", "headset", "celular", "acessorios"
    ]
    if asset not in valid_assets:
        return jsonify({'message': 'Ativo inválido!'}), 400

    if asset in ["notebook", "desktop"]:
        fields_to_update = {f"{asset}.{field}": None for field in ['modelo', 'tag', 'versao', 'caracteristicas']}
    elif asset in ["monitor1", "monitor2", "teclado", "mouse", "nobreak", "headset"]:
        fields_to_update = {f"{asset}.modelo": None}
    elif asset == "celular":
        fields_to_update = {f"{asset}.{field}": None for field in ['modelo', 'numero']}
    else:
        fields_to_update = {asset: None}

    updated = collection.update_one({'cpf': cpf}, {'$set': fields_to_update})
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
