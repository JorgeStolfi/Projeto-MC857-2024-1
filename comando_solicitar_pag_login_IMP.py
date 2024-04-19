# Implementação do módulo {comando_solicitar_pag_login}. 

import html_pag_login

def processa(ses, cmd_args):
  # Comandos gerados pelas páginas do sistema devem satisfazer estas condições:
  assert ses == None, "Não deveria estar logado"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  assert cmd_args == {}, "Argumentos espúrios"
  
  pag = html_pag_login.gera(None)
  return pag
    
