import html_pag_mensagem_de_erro_IMP

def gera(ses, erros):
  """Retorna uma página de erro com as mensagens {erros},
  que pode ser um string ou uma lista de strings, não vazia.

  A página terá um botão "OK" que, quando clicado, gera um comando
  "GET" com URL "pag_principal"."""
  return html_pag_mensagem_de_erro_IMP.gera(ses, erros)
