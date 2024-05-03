import html_elem_item_de_resumo_IMP

def gera(texto, cab, cor_fundo, alinha):
  """
  Retorna um string que é um fragmento HTML consistindo to string {texto},
  formatado com estilo adequado para um item de uma linha de resumo,
  como {html_linha_resumo_de_usuario.gera}, {html_linha_resumo_de_video.gera}, etc.
  
  Se {cab} é {True}, supõe que o {texto} é um cabeçalho de coluna, e usa
  cores de texto e fundo padronizados para esse fim. 
  
  Se {cab} é false, supõe que o {texto} é um atributo de objeto, que
  será mostrado com o fundo da {cor_fundo} indicada (ou transparente se
  {cor_fundo} for {None}).
  
  O parâmetro {alinha} especifica o alinhamento horizontal do texto na coluna. Deve ser
  "left", "center",ou "right".
  
  Mais precisamente o resultado é um elemento '<span style="{estilo}">{texto}</span>'
  com o {estilo} apropriado.
  """
  return html_elem_item_de_resumo_IMP.gera(texto, cab, cor_fundo, alinha)
