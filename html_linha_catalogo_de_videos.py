import html_linha_catalogo_de_video_IMP

def gera(vid, mostra_autor):
  """
  Recebe objeto {vid} da classe {obj_video.Classe}. Devolve uma lista
  de dois fragmentos HTML. O primeiro é uma janela que mostra o vídeo
  {vid}, em tamanho um pouco reduzido. O segundo é um texto em várias
  linhas com os atributos do vídeo (identificador, título, autor, data,
  etc.), como o cabeçalho e rodapé de {html_bloco_video.gera}.
  
  Esta função serve para gerar os elementos de uma linha da tabela
  produzida por {html_bloco_catalogo_de_videos.gera}.

  O parametro booleano {mostra_autor} determina se o resumo vai incluir
  o campo 'autor'.
  
  Se {vid} não é {None}, resultado inclui também um botão "Ver" que dispara um comando
  HTTP "ver_video".  O argumento desse comando será {{ 'video': vid_id }}.
  """
  return html_linha_catalogo_de_video_IMP.gera(vid, mostra_autor)
  
