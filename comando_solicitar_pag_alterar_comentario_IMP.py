import html_pag_alterar_comentario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_comentario
from util_erros import erro_prog

def processa(ses, cmd_args):
  erros = [ ].copy()
  erros.append("!!! O comando 'solicitar_pag_alterar_comentario' ainda não foi implementado !!!")

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    id_com = cmd_args['comentario'] if 'comentario' in cmd_args else None
    pag = html_pag_alterar_comentario.gera(ses, id_com, {}, None)
  return pag
    
