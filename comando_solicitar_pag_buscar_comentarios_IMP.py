# Implementação do módulo {comando_solicitar_pag_buscar_comentarios}.

import html_pag_buscar_comentarios
import obj_sessao

def processa(ses, cmd_args):
  # Estas condições deveriam valer para comandos gerados
  # pelas páginas do site:
  assert ses == None or obj_sessao.aberta(ses), "Sessao inválida"
  assert type(cmd_args) is dict and cmd_args == {}, "Argumentos inválidos"
  
  pag = html_pag_buscar_comentarios.gera(ses, {}, None)
  return pag
