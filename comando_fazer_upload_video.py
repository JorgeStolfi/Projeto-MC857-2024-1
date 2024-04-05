import comando_fazer_upload_video_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando um usuário (que deve estar cadastrado) 
  aperta o botão "Upload" no formulário de upload de video. Ela recebe no
  dicionário {cmd_args} os dados que o usuário preencheu
  nesse formulário, especificamente o nome 'arq' do vídeo
  e o 'titulo'; bem como o conteúdo do arquivo.
  
  Esta função gravar o conteúdo do vídeo no arquivo "videos/{arq}" 
  e c criar o novo objeto vídeo correspondente, registrando na tabela "videos" 
  da base de dados. A data de upload (atributo 'data') será a data corrente, 
  e o 'autor' será o dono da sessão corrente {ses} (que não deve ser {None} e
  deve estar aberta).
  
  Se o comando completou com sucesso, a função devolve uma página que exibe o video, criada 
  por {html_pag_ver_video.gera}.  Senão, devolve a página com o formulário de 
  upload de vídeo, com os mesmos dados, mais as mensagens de erro."""
  return comando_fazer_upload_video_IMP.processa(ses, cmd_args)
