
import html_elem_button_submit_IMP

def gera(texto, URL, cmd_args, cor_fundo):
  """Função que gera um botões "<input type=submit>" com o {texto} 
  e a {cor_fundo} especificados, para uso dentro de um formulário HTML "<form>...</form>".  
  
  Quando clicado, o botão emite um comando HTTP 'POST' para o {URL} dado, com as
  informações contidas nesse momento nos campos do formulário.
  O URL quase sempre é o nome de um comando do site sem o prefixo "comando_",
  por exemplo "buscar_videos".
  
  Se {cmd_args} não for {None}, deve ser um dicionário cujas chaves e
  valores são acrescentadas como campos 'hidden' junto ao 
  botão propriamente dito.  Por enquanto, cada chave
  pode usar apenas os caracteres [_A-Za-z0-9].
  
  O botão terá letras e moldura pretas com fundo da {cor_fundo}
  especificada.  Se {cor_fundo} for {None}, escolhe uma cor
  com base no {texto}.  Vide {html_estilo_button.escolhe_cor_fundo}."""
  return html_elem_button_submit_IMP.gera(texto, URL, cmd_args, cor_fundo)
