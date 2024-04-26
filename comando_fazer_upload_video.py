import comando_fazer_upload_video_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando um usuário (que deve estar cadastrado)
  aperta o botão "Upload" ou equivalente no formulário de upload de
  video. 
  
  O parâmetro {ses} será a sessão de login corrente. Não pode ser {None}
  e deve ser um objeto de tipo {obj_sessao.Classe}, ainda aberto.
  
  O parâmetro {cmd_args} será um dict com os argumentos do comando HTTP,
  ou seja os dados que o usuário preencheu nesse formulário.
  Especificamente, incluem o título do vídeo (com chave 'titulo'), o ID do
  usuário que é autor do vídeo (com chave 'autor'), e o conteúdo do
  arquivo carregado, com chave 'arquivo'.
  
  O autor deve ser o dono da sessão {ses}. O título deve ser um string
  que satisfaz certas restrições; veja {util_valida_campo.titulo_de_video}. 
  O arquivo deve ser uma sequência de bytes binários, supostamente um 
  vídeo codificado no formato MPEG-4.
  
  Se tudo correr bem, o identificador do vídeo será "V-{NNNNNNNN}" onde
  {NNNNNNNN} é o número de vídeos já inseridos, mais um. Esta função vai
  gravar o conteúdo do vídeo no arquivo "videos/{id_vid}.mp4" e criar o
  novo objeto de tipo {obv_video.Classse} correspondente, registrando o
  mesmo na tabela "videos" da base de dados. A data de upload (atributo
  'data') será a data corrente.
  
  Se o comando completou com sucesso, a função devolve uma página que exibe o video, criada 
  por {html_pag_ver_video.gera}.  Senão, devolve a página com o formulário de 
  upload de vídeo, com os mesmos dados, mais as mensagens de erro.
  """
  return comando_fazer_upload_video_IMP.processa(ses, cmd_args)
