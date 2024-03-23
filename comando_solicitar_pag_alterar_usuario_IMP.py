# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_usuario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
from util_testes import erro_prog

def processa(ses, cmd_args):
  erros = [ ].copy()
  if ses == None or not obj_sessao.aberta(ses):
    erros.append("sessão inativa")
  else:
    usr_ses = obj_sessao.obtem_usuario(ses)
    assert usr_ses != None
    admin = obj_usuario.obtem_atributo(usr_ses, 'administrador')

    if cmd_args == {} or cmd_args['id_usuario'] == None :
      # O parâmetro 'id_usuario' do comando nao foi especificado; supõe que é o dono da sessao:
      usr = usr_ses
      id_usr = obj_usuario.obtem_identificador(usr)
    elif cmd_args['id_usuario'] != None:
      # O parâmetro 'id_usuario' foi especificado; obtém dados do do dito cujo.
      id_usr = cmd_args['id_usuario']
      usr = obj_usuario.busca_por_identificador(id_usr)
      if usr == None:
        erros.append(f"usuario '{id_usr}' não existe")
    else:
      erros.append("usuário não especificado")

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    atrs = obj_usuario.obtem_atributos(usr)
    pag = html_pag_alterar_usuario.gera(ses, id_usr, atrs, admin, None)
  return pag
    
