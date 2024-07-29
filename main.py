from flask import Flask, jsonify, request
import json
from database import db
from flask_migrate import Migrate
from models.produto import Produto

app = Flask(__name__)
app.config['SECRET_KEY'] = 'palavra_secreta'


#String de Conexão
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@127.0.0.1/backend'
db.init_app(app)

#Inicializando classe para Migrate
migrate = Migrate(app, db)

@app.route("/", methods = ['GET'])
def home():
    return "Hello, World!"

@app.route("/cadastro", methods = ['POST'])
def cadastroProduto():
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    price = data.get("price")
    produto = Produto(name, quantity, price)
    
    db.session.add(produto)
    db.session.commit()
    return jsonify({"message":"Produto cadastrado"})

@app.route("/registro/<int:id>", methods = ["GET"])
def mostrarRegistro(id):
    produto = Produto.query.get(id)
    return jsonify(produto.to_dict())

@app.route("/registros", methods = ["GET"])
def mostrarRegistros():
    produtos_treateds = []
    produtos = Produto.query.all()
    for produto in produtos:
        _produto = Produto.query.get(produto.id)
        _produto_treated = _produto.to_dict()
        produtos_treateds.append(_produto_treated)
        
    return jsonify(produtos_treateds)

@app.route("/atualizar/<int:id>", methods = ["PUT"])
def atualizarRegistro(id):
    produto = Produto.query.get(id)
    
    data = request.json
    name = data.get("name")
    quantity = data.get("quantity")
    price = data.get("price")
    
    if name != produto.name:
        produto.name = name
    if quantity != produto.quantity:
        produto.quantity = quantity
    if price != produto.price:
        produto.price = price
    
    db.session.add(produto)
    db.session.commit()
    return jsonify({"message":"produto atualizado"})

@app.route("/deletar/<int:id>", methods = ["DELETE"])
def deletarRegistro(id):
    produto = Produto.query.get(id)
    db.session.delete(produto)
    db.session.commit()
    return jsonify({"message":"produto deletado"})  
    
if __name__ == "__main__":
    app.run(debug=True)
    