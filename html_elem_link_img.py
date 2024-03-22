import html_elem_link_img_IMP 

def gera(nome, alt, tam, url):
  """Constrói o HTML para um link "<a ...><img ...></a>"
  que mostra a imagem "imagens/{nome}" com altura {tam} 
  e texto alternativo {alt}.  Quando o usuário clica na imagem, é emitido
  um comando HTTP GET com o {url} dado."""
  return html_elem_link_img_IMP.gera(nome, alt, tam, url)
