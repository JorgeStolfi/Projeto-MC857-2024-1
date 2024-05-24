import html_pag_mensagem_de_erro
import html_pag_ver_comentario
import html_pag_ver_video
import obj_comentario
import obj_sessao
import obj_video
import obj_usuario

crec_debug = False  # Deve imprimir mensagens para depuração?

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  cmd_args = cmd_args.copy() # Para não alterar o original.
  erros = [] # Mensagens de erro.

  ses_dono = None
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. Precisa estar logado para executar este comando")
  else:
    # Obtem o dono da sessão corrente:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono is not None
    
  para_admin = obj_usuario.eh_administrador(ses_dono) if ses_dono != None else False
  if not para_admin:
    erros.append("Você não tem permissão para executar esta ação")

  # Obtém o id {com_id} do comentário {com} ou o id {vid_id} do video {vid} a alterar,
  # e elimina 'comentario' ou 'video' de {cmd_args}:
  com_id = cmd_args.pop('comentario', None)
  vid_id = cmd_args.pop('video', None)

  pag = None
  if len(erros) == 0:
    if com_id != None:
      com = obj_comentario.obtem_objeto(com_id)
      if com == None:
        erros.append(f"O comentário {com_id} não existe")
      else:
        nota = obj_comentario.recalcula_nota(com)
        obj_comentario.muda_atributos(com, {'nota': nota})
        pag = html_pag_ver_comentario.gera(ses, com, None)
    elif vid_id != None:
      vid = obj_video.obtem_objeto(vid_id)
      if vid == None:
        erros.append(f"O vídeo {vid_id} não existe")
      else:
        nota = obj_comentario.recalcula_nota(vid)
        obj_video.muda_atributos(vid, {'nota': nota})
        pag = html_pag_ver_video.gera(ses, vid, None)
 
  if pag == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    assert len(erros) == 0

  return pag
