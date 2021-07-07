# SuapAPI

Uma adaptação em python do projeto originalmente criado por ivmelo (disponível em https://github.com/ivmelo/suap-api-php/).
Ela atualmente suporta o IFSULDEMINAS, mas pode ser facilmente modificada para suportar outros institutos que usam o mesmo sistema.
Como dependências, há a lib requests e json.

# Como usar

Importar o módulo:
```python
from suap import suap_client
```


Criar o objeto do client (coloque suas credenciais nos locais indicados):
```python
suap_client = suap_client( 'usuario', 'senha' )
```

Agora você pode usar as funções disponíveis.

get_boletim -> Recebe o ano e o período. Retorna um JSON com os dados do boletim.
get_dados -> Retorna um JSON com os dados do aluno.
get_token -> Retorna o token de acesso gerado no login.
