import html_pag_alterar_comentario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
import obj_comentario

def processa(ses, cmd_args):
  
  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and isinstance(cmd_args, dict)
  
  erros = []

  # Obtem o comentário:
  com_id = cmd_args.get('comentario', None)
  if com_id == None:
    erros.append("O comentário a editar não foi especificado!")
    com = None
  else:
    com = obj_comentario.obtem_objeto(com_id)
    if com == None:
      erros.append(f"O comentário {com_id} não existe")
  
  # Valida a sessão do usuário, obtem o dono, verifica permissão:
  ses_dono = None
  pode_alterar = False
  if ses == None:
    erros.append("Não pode editar comentários sem fazer login")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login já foi encerrada")
  elif com != None:
    ses_dono = obj_sessao.obtem_dono(ses)
    ses_admin = obj_usuario.eh_administrador(ses_dono)
    com_autor = obj_comentario.obtem_atributo(com, 'autor')
    assert com_autor != None
    pode_alterar = ses_admin or com_autor == ses_dono
    if not pode_alterar:
      erros.append("Você não tem permissão para editar este comentário")
  
  if len(erros) > 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    # Obtem os atributos atuais do comemtário:
    assert com != None
    com_atrs = obj_comentario.obtem_atributos(com)
    pag = html_pag_alterar_comentario.gera(ses, com, com_atrs, None)
  return pag
    
