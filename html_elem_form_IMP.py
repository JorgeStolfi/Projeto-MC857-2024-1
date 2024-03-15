import html_elem_span

def gera(conteudo):
  # define o estilo padrão:
  fam_fonte = "Courier"
  peso_fonte = None
  tam_fonte = "18px"
  estilo = \
    "  display: inline-block;" + \
    "  font-family: " + fam_fonte + ";" + \
    "  font-size: " + tam_fonte + ";" + \
    "  padding: 5px;"
  ht_form = "<form>" + conteudo + "</form>"
  return ht_form
