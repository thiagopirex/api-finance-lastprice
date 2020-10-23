from flask import Flask 
from flask_restful import Resource, Api

#import para ações
from yahoo_fin import stock_info

#import para opções
from lxml import html
import requests
#
#---------------------------------------------
#
app = Flask(__name__)
api = Api(app)
  

class Home(Resource):
    def get(self):
        return "Exemplo de uso da API: http://[ip:port]/acao/PETR4"

class Acao(Resource):
    def get(self, codigo_ativo):
        valor = stock_info.get_live_price(codigo_ativo + ".SA")
        print (codigo_ativo + ": " + str(valor))
        return round(valor, 2)
    
class Opcao(Resource):
    def get(self, codigo_ativo):
        #return {'opcao': codigo_ativo}
        page = requests.get('https://br.advfn.com/bolsa-de-valores/bovespa/petrk96-ex-9-65-PETRK96/grafico')
        tree = html.fromstring(page.content)
        prices = tree.xpath('//span[@class="PriceTextUp"]/text()')
        valor = float(prices[2].replace(',', '.'))
        return valor

api.add_resource(Home, '/') # Route_0
api.add_resource(Acao, '/acao/<codigo_ativo>') # Route_1
api.add_resource(Opcao, '/opcao/<codigo_ativo>') # Route_2
