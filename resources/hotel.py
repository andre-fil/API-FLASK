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

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return {'Message' : 'Hotel not found'}, 404
    def post(self, hotel_id):
        argumentos = reqparse.RequestParser()
        argumentos.add_argument('Nome')
        argumentos.add_argument('Estrelas')
        argumentos.add_argument('Diaria')
        argumentos.add_argument('Cidade')

        dados = argumentos.parse_args()
        novo_hotel = {
        'hotel_id' : hotel_id,
        'Nome' : dados['Nome'],
        'Estrelas' : dados['Estrelas'],
        'Diaria' : dados['Diaria'],
        'Cidade' : dados['Cidade']
        }

        hoteis.append(novo_hotel)
        return novo_hotel, 200
    def put(self, Id):
        pass
    def delete(self, Id):
        pass
