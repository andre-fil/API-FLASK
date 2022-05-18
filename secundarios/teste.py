
"""
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
 return "Hello World!"
if __name__ == "__main__":
 app.run()

"""

from flask import Flask
app = Flask(__name__)

@app.get('/')
def index():
    return "olá mundo"

if __name__ =='__main__':
    app.run(debug=True)


    #Criando arrays de hotéis (Dicionário/json)
    '''
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

    '''

    #verificando se oum determinado hotel existe no array de hotéis
    '''
    def find_hotel(hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        return None
        '''

                # hoteis = [hotel for hotel in hoteis if hotel['hotel_id'] != hotel_id]
                '''
                global hoteis
                hotel = Hotel.find_hotel(hotel_id)
                if hotel:
                    hoteis.remove(hotel)
                    return {'message' : 'Hotel deleted'}
                '''
