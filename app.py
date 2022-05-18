#Fazendo importações de bibliotecas
from flask import Flask, request
from flask_restful import Api
from resources.hotel import Hoteis, Hotel
#Definindo aonexão do arquivo com o Flask
app = Flask(__name__)
#configurando caminho e nome do banco
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
#opcional
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Instanciando uma conexão com a Api
api = Api(app)

#Criando o banco apenas antes da primeira requisição
@app.before_first_request
def cria_banco():
    banco.create_all()

#rota de teste
@app.get('/oi')
def hj():
    return "teste"

#Definindo o caminho das rotas (urls) -> Adicionando recursos
api.add_resource   (Hoteis, '/hoteis')
api.add_resource   (Hotel, '/hoteis/<string:hotel_id>')

#Inicializando o programa
if __name__ == '__main__':
    #importanto banco do arquivo sql_alchemy
    from sql_alchemy import banco
    banco.init_app(app)
    app.run(debug=True)
