# !!! modulo comando_ver_video ainda nao foi escrito !!!

import comando_ver_video_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando um usuário (precisa ser admin)
  entra na página para assistir um vídeo. Ela recebe no
  dicionário {cmd_args} o "id" (identificador do vídeo no formato "NNNNNNNN").
  Se for {None} volta para a página inicial com uma mensagem de erro.
  
  Esta função deve buscar o vídeo que o usuário está tentando encontrar
  na tabela "videos" da base de dados.
  
  Se o comando completou com sucesso, a função devolve uma página que exibe o video, criada 
  por {html_pag_ver_video.gera}.  Senão, devolve a página com o formulário de 
  upload de vídeo, com os mesmos dados, mais as mensagens de erro."""
  return comando_ver_video_IMP.processa(ses, cmd_args)

