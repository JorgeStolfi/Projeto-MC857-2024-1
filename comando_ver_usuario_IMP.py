import html_pag_ver_usuario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = []

  # Obtém o usuário {usr}:
  usr_id = cmd_args['usuario'] if 'usuario' in cmd_args else None
  if usr_id == None:
    if ses == None:
      usr = None
      erros.append("O identificador do usuário não foi especificado")
    else:
      usr_ses = obj_sessao.obtem_dono(ses)
      assert usr_ses != None
      usr = usr_ses
      usr_id = obj_usuario.obtem_identificador(usr)
  else:
    usr = obj_usuario.obtem_objeto(usr_id)
    if usr == None:
      erros.append(f"O usuário {usr_id} não existe")
  
  if usr == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_ver_usuario.gera(ses, usr, erros)
  return pag
