
def gera(cor_texto):
  fam_fonte = "Courier"
  peso_fonte = "bold"
  tam_fonte = "24px"

  estilo = \
    " color: " + cor_texto + ";" + \
    " font-family:" + fam_fonte + ";" + \
    " font-weight:" + peso_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    " padding: 0px 10px 0px 0px;"
  return estilo
