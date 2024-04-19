import html_form_upload_video_IMP

def gera(id_autor, atrs):
  """Retorna um elemento "<form>...</form>" adequado para 
  fazer upload de um novo video do usuário {id_autor}.
  
  O formulário contém campos editáveis para o usuário
  especificar os atributos do vídeo.
  
  O formulário conterá um botão (de tipo 'submit') com texto "Enviar".
  Quando o usuário clicar nesse botão, será emitido um comando POST com ação
  "fazer_upload_video".  Os argumentos desse POST são todos os atributos da classe
  {obj_video.Classe}.

  O formulário também terá um botão simples 'Cancelar',
  que, quando clicado, emite o comando 'pag_principal'."""
  return html_form_upload_video_IMP.gera(id_autor, atrs)
