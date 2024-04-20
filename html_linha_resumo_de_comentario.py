import html_linha_resumo_de_comentario_IMP

def gera(com, mostra_autor=True, mostra_video=True):
  """Devolve uma lista de fragmentos HTML com os valores dos principais 
  campos do objeto {com} da classe {obj_comentario.Classe}.
  
  O resultado atualmente inclui os campos 'video', 'autor', 'data',
  'pai', e 'texto'. Inclui também um botão "Ver" que dispara um comando
  HTTP "ver_comentario" com o argumento 'comentario', o identificador
  do dito cujo.

  Essa funcao agora aceita os parametros {mostra_autor, mostra_video},
  que determinam se o resumo inclui os campos de autor e video.
  Eles tem o valor default de True, ou seja, se o usuário.
  
  Esta função serve para gerar os elementos de uma linha da tabela
  produzida por {html_bloco_lista_de_comentarios.gera}.
  """
  return html_linha_resumo_de_comentario_IMP.gera(com, mostra_autor, mostra_video)
