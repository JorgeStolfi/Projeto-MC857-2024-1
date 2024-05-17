import html_bloco_video_IMP

def gera(vid, bt_alterar, bt_conversa, bt_comentar):
  """
  Retorna um fragmento HTML que exibe dados do video {vid}
  (não editáveis) e o vídeo em si.
  
  O parâmetro {vid} deve ser um objeto de tipo {obj_video.Classe}.
  Não pode ser {None}.
  
  O título e o identificador do vídeo NÃO são exibidos.  Quem chama
  esta função deve cuidar de exibí-los da maneira apropriada.

  Os parâmetros booleanos {bt_alterar}, {bt_conversa} e {bt_comentar}
  especificam botões que podem ser acrescentados opcionalmente em baixo
  dos dados:
  
    * Se {bt_alterar} é {True}, inclui um botão "Editar" ou equivalente,
    que emite o comando "solicitar_pag_alterar_video" para alterar o título
    ou outros atributos mutáveis do vídeo.
  
    * Se {bt_conversa} é {True}, inclui um botão "Comentários" ou equivalente,
    que emite o comando "ver_conversa" para exibir a árvore de comentários
    e respostas associadas a este vídeo.
  
    * Se {bt_comentar} é {True}, inclui um botão "Comentar" ou equivalente,
    que emite o comando "solicitar_pag_postar_comentario" para acrescentar 
    um comentário ao vídeo.
    
  Em todos estes comandos, os argumentos serão {{ 'video': vid_id }} onde
  {vid_id} é o identificador do vídeo {vid}.
  """
  return html_bloco_video_IMP.gera(vid, bt_alterar, bt_conversa, bt_comentar)
