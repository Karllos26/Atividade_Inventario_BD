# API de Inventário de Ativos de TI

Esta API permite realizar as principais operações de CRUD (Create, Read, Update, Delete) para gerenciar um inventário de ativos de TI de funcionários.

## Endpoints

### Adicionar um novo funcionário

- **URL:** `/api/funcionarios`
- **Método:** `POST`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
      "cpf": "12345678901",
      "nome": "João Silva"
  }
  ```
- **Exemplo de uso com cURL:**
  ```bash
  curl -X POST http://127.0.0.1:5000/api/funcionarios -H "Content-Type: application/json" -d "{\"cpf\": \"12345678901\", \"nome\": \"João Silva\"}"
  ```

### Listar todos os funcionários

- **URL:** `/api/funcionarios`
- **Método:** `GET`
- **Exemplo de uso com cURL:**
  ```bash
  curl http://127.0.0.1:5000/api/funcionarios
  ```

### Consultar o inventário completo de um determinado funcionário

- **URL:** `/api/funcionarios/<cpf>`
- **Método:** `GET`
- **Exemplo de uso com cURL:**
  ```bash
  curl http://127.0.0.1:5000/api/funcionarios/12345678901
  ```

### Atualizar o nome do funcionário

- **URL:** `/api/funcionarios/<cpf>`
- **Método:** `PUT`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
      "nome": "João Silva Neto"
  }
  ```
- **Exemplo de uso com cURL:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901 -H "Content-Type: application/json" -d "{\"nome\": \"João Silva Neto\"}"
  ```

### Atualizar as informações do ativo notebook

- **URL:** `/api/funcionarios/<cpf>/notebook`
- **Método:** `PUT`
- **Headers:**
  - `Content-Type: application/json`
- **Body:**
  ```json
  {
      "notebook": "Dell XPS 13"
  }
  ```
- **Exemplo de uso com cURL:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/notebook -H "Content-Type: application/json" -d "{\"notebook\": \"Dell XPS 13\"}"
  ```

### Limpar as informações do ativo notebook

- **URL:** `/api/funcionarios/<cpf>/notebook`
- **Método:** `DELETE`
- **Exemplo de uso com cURL:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/notebook
  ```

## Exemplo de uso com Python

Utilize a biblioteca `requests` para fazer requisições à API:

```python
import requests

# URL base da API
base_url = "http://127.0.0.1:5000/api"

# Adicionar um novo funcionário
response = requests.post(f"{base_url}/funcionarios", json={"cpf": "12345678901", "nome": "João Silva"})
print(response.status_code)
print(response.json())

# Listar todos os funcionários
response = requests.get(f"{base_url}/funcionarios")
print(response.json())

# Consultar o inventário completo de um determinado funcionário
response = requests.get(f"{base_url}/funcionarios/12345678901")
print(response.json())

# Atualizar o nome do funcionário
response = requests.put(f"{base_url}/funcionarios/12345678901", json={"nome": "João Silva Neto"})
print(response.status_code)
print(response.json())

# Atualizar as informações do ativo notebook
response = requests.put(f"{base_url}/funcionarios/12345678901/notebook", json={"notebook": "Dell XPS 13"})
print(response.status_code)
print(response.json())

# Limpar as informações do ativo notebook
response = requests.delete(f"{base_url}/funcionarios/12345678901/notebook")
print(response.status_code)
print(response.json())
```

## Notas

- Certifique-se de que a API está rodando em `http://127.0.0.1:5000` antes de fazer as requisições.
- Cada CPF deve ser único no banco de dados.
- Utilize um CPF diferente se receber um erro de duplicação ao adicionar um novo funcionário.