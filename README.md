# IFSP BACKEND Flask ORM

Projeto realizado em Flask com o intuito de realizar um CRUD num banco de dados relacional (SQL), no caso o MySQL. O projeto realiza o processo de vida util de um produto numa papelaria(C- criação do produto no banco, R- leitura individual e geral dos registros, U- atualização do produto, D- deleção do produto no banco de dados).

Rotas:
- ### GET: /
    - Hello World

- ### GET: /registro/id
    - Retorna um JSON do produto

- ### GET: /registros
    - Retorna um JSON de todos os produtos na base de dados

- ### POST: /cadastro
    - Retorna uma mensagem de sucesso ao cadastrar 
        - Formato de JSON para envio:
    ```
    {
        "name":"Lapiseira",
        "quantity": "210",
        "price":"0.90"
    }
    ```

- ### PUT: /atualizar/id
    - Retorna uma mensagem de sucesso ao atualizar 
        - Formato de JSON para envio:
    ```
    {
        "name":"Lapiseira",
        "quantity": "210",
        "price":"0.90"
    }
    ```


- ### DELETE: /deletar/id
    - Retorna uma mensagem de sucesso ao deletar