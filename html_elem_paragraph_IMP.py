
def gera(estilo, conteudo):
  est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<p" + est + ">" + conteudo + "</p>\n"
  return html
