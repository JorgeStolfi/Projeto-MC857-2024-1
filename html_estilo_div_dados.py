import html_estilo_div_dados_IMP

def gera(display, width, word_wrap, padding, line_height):
  """Retorna um fragmento de CSS para uso no atributo "style" 
  de um texto genperico, por exemplo mensagem de erro,
  título de vídeo, texto de comentário, etc.
  
  O parâmetro {display} define se um elemento é tratado como um bloco 
  ou elemento inline, como  no atributo CSS "display:" por exemplo "block".
  
  O parâmetro {width} determina a largura da área de conteúdo de um elemento, 
  como no atributo CSS "width:" por exemplo "600px".
  
  O parâmetro {word_wrap} é utilizado para especificar se o navegador pode 
  ou não quebrar linhas dentro das palavras, como  no atributo CSS "word-wrap:" 
  por exemplo "break-word".

  O parâmetro {padding} é uma lista de 4 strings que definem uma distância entre 
  o conteúdo de um elemento e suas bordas, por exemplo {( "10px", "0px", "5px", "0px" )}.

  O parâmetro {line_height} permite controlar o espaçamento entre as linhas de 
  um texto, como  no atributo CSS "line-height:" por exemplo "85%".
  """
  return html_estilo_div_dados_IMP.gera(display, width, word_wrap, padding, line_height)
