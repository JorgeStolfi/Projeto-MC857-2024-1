import html_pag_alterar_video_IMP

def gera(ses, vid_id, atrs_mod, erros):
  """
  Retorna uma página com formulário para alterar os dados
  do vídeo cujo identificador é {vid_id}. 
  
  O parâmetro {ses} deve ser um objeto {obj_sessao.Classe} 
  de uma sessão aberta, diferente de {None}.
  
  O parâmetro {vid_id} deve ser um identificador "V-{NNNNNNNN}" de um
  vídeo existente {vid}.  Se a sessão {ses} não for de administrador,
  o autor deste vídeo deve ser o dono da sessão {ses}.
 
  O parâmetro {atrs_mod} deve ser {None} ou um dicionário que especifica os
  valores iniciais de todos os campos editáveis do formulário, que podem
  ser diferentes dos valores dos atributos atuais do vídeo {vid}.
  
  Vários atributos do vídeo não podem ser alterados, nem mesmo pelo
  administrador. Os valores desses atributos bem como o indentificador
  do vídeo, serão mostrados mas como campos "readonly". Se especificados
  em {atrs_mod}, devem ser iguais aos valores atuais no comentário {com}.
  
  O parâmetro {erros} deve ser {None} ou uma lista de mensagens (strings)
  a incluir na página.

  O formulário em si será gerado por {html_form_alterar_video.gera}.

  A página terá um botão "Submeter", "Salvar", "Confirmar" ou
  equivalente, que, quand
  clicado, emitirá o comando "alterar_video". Os
  argumentos serão o identificador do vídeo (com chave 'video') e os
  atributos editáveis com os valores que constam do formulário. A página
  também terá um botão simples "Cancelar", que, quando clicado, emite o
  comando 'pag_principal'.
  """
  return html_pag_alterar_video_IMP.gera(ses, vid_id, atrs_mod, erros)
