# Implementação do módulo {comando_solicitar_pag_buscar_comentarios}.

import html_pag_buscar_comentarios
import obj_sessao

def processa(ses, cmd_args):
  # Estas condições deveriam valer para comandos gerados
  # pelas páginas do site:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  pag = html_pag_buscar_comentarios.gera(ses, {}, None)
  return pag
