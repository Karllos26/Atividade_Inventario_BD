
```markdown
# API de Inventário de Ativos de TI

Esta API permite realizar as principais operações de CRUD (Create, Read, Update, Delete) para gerenciar um inventário de ativos de TI de funcionários, salvando os dados em um banco de dados MongoDB.

## Instalação

1. Clone o repositório:
    ```bash
    git clone <https://github.com/Karllos26/Atividade_Inventario_BD>
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

## Sobre o `pyvenv.cfg`

Quando você cria o ambiente virtual usando o comando `python -m venv venv`, um arquivo chamado `pyvenv.cfg` é gerado automaticamente no diretório raiz do ambiente virtual (`venv`). Este arquivo contém informações sobre a configuração do ambiente virtual, como a versão do Python e a localização da instalação principal do Python. 

### Exemplo de conteúdo do `pyvenv.cfg`:

```plaintext
home = /usr/bin
include-system-site-packages = false
version = 3.8.10
```

O `pyvenv.cfg` é essencial para o funcionamento do ambiente virtual, pois ajuda a isolar o ambiente de desenvolvimento das bibliotecas e dependências do sistema global do Python.

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

### Atualizar as informações do ativo

- **URL:** `/api/funcionarios/<cpf>/<asset>`
- **Método:** `PUT`
- **Headers:**
  - `Content-Type: application/json`
- **Body:** (exemplo para notebook)
  ```json
  {
      "notebook": "Dell XPS 13"
  }
  ```
- **Exemplo de uso com cURL:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/notebook -H "Content-Type: application/json" -d "{\"notebook\": \"Dell XPS 13\"}"
  ```

### Limpar as informações do ativo

- **URL:** `/api/funcionarios/<cpf>/<asset>`
- **Método:** `DELETE`
- **Exemplo de uso com cURL:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/notebook
  ```

### Atualizar e Limpar Ativos

- **Atualizar Monitor 1:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/monitor1 -H "Content-Type: application/json" -d "{\"monitor1\": \"Samsung 24\"}"
  ```

- **Limpar Monitor 2:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/monitor2
  ```

- **Atualizar Teclado:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/teclado -H "Content-Type: application/json" -d "{\"teclado\": \"Logitech K380\"}"
  ```

- **Limpar Teclado:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/teclado
  ```

- **Atualizar Mouse:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/mouse -H "Content-Type: application/json" -d "{\"mouse\": \"Logitech MX Master 3\"}"
  ```

- **Limpar Mouse:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/mouse
  ```

- **Atualizar Nobreak:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/nobreak -H "Content-Type: application/json" -d "{\"nobreak\": \"APC 1500VA\"}"
  ```

- **Limpar Nobreak:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/nobreak
  ```

- **Atualizar Desktop:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/desktop -H "Content-Type: application/json" -d "{\"desktop\": \"HP EliteDesk 800\"}"
  ```

- **Limpar Desktop:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/desktop
  ```

- **Atualizar Headset:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/headset -H "Content-Type: application/json" -d "{\"headset\": \"Plantronics Blackwire 3220\"}"
 

 ```

- **Limpar Headset:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/headset
  ```

- **Atualizar Celular:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/celular -H "Content-Type: application/json" -d "{\"celular\": \"iPhone 12\"}"
  ```

- **Limpar Celular:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/celular
  ```

- **Atualizar Acessórios:**
  ```bash
  curl -X PUT http://127.0.0.1:5000/api/funcionarios/12345678901/acessorios -H "Content-Type: application/json" -d "{\"acessorios\": \"Dock Station\"}"
  ```

- **Limpar Acessórios:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901/acessorios
  ```

### Excluir um funcionário

- **URL:** `/api/funcionarios/<cpf>`
- **Método:** `DELETE`
- **Exemplo de uso com cURL:**
  ```bash
  curl -X DELETE http://127.0.0.1:5000/api/funcionarios/12345678901
  ```

**Nota:** Um funcionário só pode ser excluído se não houver nenhum ativo configurado para ele.