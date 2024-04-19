import comando_ver_video_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP "ver_video".
  Esse comando é tipicamente emitido quando um usuário (mesmo não logado)
  quer examinar dados de um vídeo, incluindo assistir o dito cujo.
  
  O parâmetro {ses} é a sessão de login que emitiu o comando. Deve ser
  {None} (se quem pediu não está logado), ou uma objeto de tipo
  {obj_sessao.Classe}, atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com um único campo
  com chave 'video', cujo valor é o identificador do vídeo (um string
  no formato "V-{NNNNNNNN}").
  
  Normalmente a função devolve uma página que exibe o video, criada por
  {html_pag_ver_video.gera}. A página pode ter botões para alterar os
  dados do usuário, e buscar vídeos, sessões, e comentários do usuário.
  
  Se o comando falhou (por exemplo, se o campo {cmd_args['video']} está
  faltando ou é {None}, ou o vídeo indicado não existe), devolve a
  página principal do site com uma mensagem de erro.
  """
  return comando_ver_video_IMP.processa(ses, cmd_args)

