import html_pag_mensagem_de_erro
import html_pag_ver_comentario
import html_pag_ver_video
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video
import util_dict
from util_erros import ErroAtrib

import sys

crec_debug = False  # Deve imprimir mensagens para depuração?

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):

  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  cmd_args = cmd_args.copy() # Para não alterar o original.
  erros = [] # Mensagens de erro.

  ses_dono = None
  para_admin = False
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. Precisa estar logado para executar este comando")
  else:
    # Obtem o dono da sessão corrente:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono is not None
    para_admin = obj_usuario.eh_administrador(ses_dono)

  # Obtém o comentário {com} a alterar, e elimina 'comentario' de {cmd_args}:
  com_id = cmd_args.pop('comentario', None)
  vid_id = cmd_args.pop('video', None)

  erros.append("!!! O módulo {comando_recalcular_nota} ainda não foi implementado !!!\n")

  if len(erros) == 0:
    assert false, "!!! implementar !!!"
    pag = None
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)

  return pag
