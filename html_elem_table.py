import html_elem_table_IMP

def gera(linhas, cabecalho):
  """Gera o HTML para uma tabela "<table>...</table>".
  
  O parâmetro {linhas} deve ser uma lista ou tupla cujos elementos descrevem as linhas.
  Cada elemento de {linhas} deve ser uma list ou tupla de fragmentos HTML, que são 
  inseridos nas células da linha correspondente da tabela.
  O parâmetro {cabecalho} deve ser uma lista com o título de cada coluna da tabela."""
  return html_elem_table_IMP.gera(linhas, cabecalho)
