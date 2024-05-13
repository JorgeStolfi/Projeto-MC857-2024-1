import html_form_upload_video_IMP

def gera(atrs, para_admin):
  """
  Retorna um formulário HTML (um elemento "<form>...</form>" adequado
  para fazer upload de um novo video. O formulário terá campos editáveis
  para o usuário especificar os atributos do vídeo.
  
  O parâmetro {atrs} deve ser {None} ou um dicionário com valores
  iniciais (defaults) para alguns ou todos esses atributos. Deve conter
  obrigatoriamente um campo 'autor'. Não deve especificar atributos que
  são definidos internamente no momento da criação, como 'data',
  'duração', etc., ou o identificador do vídeo.
  
  Se o parâmetro booleano {para_admin} for {True}, a função supõe que o
  formulário foi pedido por um administrador. Se {para_admin} for
  {False}, supõe que o formulário vai ser usado por um usuário comum
  (não administrador). Este parâmetro atualmente é ignorado, mas no
  futuro pode determinar se certos atributos podem ou não ser
  especificados pelo usuário.
  
  O formulário terá um botão (de tipo 'submit') com texto "Enviar" ou
  equivalente. Quando o usuário clicar nesse botão, será emitido um
  comando POST com ação "fazer_upload_video". Os argumentos desse POST
  são todos os atributos da classe {obj_video.Classe} que estiverem no
  formulário nesse momento.
  """
  return html_form_upload_video_IMP.gera(atrs, para_admin)
