# Implementação do módulo {comando_solicitar_pag_upload_video}. 

import html_pag_upload_video

def processa(ses, cmd_args):
  pag = html_pag_upload_video.gera(ses, None)
  return pag
    
