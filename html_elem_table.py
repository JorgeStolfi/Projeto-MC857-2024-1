import html_elem_table_IMP

def gera(linhas):
  """Gera o HTML para uma tabela "<table>...</table>".
  
  O parâmetro {linhas} deve ser uma lista/tupla de listas/tuplas
  que descreve as linhas da tabela. Cada elemento {linhas[i]} de {linhas} 
  deve ser uma lista/tupla não vazia que descreve a linha {i} da tabela. 
  Cada elemento {linha[i][j]} deve ser um fragmento HTML, que é inserido 
  nas células da linha {i}, coluna {j} da tabela.  Cada um destes fragmentos deve
  estar envolvido em um elemento HTML "<td ...>....</td>".
  
  Esta função providencia os marcadores "<table>...</table>" e "<tr>..</tr>"."""
  return html_elem_table_IMP.gera(linhas)
