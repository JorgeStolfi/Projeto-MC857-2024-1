def gera(tam_fonte, peso_fonte, cor_texto, cor_fundo, margens):
  fam_fonte = "Courier"

  estilo = \
    " color: " + cor_texto + ";" + \
    " font-family:" + fam_fonte + ";" + \
    " font-weight:" + peso_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    ( (" background:" + cor_fundo + ";") if cor_fundo != None else "") + \
    ( f" padding: {margens[0]} {margens[1]} {margens[2]} {margens[3]};" if margens != None else "")
  return estilo
