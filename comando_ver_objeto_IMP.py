import obj_usuario
import obj_sessao
from util_valida_campo import ErroAtrib

import html_pag_ver_usuario
import html_pag_ver_sessao
import html_pag_ver_video

import html_pag_mensagem_de_erro
import sys

def processa(ses, cmd_args):
  assert obj_sessao.eh_administrador(ses) # O dono da sessão deve ser administrador.
  try:
    if not 'id_objeto' in cmd_args:
      pag = html_pag_mensagem_de_erro.gera(ses, 'É necessário adicionar um ID para pesquisar.')
      return pag

    id_obj = cmd_args['id_objeto']
    if len(id_obj) != 10: raise ErroAtrib("O identificador \"" + id_obj + "\" é inválido")
    
    letra = id_obj[0]
    if letra == "U":
      usr = obj_usuario.busca_por_identificador(id_obj)
      if usr == None: raise ErroAtrib("Não existe usuário com identificador " + id_obj)
      pag = html_pag_ver_usuario.gera(ses, usr, None)
    elif letra == "S":
      ses_indicada = obj_sessao.busca_por_identificador(id_obj)
      if ses_indicada == None: raise ErroAtrib("Não existe sessão com identificador" + id_obj)
      pag = html_pag_ver_sessao.gera(ses, ses_indicada, None)
    elif letra == "V":
      vid_indicada = obj_video.busca_por_identificador(id_obj)
      if vid_indicada == None: raise ErroAtrib("Não existe vídeo com identificador" + id_vid)
      pag = html_pag_ver_video.gera(ses, vid_indicada, None)
    else:
      raise ErroAtrib("Classe de objeto \"" + letra + "\" inválida")
  except ErroAtrib as ex:
    erros = ex.args[0]
    return html_pag_mensagem_de_erro.gera(ses, erros)
  return pag

