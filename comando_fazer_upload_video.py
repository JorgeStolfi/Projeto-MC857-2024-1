import comando_fazer_upload_video_IMP

def processa(ses, dados):
  """Esta função é chamada quando o usuário (que não deve estar cadastrado) 
  aperta o botão "Upload" no formulário de upload de video.  Ela recebe no
  dicionário {dados} os campos 'arq' e 'titulo' com os dados que o usuário preencheu
  nesse formulário. Deve processar o upload do arquivo e criar um novo objeto 
  vídeo com esses dados, registrando na tabela "videos" da base de dados.  A função deve  
  devolver a página de entrada."""
  return comando_fazer_upload_video_IMP.processa(ses, dados)
