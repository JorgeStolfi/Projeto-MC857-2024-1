# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_usuario
import obj_sessao
import obj_usuario
from util_testes import erro_prog

def processa(ses, args):
  if ses == None or not obj_sessao.aberta(ses):
    erro_prog("sessão deveria estar aberta")
  else:
    usr_ses = obj_sessao.obtem_usuario(ses)
    admin = obj_usuario.obtem_atributo(usr_ses, 'administrador')
    
  if args == {} or args['id_usuario'] == None :
    # O 'id_usuario' nao foi especificado; supõe que é o dono da sessao:
    usr = usr_ses
    id_usr = obj_usuario.obtem_identificador(usr)
  elif args['id_usuario'] != None:
    # O 'id_usuario' foi especificado; obtém dados do do dito cujo.
    id_usr = args['id_usuario']
    usr = obj_usuario.busca_por_identificador(id_usr)
  else:
    erro_prog("usuário não identificado")

  atrs = obj_usuario.obtem_atributos(usr)
  pag = html_pag_alterar_usuario.gera(ses, id_usr, atrs, admin, None)
  return pag
    
