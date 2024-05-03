import html_elem_img_IMP

def gera(arquivo, descr, alt_px):  
  """
  Constrói o HTML para um elemento "<img ...>" que mostra a imagem "{arquivo}",
  escalado para altura {alt_px} pixels, e texto alternativo {descr}.
  
  O {arquivo} deve incluir o folder e a extensão (por exemplo,
  "imagens/Foo.png" ou "avatares/avatar_U-00000001.png". Se {arquivo}
  for {None}, mostra "imagens/cinza.png
  """
  return html_elem_img_IMP.gera(arquivo, descr, alt_px)
