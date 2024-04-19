import obj_sessao
import obj_video
import html_pag_generica
import html_pag_alterar_video
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  erros = [].copy()
  erros.append("!!! comando_alterar_video} ainda não foi implementado !!!")
  pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
