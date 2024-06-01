---
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
pip install -r requirements.txt
```

Configure a variável de ambiente MONGO_URI com a URI do seu MongoDB:

```bash
export MONGO_URI='mongodb://localhost:27017/'   # No Windows use: set MONGO_URI='mongodb://localhost:27017/'
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
        "cpf": "12345678901",
        "nome": "João Silva",
        "notebook_modelo": "Dell XPS 13",
        "notebook_tag": "TAG123",
        "notebook_versao": "2023",
        "notebook_caracteristicas": "Core i7, 16GB RAM, 512GB SSD",
        # Adicione outras informações aqui conforme necessário
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())

inserir_funcionario()
```

#### cURL

```bash
curl -X POST http://127.0.0.1:5000/api/funcionarios \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "cpf": "12345678901",
    "nome": "João Silva",
    "notebook_modelo": "Dell XPS 13",
    "notebook_tag": "TAG123",
    "notebook_versao": "2023",
    "notebook_caracteristicas": "Core i7, 16GB RAM, 512GB SSD",
    # Adicione outras informações aqui conforme necessário
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

#### cURL

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

consultar_funcionario("12345678901")
```

#### cURL

```bash
curl -X GET http://127.0.0.1:5000/api/funcionarios/12345678901
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

atualizar_nome("12345678901", "João Pereira")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901 \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "nome": "João Pereira"
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

atualizar_notebook("12345678901", "MacBook Pro", "TAG456", "2021", "M1, 16GB RAM, 1TB SSD")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/notebook \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "MacBook Pro",
    "tag": "TAG456",
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

limpar_notebook("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/notebook
```

### Excluir um funcionário

#### Python

```python
import requests

def excluir_funcionario(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}'
    response = requests.delete(url)
    print(response.json())

excluir_funcionario("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901
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

atualizar_monitor1("12345678901", "Samsung 27'")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/monitor1 \
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

limpar_monitor1("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/monitor1
```

### Atualizar as informações do ativo monitor 2

#### Python

```python
import requests

def atualizar_monitor2(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/monitor2'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_monitor2("12345678901", "LG 24'")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/monitor2 \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "LG 24'"
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

limpar_monitor2("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/monitor2
```

### Atualizar as informações do ativo teclado

#### Python

```python
import requests

def atualizar_teclado(cpf, modelo):
    url = f'http://127.0.0.1:5000/api/func

ionarios/{cpf}/teclado'
    headers = {'Content-Type': 'application/json'}
    data = {"modelo": modelo}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_teclado("12345678901", "Logitech K120")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/teclado \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Logitech K120"
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

limpar_teclado("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/teclado
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

atualizar_mouse("12345678901", "Logitech M185")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/mouse \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Logitech M185"
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

limpar_mouse("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/mouse
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

atualizar_nobreak("12345678901", "APC Back-UPS 600")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/nobreak \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "APC Back-UPS 600"
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

limpar_nobreak("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/nobreak
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

atualizar_desktop("12345678901", "HP EliteDesk", "DT456", "2022", "Core i5, 8GB RAM, 256GB SSD")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/desktop \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "HP EliteDesk",
    "tag": "DT456",
    "versao": "2022",
    "caracteristicas": "Core i5, 8GB RAM, 256GB SSD"
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

limpar_desktop("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/desktop
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

atualizar_headset("12345678901", "Jabra Evolve 75")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/headset \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "Jabra Evolve 75"
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

limpar_headset("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/headset
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

atualizar_celular("12345678901", "iPhone 12", "99999-9999")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/celular \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{
    "modelo": "iPhone 12",
    "numero": "99999-9999"
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

limpar_celular("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/celular
```

### Atualizar as informações do ativo acessórios

#### Python

```python
import requests

def atualizar_acessorios(cpf, descricao):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/acessorios'
    headers = {'Content-Type': 'application/json'}
    data = {"acessorios": descricao}

    response = requests.put(url, headers=headers, json=data)
    print(response.json())

atualizar_acessorios("12345678901", "Dock Station, Cabo HDMI")
```

#### cURL

```bash
curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/acessorios \
-H "Content-Type: application/json; charset=utf-8" \
--data-raw '{


    "acessorios": "Dock Station, Cabo HDMI"
}'
```

### Limpar as informações do ativo acessórios

#### Python

```python
import requests

def limpar_acessorios(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}/acessorios'
    response = requests.delete(url)
    print(response.json())

limpar_acessorios("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/acessorios
```

## Exclusão de um Funcionário

### Excluir um funcionário se ele não possuir ativos

#### Python

```python
import requests

def excluir_funcionario(cpf):
    url = f'http://127.0.0.1:5000/api/funcionarios/{cpf}'
    response = requests.delete(url)
    print(response.json())

excluir_funcionario("12345678901")
```

#### cURL

```bash
curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901
```

**Nota**: Certifique-se de ter o MongoDB em execução e acessível a partir do URI fornecido antes de iniciar o servidor Flask.