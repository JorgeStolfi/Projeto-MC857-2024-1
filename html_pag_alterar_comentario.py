import html_pag_alterar_comentario_IMP

def gera(ses, id_com, atrs, erros):
  """
  Retorna uma página com formulário para alterar os dados
  do comentário cujo identificador é {id_com}. 
  
  O parâmetro {ses} deve ser um objeto {obj_sessao.Classe} 
  de uma sessão aberta, diferente de {None}.
  
  O parâmetro {id_com} deve ser um identificador "V-{NNNNNNNN}" de um
  comentário existente {com}.  Se a sessão {ses} não for de administrador,
  o autor deste comentário deve ser o dono da sessão {ses}.
 
  O parâmetro {atrs} deve ser {None} ou um dicionário que especifica os
  valores iniciais de todos os campos editáveis do formulário, que podem ser
  diferentes dos valores dos atributos atuais do comentário {com}.
  
  Vários atributos do comentário não podem ser alterados, nem mesmo pelo
  administrador. Os valores desses atributos bem como o indentificador
  do comentário, serão mostrados mas como campos "readonly". Se
  especificados em {atrs}, devem ser iguais aos valores atuais no
  comentário {com}.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens (strings)
  a incluir na página.

  O formulário em si será gerado por {html_form_alterar_comentario.gera}.
  Ele conterá um botão "Confirmar alterações" ou similar (de tipo 'submit').
  Quando o comentário clicar nesse botão, será emitido um comando POST com ação
  "alterar_comentario".  Os argumentos desse POST são todos os atributos da classe
  {obj_comentario.Classe}, com os valores de {atrs} a menos de alterações feitas pelo
  usuário.

  A página terá botôes que permitem buscar as respostas ao comentário {com}
  e examinar o vídeo associado. A página também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'pag_principal'.
  """
  return html_pag_alterar_comentario_IMP.gera(ses, id_com, atrs, erros)
