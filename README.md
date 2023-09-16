# SuapAPI

Uma adaptação em python do projeto originalmente criado por ivmelo (disponível em https://github.com/ivmelo/suap-api-php/).  
Ela atualmente suporta o IFSULDEMINAS, mas pode ser facilmente modificada para suportar outros institutos que usam o mesmo sistema.  
Como dependências, há a lib requests e json.  

# Exemplo de uso

Importar o módulo:  

```python
# main.py
from suap import suap_client

client = suap_client( 'usuario', 'senha' )
print( client.get_dados( ) )
print( client.get_boletim( 2023, 2 ) )
```