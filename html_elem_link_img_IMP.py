import html_elem_img

def gera(arquivo, descr, alt_px, url):
  ht_img_crua = html_elem_img.gera(arquivo, descr, alt_px)
  if url == None:
    url = arquivo if arquivo != None else "imagens/cinza.png"
  ht_img = "<a href=\"" + url + "\" border=0px>" + ht_img_crua + "</a>"
  return ht_img

