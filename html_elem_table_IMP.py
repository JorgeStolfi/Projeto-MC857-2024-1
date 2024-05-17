import sys

def gera(linhas, estilo):

  if estilo != None:
    ht_tabela = f"<table style=\"{estilo}\">\n"
  else:
    ht_tabela = "<table>\n"

  # Adiciona linhas:
  for lin in linhas:
    assert len(lin) > 0, "linha de tabela não pode ser vazia"

    # Adiciona os elementos da linha
    ht_elems = ""
    for el in lin:
      ht_elems += "    " + el + "\n"
    ht_linha = "  <tr>\n" + ht_elems + "  </tr>\n"

    ht_tabela += ht_linha
  ht_tabela += "</table>"
  return ht_tabela
