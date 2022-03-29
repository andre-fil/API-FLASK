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
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
    def get(self):
        return {'hoteis' : hoteis}

class Hotel(Resource):
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
        novo_hotel = {'hotel_id' : hotel_id, **dados }
        hoteis.append(novo_hotel)
        return novo_hotel, 200

    def put(self, hotel_id):
        dados = Hotel.argumentos.parse_args()
        novo_hotel = {'hotel_id' : hotel_id, **dados }
        hotel = Hotel.find_hotel(hotel_id)
        if hotel:
            hotel.update(novo_hotel)
            return novo_hotel, 200
        hoteis.append(novo_hotel)
        return novo_hotel, 201



    def delete(self, Id):
        pass
