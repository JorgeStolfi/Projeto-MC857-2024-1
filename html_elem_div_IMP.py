def gera(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<div" + est + ">" + conteudo + "</div>"
  return html
