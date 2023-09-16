import requests
import json
from bs4 import BeautifulSoup as bs

class suap_client:

    # Constructor
    def __init__( self, usuario, senha ):
        headers: dict[ str, str ] = {
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:106.0) Gecko/20100101 Firefox/106.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Referer': 'https://suap.ifsuldeminas.edu.br/accounts/login/'
        }
         
        self.__session = requests.Session( )
        self.__endpoint = 'https://suap.ifsuldeminas.edu.br/api/v2/'
        url = self.__endpoint + 'autenticacao/token/'

        params = { 'username': usuario, 'password': senha }
        login_response = self.__session.post( url, data = params )
        self.__access = json.loads( login_response.text )[ 'refresh' ]

        page = self.__session.get( url= 'https://suap.ifsuldeminas.edu.br/accounts/login/', headers= headers )
        parser = bs( page.text, 'html.parser' )
        self.__token = parser.find( 'input', { 'type': 'hidden' } )[ 'value' ]

        post_data = {
            'csrfmiddlewaretoken': self.__token,
            'username': usuario,
            'password': senha,
            'this_is_the_login_form': '1',
            'next': '/',
            'g-recaptcha-response': ''
        }

        self.__session.post( url= 'https://suap.ifsuldeminas.edu.br/accounts/login/', headers= self.headers, data= post_data )
    
    # Retorna o token
    def get_token( self ):
        return self.__token
        
    # Retorna os dados do usuário
    def get_dados( self ):
        return self.__send_get( f'{ self.__endpoint }minhas-informacoes/meus-dados/' )
        
    # Retorna o boletim do usuário
    def get_boletim( self, ano, periodo ):
        return self.__send_get( f'{ self.__endpoint }minhas-informacoes/boletim/{ ano }/{ periodo }' )

    # Helper para mandar GET requests
    def __send_get( self, url ):
        h = { 
            'Authorization': self.__access,
            'Accept': 'application/json',
            'X-CSRFToken': self.__token
        }
        r = self.__session.get( url, headers= h )
        
        return json.loads( r.text )