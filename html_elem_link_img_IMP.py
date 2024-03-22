import html_elem_img

def gera(nome, alt, tam, url):
  ht_img_crua = html_elem_img.gera(nome, alt, tam)
  ht_img = "<a href=\"" + url + "\" border=0px>" + ht_img_crua + "</a>"
  return ht_img

