# API de Inventário de Ativos de TI

Esta API permite gerenciar um inventário de ativos de TI atribuídos a funcionários, utilizando operações de CRUD (Create, Read, Update, Delete) e armazenando os dados em um banco de dados MongoDB.

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/Karllos26/Atividade_Inventario_BD
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate   # No Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure a variável de ambiente `MONGO_URI` com a URI do seu MongoDB:

```bash
export MONGO_URI='mongodb://localhost:27017/'   # No Windows use: set MONGO_URI='mongodb://localhost:27017/'
```

4. Execute a aplicação:

```bash
python app.py
```

## Sobre o pyvenv.cfg

Ao criar o ambiente virtual com `python -m venv venv`, um arquivo `pyvenv.cfg` é gerado no diretório raiz do ambiente virtual (`venv`). Este arquivo contém informações sobre a configuração do ambiente, como a versão do Python e a localização da instalação principal do Python.

## Endpoints

### Adicionar um novo funcionário

- **URL:** `/api/funcionarios`
- **Método:** POST
- **Headers:** `Content-Type: application/json`

#### Exemplo de uso com cURL:

```bash
curl -X POST http://127.0.0.1:5000/api/funcionarios -H "Content-Type: application/json" -d '{
    "cpf": "12345678901",
    "nome": "João Silva",
    "notebook_modelo": "Dell XPS 13",
    "notebook_tag": "TAG123",
    "notebook_versao": "2023",
    "notebook_caracteristicas": "Core i7, 16GB RAM, 512GB SSD",
    "monitor1_modelo": "Samsung 24",
    "monitor2_modelo": "Dell 27",
    "teclado_modelo": "Logitech K380",
    "mouse_modelo": "Logitech MX Master 3",
    "nobreak_modelo": "APC 1500VA",
    "desktop_modelo": "HP Pavilion",
    "desktop_tag": "TAG456",
    "desktop_versao": "2022",
    "desktop_caracteristicas": "Core i5, 8GB RAM, 1TB HDD",
    "headset_modelo": "Plantronics Blackwire 3220",
    "celular_modelo": "iPhone 12",
    "celular_numero": "987654321",
    "acessorios": "Dock Station"
}'
```

#### Exemplo de uso com Python:

```python
import requests

url = 'http://127.0.0.1:5000/api/funcionarios'
data = {
    "cpf": "12345678901",
    "nome": "João Silva",
    "notebook_modelo": "Dell XPS 13",
    "notebook_tag": "TAG123",
    "notebook_versao": "2023",
    "notebook_caracteristicas": "Core i7, 16GB RAM, 512GB SSD",
    "monitor1_modelo": "Samsung 24",
    "monitor2_modelo": "Dell 27",
    "teclado_modelo": "Logitech K380",
    "mouse_modelo": "Logitech MX Master 3",
    "nobreak_modelo": "APC 1500VA",
    "desktop_modelo": "HP Pavilion",
    "desktop_tag": "TAG456",
    "desktop_versao": "2022",
    "desktop_caracteristicas": "Core i5, 8GB RAM, 1TB HDD",
    "headset_modelo": "Plantronics Blackwire 3220",
    "celular_modelo": "iPhone 12",
    "celular_numero": "987654321",
    "acessorios": "Dock Station"
}

response = requests.post(url, json=data)
print(response.json())
```

### Listar todos os funcionários

- **URL:** `/api/funcionarios`
- **Método:** GET

#### Exemplo de uso com cURL:

```bash
curl http://127.0.0.1:5000/api/funcionarios
```

### Consultar o inventário completo de um funcionário

- **URL:** `/api/funcionarios/<cpf>`
- **Método:** GET

#### Exemplo de uso com cURL:

```bash
curl http://127.0.0.1:5000/api/funcionarios/12345678901
```

### Atualizar o nome do funcionário

- **URL:** `/api/funcionarios/<cpf>`
- **Método:** PUT
- **Headers:** `Content-Type: application/json`

#### Exemplo de uso com cURL:

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901 -H "Content-Type: application/json" -d '{"nome": "João Silva Neto"}'
```

### Atualizar as informações de um ativo

- **URL:** `/api/funcionarios/<cpf>/<asset>`
- **Método:** PUT
- **Headers:** `Content-Type: application/json`

#### Exemplo de uso com cURL:

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/notebook -H "Content-Type: application/json" -d '{"notebook": "Dell XPS 13"}'
```

Substitua `<asset>` pelo tipo de ativo que deseja atualizar e `<modelo>` pelo novo modelo do ativo.

### Limpar as informações de um ativo

- **URL:** `/api/funcionarios/<cpf>/<asset>`
- **Método:** DELETE

#### Exemplo de uso com cURL:

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/notebook
```

### Excluir um funcionário

- **URL:** `/api/funcionarios/<cpf>`
- **Método:** DELETE

#### Exemplo de uso com cURL:

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901
```
