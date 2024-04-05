def gera(estilo, conteudo):
  assert estilo == None or type(estilo) is str
  assert conteudo == None or type(conteudo) is str
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  ctd = (conteudo if conteudo != None else "")
  html = "<span" + est + ">" + ctd + "</span>"
  return html
