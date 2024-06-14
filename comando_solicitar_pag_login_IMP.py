# Implementação do módulo {comando_solicitar_pag_login}. 

import html_pag_login

def processa(ses, cmd_args):
  # Comandos gerados pelas páginas do sistema devem satisfazer estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert type(cmd_args) is dict, "Argumentos inválidos"
  assert cmd_args == {}, "Argumentos espúrios"
  
  erros = []
  
  if ses != None and obj_sessao.aberta(ses):
    erros.append("Precisa fazer logout antes de pedir login")
    
  if len(erros) != 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else: 
    pag = html_pag_login.gera(None)
  return pag
    
