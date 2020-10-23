#import para API
from flask import Flask, request
from flask_restful import Resource, Api

#import para ações
from yahoo_fin import stock_info

#import para opções
from lxml import html
import requests



app = Flask(__name__)
api = Api(app)

class Acao(Resource):
    def get(self, codigo_ativo):
        valor = stock_info.get_live_price(codigo_ativo + ".SA")
        print (codigo_ativo + ": " + str(valor))
        return round(valor, 2)

class Opcao(Resource):
    def get(self, codigo_ativo):
        #return {'opcao': codigo_ativo}
        page = requests.get('https://br.advfn.com/bolsa-de-valores/bovespa/petrk207-ex-20-7-PETRK207/grafico')
        tree = html.fromstring(page.content)
        return options.get_expiration_dates(codigo_ativo)
    

api.add_resource(Acao, '/acao/<codigo_ativo>') # Route_1
api.add_resource(Opcao, '/opcao/<codigo_ativo>') # Route_2

if __name__ == '__main__':
     app.run(port='5002')