# API de Inventário de Ativos de TI

Esta API permite realizar as principais operações de CRUD (Create, Read, Update, Delete) para gerenciar um inventário de ativos de TI de funcionários, salvando os dados em um banco de dados MongoDB.

## Instalação

Clone o repositório:

```bash
git clone <https://github.com/Karllos26/Atividade_Inventario_BD>
```

Crie um ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate   # No Windows use: venv\Scripts\activate
pip install -r requirements.in
```

Configure a variável de ambiente MONGO_URI com a URI do seu MongoDB:

```bash
export MONGO_URI='mongodb://localhost:27017/'
```

Execute a aplicação:

```bash
python app.py
```

## Endpoints

### Inserir um novo funcionário

#### Python

```python
import requests

def inserir_funcionario():
    url = 'http://127.0.0.1:5000/api/funcionarios'
    headers = {'Content-Type': 'application/json'}
    data = {
        "cpf": "12345678903",
        "nome": "Ana Oliveira",
        "notebook_modelo": "Lenovo ThinkPad X1 Carbon",
        "notebook_tag": "TAG456",
        "notebook_versao": "2023",
        "notebook_caracteristicas": "Core i7, 16GB RAM, 512GB SSD",
        "monitor1_modelo": "LG Ultrawide 34",
        "monitor2_modelo": "Dell 27",
        "teclado_modelo": "Microsoft Ergonomic Keyboard",
        "mouse_modelo": "Logitech MX Master 3",
        "nobreak_modelo": "APC 1000VA",
        "desktop_modelo": "Dell OptiPlex 7080",
        "desktop_tag": "TAG789",
        "desktop_versao": "2022",
        "desktop_caracteristicas": "Core i5, 8GB RAM, 256GB SSD",
        "headset_modelo": "Sennheiser HD 660S",
        "celular_modelo": "Samsung Galaxy S21",
        "celular_numero": "123456789",
        "acessorios": "Dock Station, Monitor Stand"
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

inserir_funcionario()
```

#### CURL

```bash
curl -X POST http://127.0.0.1:5000/api/funcionarios \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "cpf": "12345678903",
    "nome": "Ana Oliveira",
    "notebook_modelo": "Lenovo ThinkPad X1 Carbon",
    "notebook_tag": "TAG456",
    "notebook_versao": "2023",
    "notebook_caracteristicas": "Core i7, 16GB RAM, 512GB SSD",
    "monitor1_modelo": "LG Ultrawide 34",
    "monitor2_modelo": "Dell 27",
    "teclado_modelo": "Microsoft Ergonomic Keyboard",
    "mouse_modelo": "Logitech MX Master 3",
    "nobreak_modelo": "APC 1000VA",
    "desktop_modelo": "Dell OptiPlex 7080",
    "desktop_tag": "TAG789",
    "desktop_versao": "2022",
    "desktop_caracteristicas": "Core i5, 8GB RAM, 256GB SSD",
    "headset_modelo": "Sennheiser HD 660S",
    "celular_modelo": "Samsung Galaxy S21",
    "celular_numero": "123456789",
    "acessorios": "Dock Station, Monitor Stand"
}'
```

### Listar todos os funcionários

#### Python

```python
import requests

def listar_funcionarios():
    url = 'http://127.0.0.1:5000/api/funcionarios'
    response = requests.get(url)
    print(response.json())

listar_funcionarios()
```

#### CURL

```bash
curl -X GET http://127.0.0.1:5000/api/funcionarios
```

### Consultar o inventário completo de um determinado funcionário

#### Python

```python
import requests

def consultar_funcionario(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}'
    response = requests.get(url)
    print(response.json())

consultar_funcionario("12345678903")
```

#### CURL

```bash
curl -X GET http://127.0.0.1:5000/api/funcionarios/12345678903
```

### Atualizar o nome do funcionário tendo como referência o CPF

#### Python

```python
import requests

def atualizar_nome(cpf, nome):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}'
    headers = {'Content-Type': 'application/json'}
    data = {"nome": nome}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_nome("12345678903", "Ana Maria Oliveira")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903 \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "nome": "Ana Maria Oliveira"
}'
```

### Atualizar as informações do ativo notebook

#### Python

```python
import requests

def atualizar_notebook(cpf, modelo, tag, versao, caracteristicas):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/notebook'
    headers = {'Content-Type': 'application/json'}
    data = {
        "modelo": modelo,
        "tag": tag,
        "versao": versao,
        "caracteristicas": caracteristicas
    }

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_notebook("12345678903", "MacBook Pro", "TAG789", "2021", "M1, 16GB RAM, 1TB SSD")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/notebook \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "MacBook Pro",
    "tag": "TAG789",
    "versao": "2021",
    "caracteristicas": "M1, 16GB RAM, 1TB SSD"
}'
```

### Limpar as informações do ativo notebook

#### Python

```python
import requests

def limpar_notebook(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/notebook'
    response = requests.delete(url)
    print(response.json())

limpar_notebook("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/notebook
```

### Excluir um funcionário

#### Python

```python
import requests

def excluir_funcionario(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}'
    response = requests.delete(url)
    print(response.json())

excluir_funcionario("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903
```

### Atualizar as informações do ativo monitor 1

#### Python

```python
import requests

def atualizar_monitor1(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/monitor1'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_monitor1("12345678903", "Samsung 27'")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/monitor1 \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Samsung 27'"
}'
```

### Limpar as informações do ativo monitor 1

#### Python

```python
import requests

def limpar_monitor1(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/monitor1'
    response = requests.delete(url)
    print(response.json())

limpar_monitor1("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/monitor1
```

### Atualizar as informações do ativo monitor 2

#### Python

```python
import requests

def atualizar_monitor2(c

pf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/monitor2'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_monitor2("12345678903", "Dell 27'")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/monitor2 \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Dell 27'"
}'
```

### Limpar as informações do ativo monitor 2

#### Python

```python
import requests

def limpar_monitor2(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/monitor2'
    response = requests.delete(url)
    print(response.json())

limpar_monitor2("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/monitor2
```

### Atualizar as informações do ativo teclado

#### Python

```python
import requests

def atualizar_teclado(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/teclado'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_teclado("12345678903", "Razer BlackWidow")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/teclado \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Razer BlackWidow"
}'
```

### Limpar as informações do ativo teclado

#### Python

```python
import requests

def limpar_teclado(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/teclado'
    response = requests.delete(url)
    print(response.json())

limpar_teclado("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/teclado
```

### Atualizar as informações do ativo mouse

#### Python

```python
import requests

def atualizar_mouse(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/mouse'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_mouse("12345678903", "Logitech G Pro")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/mouse \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Logitech G Pro"
}'
```

### Limpar as informações do ativo mouse

#### Python

```python
import requests

def limpar_mouse(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/mouse'
    response = requests.delete(url)
    print(response.json())

limpar_mouse("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/mouse
```

### Atualizar as informações do ativo nobreak

#### Python

```python
import requests

def atualizar_nobreak(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/nobreak'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_nobreak("12345678903", "CyberPower 1500VA")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/nobreak \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "CyberPower 1500VA"
}'
```

### Limpar as informações do ativo nobreak

#### Python

```python
import requests

def limpar_nobreak(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/nobreak'
    response = requests.delete(url)
    print(response.json())

limpar_nobreak("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/nobreak
```

### Atualizar as informações do ativo desktop

#### Python

```python
import requests

def atualizar_desktop(cpf, modelo, tag, versao, caracteristicas):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/desktop'
    headers = {'Content-Type': 'application/json'}
    data = {
        "modelo": modelo,
        "tag": tag,
        "versao": versao,
        "caracteristicas": caracteristicas
    }

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_desktop("12345678903", "HP EliteDesk", "TAG123", "2023", "Core i9, 32GB RAM, 1TB SSD")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/desktop \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "HP EliteDesk",
    "tag": "TAG123",
    "versao": "2023",
    "caracteristicas": "Core i9, 32GB RAM, 1TB SSD"
}'
```

### Limpar as informações do ativo desktop

#### Python

```python
import requests

def limpar_desktop(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/desktop'
    response = requests.delete(url)
    print(response.json())

limpar_desktop("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/desktop
```

### Atualizar as informações do ativo headset

#### Python

```python
import requests

def atualizar_headset(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/headset'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_headset("12345678903", "Sony WH-1000XM4")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/headset \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Sony WH-1000XM4"
}'
```

### Limpar as informações do ativo headset

#### Python

```python
import requests

def limpar_headset(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/headset'
    response = requests.delete(url)
    print(response.json())

limpar_headset("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/headset
```

### Atualizar as informações do ativo celular

#### Python

```python
import requests

def atualizar_celular(cpf, modelo, numero):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/celular'
    headers = {'Content-Type': 'application/json'}
    data = {
        "modelo": modelo,
        "numero": numero
    }

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_celular("12345678903", "iPhone 13 Pro", "987654321")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/celular \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "i

Phone 13 Pro",
    "numero": "987654321"
}'
```

### Limpar as informações do ativo celular

#### Python

```python
import requests

def limpar_celular(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/celular'
    response = requests.delete(url)
    print(response.json())

limpar_celular("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/celular
```

### Atualizar as informações do ativo notebook

#### Python

```python
import requests

def atualizar_notebook(cpf, modelo, tag, versao, caracteristicas):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/notebook'
    headers = {'Content-Type': 'application/json'}
    data = {
        "modelo": modelo,
        "tag": tag,
        "versao": versao,
        "caracteristicas": caracteristicas
    }

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_notebook("12345678903", "Dell XPS", "TAG456", "2022", "Core i7, 16GB RAM, 512GB SSD")
```

#### CURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678903/notebook \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Dell XPS",
    "tag": "TAG456",
    "versao": "2022",
    "caracteristicas": "Core i7, 16GB RAM, 512GB SSD"
}'
```

### Limpar as informações do ativo notebook

#### Python

```python
import requests

def limpar_notebook(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/notebook'
    response = requests.delete(url)
    print(response.json())

limpar_notebook("12345678903")
```

#### CURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678903/notebook
```
