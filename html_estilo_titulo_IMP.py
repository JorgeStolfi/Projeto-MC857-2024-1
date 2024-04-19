
def gera():
  fam_fonte = "Courier"
  peso_fonte = "bold"
  tam_fonte = "24px"
  cor_texto = "#000000"

  cor_fundo = None

  estilo = \
    " color: " + cor_texto + ";" + \
    " font-family:" + fam_fonte + ";" + \
    " font-weight:" + peso_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    ( (" background:" + cor_fundo + ";") if cor_fundo != None else "") + \
    " padding: 0px 10px 0px 0px;"
  return estilo
