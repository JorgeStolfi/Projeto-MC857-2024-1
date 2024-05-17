# Implementação do módulo {comando_fazer_logout}.

import html_pag_principal
import html_pag_mensagem_de_erro
import obj_sessao

def processa(ses, cmd_args):
  if ses == None:
    pag = html_pag_mensagem_de_erro.gera(ses, "Precisa fazer login no site antes de sair")
    ses_nova = None
  elif not obj_sessao.aberta(ses):
    pag = html_pag_mensagem_de_erro.gera(ses, "Esta sessão de login já foi fechada")
    ses_nova = None
  else:
    obj_sessao.fecha(ses)
    ses_nova = None
    pag = html_pag_principal.gera(ses_nova, None)
  return pag, ses_nova
