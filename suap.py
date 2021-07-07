import requests
import json

class suap_client:

    # Constructor
    # Como parâmetro, recebe o usuário/senha e salva o token
    def __init__( self, usuario, senha ):
        self.__endpoint = 'https://suap.ifsuldeminas.edu.br/api/v2/'
        url = self.__endpoint + 'autenticacao/token/'
        params = { 'username': usuario, 'password': senha }
        r = requests.post( url, data = params )
        self.__token = json.loads( r.text )[ 'token' ]
    
    # Retorna o token
    def get_token( self ):
        return self.__token
        
    # Retorna os dados do usuário
    def get_dados( self ):
        return self.__send_get( '{0}minhas-informacoes/meus-dados/'.format( self.__endpoint ) )
        
    # Retorna o boletim do usuário
    def get_boletim( self, ano, periodo ):
        return self.__send_get( '{0}minhas-informacoes/boletim/{1}/{2}'.format( self.__endpoint, ano, periodo ) )

    # Helper para mandar GET requests
    def __send_get( self, url ):
        h = { 'Authorization': 'JWT ' + self.__token }
        r = requests.get( url, headers = h )
        
        return json.loads( r.text )