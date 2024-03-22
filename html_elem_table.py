import html_elem_table_IMP

def gera(linhas, cabecalho):
  """Gera o HTML para uma tabela "<table>...</table>".
  
  O parâmetro {linhas} deve ser uma lista/tupla de listas/tuplas
  que descreve as linhas da tabela. Cada elemento {linhas[i]} de {linhas} 
  deve ser uma lista/tupla que descreve a linha {i} da tabela. 
  Cada elemento {linha[i][j]} deve ser um fragmento HTML, que é inserido 
  nas células da linha {i}, coluna {j} da tabela.
  
  O parâmetro {cabecalho}, se não for {None},
  deve ser uma lista/tupla que descreve o cabeçalho da tabela.
  Cada elemento {cabecalho[j]} deve ser um fragmento HTML que 
  descreve o cabeçalho da coluna {j} da tabela.
  
  A função providencia os marcadores "<table>...</table>", "<tr>..</tr>",
  e "<td>..</td>."""
  return html_elem_table_IMP.gera(linhas, cabecalho)
