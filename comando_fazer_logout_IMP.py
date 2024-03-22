# Implementação do módulo {comando_fazer_logout}.

import html_pag_principal
import html_pag_mensagem_de_erro
import obj_sessao

def processa(ses, cmd_args):
  if ses == None or not obj_sessao.aberta(ses):
    # Isto nunca deveria acontecer, mas em todo caso:
    pag = html_pag_mensagem_de_erro.gera(ses, "Precisa entrar no site antes de sair")
    ses_nova = ses
  else:
    obj_sessao.fecha(ses)
    ses_nova = None
    pag = html_pag_principal.gera(ses_nova, None)
  return pag, ses_nova
