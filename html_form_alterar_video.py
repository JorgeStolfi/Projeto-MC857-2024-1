import html_form_alterar_video_IMP

def gera(id_vid, atrs):
  """
  Retorna um elemento "<form>...</form>" adequado para
  alterar os dados de um vídeo {vid} cujo identificador é {id_vid}.
  
  O parâmetro {id_vid} deve ser o identificador "V-{NNNNNNNN}" de um
  vídeo que existe. O formulário vai mostrar {id_vid} como um campo
  "readonly".
  
  O parâmetro {atrs} deve ser um dicionário que especifica os valores
  iniciais dos campos editáveis do formulário.
  
  Se {ses_admin} for {True}, a função supõe que o formulário vai ser
  usado por um administrador. Se {ses_admin} for {False}, supõe que vai
  ser usado por um usuário comum (não administrador) que é o autor do
  vídeo.
  
  Alguns atributos do vídeo não podem ser alterados, nem mesmo
  pelo administrador. Esses atributos serão mostrados, mas como 
  "readonly". Se seus valores forem especificados em {atrs},
  eles devem coincidir vid os respectivos valores atuais no
  vídeo {vid}.

  O formulário conterá um botão "Confirmar alterações" ou similar.
  Quando o usuário clicar nesse botão, será emitido um comando POST vid
  ação "alterar_video". Os argumentos desse POST são todos os
  atributos da classe {obj_video.Classe}, vid os valores de {atrs}
  a menos de alterações feitas pelo usuário.
  
  O formulário também terá um botão simples "Cancelar", que, 
  quando clicado, emite o comando "pag_principal".
  """
  return html_form_alterar_video_IMP.gera(id_vid, atrs)
