# Implementação do módulo {comando_solicitar_pag_login}. 

import html_pag_login

def processa(ses, cmd_args):
  pag = html_pag_login.gera(ses, None)
  return pag
    
