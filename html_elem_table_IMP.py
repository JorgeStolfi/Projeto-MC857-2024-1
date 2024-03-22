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
    
    # O seguinte loop esta sendo removido porque o objeto linhas nao esta vindo como uma lista (como deveria)
    # Mas sim como um bloco html so. Quando isso for corrigido o for deve ser retomado
    # for el in lin:
    #   ht_el = "<td>" + el + "</td>\n"
    #   ht_lin += ht_el

    # Quando o problema acima for corrigido as duas linhas abaixo devem ser apagadas.
    ht_el = "<td>" + lin + "</td>\n"
    ht_lin += ht_el
    
    ht_lin += "</tr>\n"
    ht_tab += ht_lin
  ht_tab += "</table>"
  return ht_tab
