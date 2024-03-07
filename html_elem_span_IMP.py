def gera(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  ctd = (conteudo if conteudo != None else "")
  html = "<span" + est + ">" + str(ctd) + "</span>"
  return html
