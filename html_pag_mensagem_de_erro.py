import html_pag_mensagem_de_erro_IMP

def gera(ses, erros):
  """Retorna uma página de erro com a mensagem de erro {erros}.  O parâmetro
  {erros} pode ser um string ou uma lista de strings.

  A página terá um botão "OK" que, quando clicado, gera um comando
  "GET" com URL "principal"."""
  return html_pag_mensagem_de_erro_IMP.gera(ses, erros)
