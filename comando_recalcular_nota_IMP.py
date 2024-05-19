import html_pag_mensagem_de_erro
import html_pag_ver_comentario
import html_pag_ver_video
import obj_comentario
import obj_sessao
import obj_video

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

  # Obtém o id {com_id} do comentário {com} ou o id {vid_id} do video {vid} a alterar,
  # e elimina 'comentario' ou 'video' de {cmd_args}:
  com_id = cmd_args.pop('comentario', None)
  vid_id = cmd_args.pop('video', None)

  if len(erros) == 0:
    if com_id:
      nota = obj_comentario.recalcula_nota(com_id)
      obj_comentario.muda_atributos(com_id, {'nota': nota})
      com = obj_comentario.obtem_objeto(com_id)
      pag = html_pag_ver_comentario.gera(ses, com, None)
    elif vid_id:
      nota = obj_video.recalcula_nota(vid_id)
      obj_video.muda_atributos(vid_id, {'nota': nota})
      vid = obj_video.obtem_objeto(vid_id)
      pag = html_pag_ver_video.gera(ses, vid, None)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)

  return pag
