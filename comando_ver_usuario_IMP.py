import html_pag_ver_usuario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_usuario

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = [].copy()

  # Obtém o usuário {usr}:
  id_usr = cmd_args['usuario'] if 'usuario' in cmd_args else None
  if id_usr == None:
    if ses == None:
      usr = None
      erros.append("O identificador do usuário não foi especificado")
    else:
      usr_ses = obj_sessao.obtem_usuario(ses)
      usr = usr_ses
      id_usr = obj_usuario.obtem_identificador(usr)
  else:
    usr = obj_usuario.busca_por_identificador(id_usr)
    if usr == None:
      erros.append(f"O usuário {id_usr} não existe")
  
  if usr == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_ver_usuario.gera(ses, usr, erros)
  return pag
