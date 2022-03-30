from flask_restful import Resource, reqparse

hoteis=[
{'hotel_id' : '1',
'Nome' : 'San Pedro',
'Estrelas' : 4.3,
'Diaria' : 150.00,
'Cidade' : 'Pedreiras'
},
{'hotel_id' : '2',
'Nome' : 'Palace Hotel',
'Estrelas' : 4.0,
'Diaria' : 170.00,
'Cidade' : 'Trizidela do Vale'
},
{'hotel_id' : '3',
'Nome' : 'Princesa do Mearim',
'Estrelas' : 3.5,
'Diaria' : 10.00,
'Cidade' : 'Pedreiras'
}
]

class Hoteis(Resource):

    def get(self):
        return {'hoteis' : hoteis}

class HotelModel:
    def __init__(self, hotel_id, Nome,Estrelas,Diaria,Cidade):
        self.hotel_id = hotel_id
        self.Nome = Nome
        self.Estrelas = Estrelas
        self.Diaria = Diaria
        self.Cidade = Cidade 

    def json(self):
        return{
        "hotel_id" : self.hotel_id,
        "Nome" : self.Nome,
        "Estrelas" : self.Estrelas,
        "Diaria" : self.Diaria,
        "Cidade" : self.Cidade
        }

class Hotel(Resource):
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('Nome')
    argumentos.add_argument('Estrelas')
    argumentos.add_argument('Diaria')
    argumentos.add_argument('Cidade')

    def get(self, hotel_id):
        if hotel:
            return hotel
        return {'Message' : 'Hotel not found'}, 404

    def post(self, hotel_id):

        dados = Hotel.argumentos.parse_args()
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        #novo_hotel = {'hotel_id' : hotel_id, **dados }
        hotel_objeto = HotelModel(hotel_id, **dados)
        novo_hotel = hotel_objeto.json()
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201



    def delete(self, hotel_id):
        # hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
        global hoteis
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hoteis.remove(hotel)
            return {'message' : 'Hotel deleted'}
        return {'message' : 'Hotel não encontrado'}
