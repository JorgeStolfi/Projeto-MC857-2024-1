import html_form_upload_video_IMP

def gera(atrs_novo, ed_nota):
  """
  Retorna um formulário HTML (um elemento "<form>...</form>" adequado
  para fazer upload de um novo video. O formulário terá campos editáveis
  para o usuário especificar os atributos do vídeo.
  
  O parâmetro {atrs_novo} deve ser {None} ou um dicionário com valores
  iniciais (defaults) para alguns ou todos esses atributos. Deve conter
  obrigatoriamente um campo 'autor'. Não deve especificar atributos que
  são definidos internamente no momento da criação, como 'data',
  'duração', etc., ou o identificador do vídeo.
  
  O formulário terá um botão "Arquivo" ou similar que permite 
  ao usuário escolher o arquivo de vídeo na sua máquina local.
  
  Se o parâmetro booleano {ed_nota} for {True}, o campo 'nota' será
  editável. Caso contrário esse campo será suprimido.
  
  O formulário terá um botão (de tipo 'submit') com texto "Enviar" ou
  equivalente. Quando o usuário clicar nesse botão, será emitido um
  comando POST tipo "multipart" com ação "fazer_upload_video". Os argumentos desse POST
  serão todos os atributos editáveis da classe {obj_video.Classe} que estiverem no
  formulário nesse momento, mais um atributo de chave 'conteudo' cujo valor é a 
  sequência de bytes do arquivo.
  """
  return html_form_upload_video_IMP.gera(atrs_novo, ed_nota)
