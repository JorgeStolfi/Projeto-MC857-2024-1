# Implementação do módulo {comando_solicitar_pag_upload_video}. 

import html_pag_upload_video
import obj_sessao

def processa(ses, cmd_args):

  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []
  
  assert len(cmd_args) == 0, f"Argumentos espúrios \"{cmd_args}\""
   
  if len(erros) > 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_upload_video.gera(ses, {}, None)

  return pag
