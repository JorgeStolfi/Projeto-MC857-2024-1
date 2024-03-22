def gera(linhas, cabecalho=None):
  ht_tab = "<table>\n"

  # Adiciona cabecalho
  if cabecalho != None:
    ht_tab += "<tr>\n"
    for el in cabecalho:
      ht_tab += "<th>" + el + "</th>"
    ht_tab += "</tr>\n"

  # Adiciona linhas de cada coluna
  for lin in linhas:
    ht_lin = "<tr>\n"
    for el in lin:
      ht_el = "<td>" + el + "</td>\n"
      ht_lin += ht_el
    ht_lin += "</tr>\n"
    ht_tab += ht_lin
  ht_tab += "</table>"
  return ht_tab
