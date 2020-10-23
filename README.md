# API Última Cotação
API para consulta do último valor da cotação de um ativo


## Configuração e instalação da API:
 
  Instale os pacotes a seguir:
  
	pip install flask flask-jsonpify flask-restful requests yahoo_fin lxml pandas

  Execute o server:
  
  	python server.py
  	
## Exemplo de utilização da API

  Requisição:

	http://localhost:5002/acao/PETR4
	
	
  Resposta:
  
  	Valor da cotação atual do ativo
  