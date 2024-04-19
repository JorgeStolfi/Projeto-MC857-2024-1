import obj_sessao
import html_bloco_lista_de_sessoes
import html_pag_generica
import html_pag_buscar_sessoes
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  erros = [].copy()
  erros.append("!!! comando_buscar_sessoes} ainda não foi implementado !!!")
  pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
