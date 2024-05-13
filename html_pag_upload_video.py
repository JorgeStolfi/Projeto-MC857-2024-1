import html_pag_upload_video_IMP

def gera(ses, atrs, erros):
  """
  Retorna uma página HTML contendo um formulário para fazer upload de
  um video. O formulário terá campos editáveis onde o usuário que pediu
  a página deverá digitar o nome do arquivo (a escolher na máquina do
  usuário) e o título do arquivo.

  O parâmetro {ses} é a sessão de login que pediu esta página.
  Deve ser um objeto de tipo {obj_sessao.Classe}, atualmente aberta.
  Não pode ser {None}.
  
  Se {atrs} não for {None}, deve ser um dicionário que define valores
  iniciais (default) para alguns ou todos os atributos do novo vídeo.
  Não deve incluir 'conteudo' nem atributos que são definidos
  internamente quando o vídeo é armazenado, como 'data', 'duracao',
  'altura', e 'largura'.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens de erro
  a mostrar na página.  

  A página terá também um botão 'Enviar' (de tipo 'submit').Quando o
  usuário clicar no botão 'Enviar', será emitido um comando POST com
  ação {fazer_upload_video}. Os argumentos desse POST serão 'autor' (o
  ID do usuário que vez o upload), 'titulo' (o título) e 'conteudo' (os
  bytes do arquivo).

  Os parâmetros {atrs} e {erros} são usados quando tentativa de fazer
  upload dá erro, e a pagina precisa ser exibida de novo com os valores
  dos campos que o usuário preencheu nessa tentativa. Neste caso, {erros}
  deve ser a lista das mensagens que explicam porque a tentativa falhou.
  """
  return html_pag_upload_video_IMP.gera(ses, atrs, erros)
