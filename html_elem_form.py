import html_elem_form_IMP

def gera(conteudo, multipart):
  """
  Retorna um string que é o fragmento HTML "<form>{conteudo}</form>".
  
  O {conteudo} deve ser um fragmento de HTML com os elementos "<input>"
  necessários, e pelo menos um botão de tipo submit (veja
  {html_elem_button_submit.gera}). Quando esse botão é acionado, o
  browser emite um comando HTTP com com os valores corrented de todos os
  elementos "<input>" -- editáveis, readonly, ou hidden. 
  
  Se {mutipart} for {False}, o comando emitido será um "GET" com enctype
  default ("application/x-www-form-urlencoded") e URL
  "http://{servidor}/{cmd}?{chave1}={valor1}&{chave2}={valor2}..." onde
  {cmd} é o comando associado ao botão.
  
  Se {multipart} for {True}, o comando emitido será um "POST" com enctype
  
  Note que um elemento "<form>" não pode ocorrer dentro de um parágrafo.
  """
  return html_elem_form_IMP.gera(conteudo, multipart)
