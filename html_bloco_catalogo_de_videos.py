import html_bloco_catalogo_de_videos_IMP

def gera(vid_ids, mostra_autor):
  """Retorna um trecho de HTML que descreve os videos cujos identificadores
  estão na lista {vid_ids}.  Cada entrada mostra o vídeo à esquerda e 
  todos os dados à direita, em várias linhas.
  
  Se {mostra_autor} for {True}, a informação ao lado de cada entrada vai incluir o
  autor do vídeo.
  
  Cada entrada terá um botão "Ver" que dispara o comando "ver_video"
  com o dentificador do vídeo como argumento (chave 'video')."""
  return html_bloco_catalogo_de_videos_IMP.gera(vid_ids, mostra_autor)
