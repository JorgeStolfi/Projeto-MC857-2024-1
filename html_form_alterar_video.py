import html_form_alterar_video_IMP

def gera(vid_id, atrs, para_admin):
  """
  Retorna um elemento "<form>...</form>" adequado para
  alterar os dados de um vídeo {vid} cujo identificador é {vid_id}.
  
  O parâmetro {vid_id} deve ser o identificador "V-{NNNNNNNN}" de um
  vídeo que existe. O formulário vai mostrar {vid_id} como um campo
  "readonly".
  
  O formulário terá campos editáveis com os atributos do vídeo. O
  parâmetro {atrs} deve ser um dicionário com um subconjuto
  (possivelmente vazio) das chaves desses atributos. Os valores
  especificados em {atrs} serão mostrados no formulário em vez dos
  valores correntes dos atributos de {vid}.
  
  Se {para_admin} for {True}, a função supõe que o formulário vai ser
  usado por um administrador. Se {para_admin} for {False}, supõe que vai
  ser usado por um usuário comum (não administrador) que é o autor do
  vídeo.
  
  Alguns atributos do vídeo não podem ser alterados, nem mesmo
  pelo administrador. Esses atributos serão mostrados, mas como 
  "readonly". Se seus valores forem especificados em {atrs},
  eles devem coincidir vid os respectivos valores atuais no
  vídeo {vid}.

  O formulário conterá um botão "Alterar", "Confirmar alterações" ou
  similar. Quando o usuário clicar nesse botão, será emitido um comando
  POST vid ação "alterar_video". Os argumentos desse POST são todos os
  atributos da classe {obj_video.Classe}, possivelmente substituidos
  pelos valores em {atrs} e edições feitas pelo dono da sessão.
  
  O formulário também terá um botão simples "Cancelar", que, 
  quando clicado, emite o comando "pag_principal".
  """
  return html_form_alterar_video_IMP.gera(vid_id, atrs, para_admin)
