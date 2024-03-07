# Implementação do módulo {comando_solicitar_pag_cadastrar_usuario}. 

import html_pag_cadastrar_usuario

def processa(ses, args):
  pag = html_pag_cadastrar_usuario.gera(ses, None, None)
  return pag
    
