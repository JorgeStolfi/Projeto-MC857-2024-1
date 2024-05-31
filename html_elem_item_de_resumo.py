import html_elem_item_de_resumo_IMP

def gera(texto, cab, cor_fundo, alinha, cor_texto, tam_fonte="20px"):
  """
  Retorna um string que é um fragmento HTML consistindo to string {texto},
  formatado com estilo adequado para um item de uma linha de resumo,
  como {html_linha_resumo_de_usuario.gera}, {html_linha_resumo_de_video.gera}, etc.
  
  Se {cab} é {True}, supõe que o {texto} é um cabeçalho de coluna, e usa
  cores de texto e fundo padronizados para esse fim. 
  
  Se {cab} é false, supõe que o {texto} é um atributo de objeto, que
  será mostrado com a cor {cor_texto} (ou preto se {cor_texto} é {None})
  e o fundo da {cor_fundo} (ou transparente se {cor_fundo} for {None}).
  
  O parâmetro {alinha} especifica o alinhamento horizontal do texto na coluna. Deve ser
  "left", "center",ou "right".

  O parâmetro opcional {tam_fonte} especifica o tamanho da fonte do texto. Deve ser
  uma string, no formato "{tamanho}px", onde {tamanho} é um número de pixels.
  O valor padrão de {tam_fonte} é "20px". 
  
  Mais precisamente o resultado é um elemento '<span style="{estilo}">{texto}</span>'
  com o {estilo} apropriado.
  
  O texto deve ser uma única linha e não muito extenso.  Quem chama esta 
  função deve cuidar para que estas restrições sejam satisfeitas. 
  """
  return html_elem_item_de_resumo_IMP.gera(texto, cab, cor_fundo, alinha, cor_texto, tam_fonte)
