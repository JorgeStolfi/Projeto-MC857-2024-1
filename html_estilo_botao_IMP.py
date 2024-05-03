
def gera(cor_fundo):
  fam_fonte = "Courier"
  peso_fonte = "Bold"
  tam_fonte = "18px"
  estilo = \
    " color: #000000; " + \
    " font-family:" + fam_fonte + ";" + \
    " font-weight:" + peso_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    " background:" + cor_fundo + ";" + \
    " padding: 2px 5px 2px 5px; " + \
    " border-radius: 5px; " + \
    " transition: all 0.4s ease 0s;"
  return estilo
