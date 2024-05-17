import html_pag_ver_usuario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []
  
  if ses == None or not obj_sessao.aberta(ses):
    ses_dono = None
  else:
    ses_dono = obj_sessao.obtem_dono(ses)

  # Obtém o usuário {usr}:
  usr_id = cmd_args.pop('usuario', None)
  if usr_id == None:
    if ses_dono == None:
      erros.append("O identificador do usuário não foi especificado")
      usr = None
    else:
      usr = ses_dono
      usr_id = obj_usuario.obtem_identificador(usr)
  else:
    usr = obj_usuario.obtem_objeto(usr_id)
    if usr == None:
      erros.append(f"O usuário \"{usr_id}\" não existe")
      
  assert len(cmd_args) == 0, f"Argumentos espúrios \"{cmd_args}\""
  
  if len(erros) == 0:
    assert usr != None
    pag = html_pag_ver_usuario.gera(ses, usr, erros)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
