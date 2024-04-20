import html_form_postar_comentario_IMP

def gera(atrs):
  """
  Retorna um elemento "<form>...</form>" adequado para criar um novo
  comentário. O formulário contém campos editáveis para o usuário
  especificar os atributos do mesmo.
  
  O parâmetro {atrs} especifica os valores dos campos não-editáveis 
  ('autor', 'video', 'pai') e o valor inicial dos editáveis ('texto').
  Não deve especificar a 'data'.
  
  O formulário conterá um botão (de tipo 'submit') com texto "Enviar".
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  "fazer_postar_comentario".  Os argumentos desse POST serão os atributos
  'autor', 'video', 'pai', e 'texto', este último com as edições
  do usuário.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'pag_principal'.
  """
  return html_form_postar_comentario_IMP.gera(atrs)