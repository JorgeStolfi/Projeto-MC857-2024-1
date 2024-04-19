# Implementação do módulo {comando_solicitar_pag_upload_video}. 

import html_pag_upload_video
import obj_sessao

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  assert cmd_args == {}, "Argumentos espúrios"

  pag = html_pag_upload_video.gera(ses, {}, None)
  return pag
