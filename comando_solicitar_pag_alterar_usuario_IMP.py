# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_usuario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
from util_erros import erro_prog

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"

  erros = []
  
  usr_ses = obj_sessao.obtem_dono(ses)
  assert usr_ses != None
  admin = obj_usuario.eh_administrador(usr_ses)

  if cmd_args == {} or cmd_args['usuario'] == None :
    # O parâmetro 'usuario' do comando nao foi especificado; supõe que é o dono da sessao:
    usr = usr_ses
    usr_id = obj_usuario.obtem_identificador(usr)
  elif cmd_args['usuario'] != None:
    # O parâmetro 'usuario' foi especificado; obtém dados do do dito cujo.
    usr_id = cmd_args['usuario']
    usr = obj_usuario.obtem_objeto(usr_id)
    if usr == None:
      erros.append(f"usuario '{usr_id}' não existe")
  else:
    erros.append("usuário não especificado")

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    atrs = obj_usuario.obtem_atributos(usr)
    pag = html_pag_alterar_usuario.gera(ses, usr_id, atrs, None)
  return pag
    
