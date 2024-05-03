import html_elem_link_img_IMP 

def gera(arquivo, descr, alt_px, url):
  """
  Constrói o HTML para um link "<a ...><img ...></a>" que mostra o
  arquivo de imagem "{arquivo}", escalada para ter altura {alt_px}
  pixels, e texto alternativo {descr}.
  
  O {arquivo} deve incluir o folder e a extensão (por exemplo, "imagens/Foo.png"
  ou "avatares/avatar_U-00000001.png".
  
  Quando o usuário clica na imagem, é emitido
  um comando HTTP GET com o {url} dado.  Se o {url} for {None},
  usa o próprio {arquivo}.
  """
  return html_elem_link_img_IMP.gera(arquivo, descr, alt_px, url)
