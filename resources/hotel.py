#Realizando importações necessárias
from flask_restful import Resource, reqparse
from sql_alchemy import banco


#Classe Hoteis - método de retornar os hotéis cadastrados
class Hoteis(Resource):
    #Método GET - Total
    def get(self):
        return {'hotéis': [hotel.json() for hotel in HotelModel.query.all()]} #Select * from hoteis

#Classe de modelo hotel, Definindo os atributos e os métodos de classe
class HotelModel(banco.Model):
    #Definindo configurações para cadastro no Banco de Dados
    __tablename__ = 'Hoteis'
    hotel_id = banco.Column(banco.String, primary_key = True) #Definindo a primary_key como hotel_id
    Nome = banco.Column(banco.String(80))
    Estrelas = banco.Column(banco.Float(precision=1))
    Diaria = banco.Column(banco.Float(precision=2))
    Cidade = banco.Column(banco.String(80))



    #Definindo parâmetros dos hotéis - atributos
    def __init__(self, hotel_id, Nome,Estrelas,Diaria,Cidade):
        self.hotel_id = hotel_id
        self.Nome = Nome
        self.Estrelas = Estrelas
        self.Diaria = Diaria
        self.Cidade = Cidade

    #Transformando os dados para o formarto Json
    def json(self):
        return{
        "hotel_id" : self.hotel_id,
        "Nome" : self.Nome,
        "Estrelas" : self.Estrelas,
        "Diaria" : self.Diaria,
        "Cidade" : self.Cidade
        }

        #Criando método para encontrar hotéis//salvar//atualizar//deletar hotéis no BD --> Funções de classe
    @classmethod
    def find_hotel(cls, hotel_id):
        hotel = cls.query.filter_by(hotel_id = hotel_id).first() #select * from hoteis where hotel_id=$hotel_id
        if hotel:
            return hotel
        return None

    def save_hotel(self):
        banco.session.add(self)
        banco.session.commit()

    def update_hotel(self, Nome, Estrelas, Diaria, Cidade):
        self.Nome = Nome
        self.Estrelas = Estrelas
        self.Diaria = Diaria
        self.Cidade = Cidade

    def delete_hotel(self):
        banco.session.delete(self)
        banco.session.commit()




#Classe Hotel
class Hotel(Resource):

    #recebendo argumentos passados pelo método post ou put
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('Nome', type=str, required=True,help='The field "Nome" cannot left blank')
    argumentos.add_argument('Estrelas',type=float, required=True,help='The field "Estrelas" cannot left blank')
    argumentos.add_argument('Diaria')
    argumentos.add_argument('Cidade')

    #Retornando o hotel procurado, caso exista
    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'Message' : 'Hotel not found'}, 404

    #Método post - criando novo hotel
    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return '{message: Esse Hotel já existe}', 400

        #Recebendo os dados passados via json e adicionando na var dados
        dados = Hotel.argumentos.parse_args()

        #Instanciando na var hotel os argumentos recebidos
        hotel= HotelModel(hotel_id, **dados)

        #Salvando hotel no BD, caso possível
        try:
            hotel.save_hotel()
        except:
            return {'Internal Error!'}, 500
        return hotel.json()

    #Método para atualizar ou criar hotel ( caso não exista)
    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
            #novo_hotel = {'hotel_id' : hotel_id, **dados }

        #Instanciando na var hotel os argumentos recebidos
        hotel = HotelModel.find_hotel(hotel_id)

        #Verificando se o hotel já existe (atualizar) - ou não ( criar)
        if hotel:
            hotel.update_hotel(**dados) #**dados = atributos do HotelModel
            hotel.save_hotel()
            return hotel.json(), 201
        hotel= HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'Internal Error!'}, 500
        return hotel.json(), 200


        #método de deletar hoteis, caso exista
    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'Internal Error!'}, 500
            return '{message: Hotel deleted}'
        return {'message' : 'Hotel not found'}, 404
