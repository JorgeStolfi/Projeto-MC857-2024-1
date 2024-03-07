
import html_elem_button_submit_IMP

def gera(texto, URL, args, cor_fundo):
  """Função que gera um botões "<input type=submit>" com o {texto} 
  e a {cor_fundo} especificados, para uso dentro de um formulário HTML "<form>...</form>".  
  
  Quando clicado, o botão emite um comando HTTP 'POST' para o {URL} dado, com as
  informações contidas nesse momento nos campos do formulário.
  
  Se {args} não for {None}, deve ser um dicionário cujas chaves e
  valores são acrescentadas como campos 'hidden' junto ao 
  botão propriamente dito. Por enquanto, as chaves e
  valores devem ser cadeias só com letras ASCII, dígitos, pontos,
  hífens, e underscores."""
  return html_elem_button_submit_IMP.gera(texto, URL, args, cor_fundo)
