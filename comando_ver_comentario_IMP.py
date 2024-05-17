import html_pag_ver_comentario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_comentario

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []

  # Obtém o comentário {com}:
  com_id = cmd_args.pop('comentario')
  if com_id == None:
    erros.append("O identificador do comentário não foi especificado")
    com = None
  else:
    com = obj_comentario.obtem_objeto(com_id)
    if com == None:
      erros.append(f"O comentário \"{com_id}\" não existe")
      
  assert len(cmd_args) == 0, f"Argumentos espúrios \"{cmd_args}\""
  
  if com == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_ver_comentario.gera(ses, com, erros)
  return pag
