import html_linha_resumo_de_video_IMP

def gera(vid, mostra_autor):
  """
  Devolve uma lista de fragmentos HTML com os valores dos principais
  atributos do objeto {vid} da classe {obj_video.Classe}. Esta função
  serve para gerar os elementos de uma linha da tabela produzida por
  {html_bloco_lista_de_videos.gera}. Observação: para os atributos
  'largura' e 'altura', os seus valores são mostrados no campo de nome
  'Tamanho' ao invés de ter um campo só para 'largura' e outro para
  'altura', sendo mostrados no formato e ordem '{largura}x{altura} px'.

  O parametro booleano {mostra_autor} determina se o resumo vai incluir
  o campo 'autor'.
  
  Se {vid} for {None}, o resultado é uma lista com os cabeçalhos das
  colunas da tabela ("Vídeo", "Autor", "Data", "Tamanho" etc.), em vez dos valores
  dos atributos.
  
  Cada elemento do resultado estará formatado com um estilo adequado.
  Veja {html_elem_item_de_resumo.gera}.
  
  Se {vid} não é {None}, resultado inclui também um botão "Ver" que dispara um comando
  HTTP "ver_video".  O argumento desse comando será {{ 'video': vid_id }}.
  """
  return html_linha_resumo_de_video_IMP.gera(vid, mostra_autor)
  
