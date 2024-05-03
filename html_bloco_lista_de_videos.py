
import html_bloco_lista_de_videos_IMP

def gera(lista_ids_vid, mostra_autor):
  """Retorna um trecho de HTML que descreve os videos cujos identificadores
  estão na lista {lista_ids_vid}.
  
  Se {mostra_autor} for {True}, a listagem terá uma coluna "Autor"
  com o id do usuário que postou o vídeo.
  
  Cada linha terá um botão "Ver" que dispara o comando "ver_video"
  com o dentificador do vídeo como argumento (chave 'video')."""
  return html_bloco_lista_de_videos_IMP.gera(lista_ids_vid, mostra_autor)
