import html_pag_ver_comentario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_comentario

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = [].copy()

  # Obtém o comentário {com}:
  id_com = cmd_args['comentario'] if 'comentario' in cmd_args else None
  if 'comentario' == None:
    erros.append("O identificador do comentário não foi especificado")
    com = None
  else:
    com = obj_comentario.obtem_objeto(id_com)
    if com == None:
      erros.append(f"O comentário {id_com} não existe")
  
  if com == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_ver_comentario.gera(ses, com, erros)
  return pag
