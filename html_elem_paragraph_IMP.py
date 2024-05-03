
def gera(estilo, conteudo):
  ht_est = (" style=\"" + estilo + "\"" if estilo != None and estilo != "" else "")
  html = "<p" + ht_est + ">" + conteudo + "</p>\n"
  return html
