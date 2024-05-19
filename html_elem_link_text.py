import html_elem_link_text_IMP 

def gera(texto, url, cmd_args):
  """
  Constrói o HTML para um link "<a href=\...></a>" que mostra o
  texto sublinhado {texto} e gera para esse texto o link correspondente {url},
  a partir da montagem do comando HTTP com o {cmd_args}.
  
  Quando o usuário clica no link, é emitido
  um comando HTTP GET com o {url} dado.
  """
  return html_elem_link_text_IMP.gera(texto, url, cmd_args)
