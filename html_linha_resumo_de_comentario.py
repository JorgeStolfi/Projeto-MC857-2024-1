import html_linha_resumo_de_comentario_IMP

def gera(ses, com, mostra_autor, mostra_video, mostra_pai, mostra_nota, forcar_mostrar_texto):
  """
  Devolve uma lista de fragmentos HTML com os valores dos principais
  atributos do objeto {com} da classe {obj_comentario.Classe}, incluindo o
  identificador {com_id}. Esta função serve para gerar os elementos de
  uma linha da tabela produzida por {html_bloco_lista_de_comentarios.gera}.

  O parãmetro {ses} deve {None} ou um objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.

  Os parametros {mostra_autor}, {mostra_video} e {mostra_pai} determinam
  se o resumo vai incluir os campos 'autor', 'video' e 'pai',
  respectivamente.
  
  Se {com} for {None}, o resultado é uma lista com os cabeçalhos das
  colunas da tabela ("Comentário", "Vídeo", etc.), em vez dos valores
  dos atributos.
  
  Cada elemento do resultado estará formatado com um estilo adequado.
  Veja {html_elem_item_de_resumo.gera}.
  
  Se {com} não é {None}, resultado inclui também um botão "Ver" que dispara um comando
  HTTP "ver_comentario".  O argumento desse comando será {{ 'comentario': com_id }}.
  """
  return html_linha_resumo_de_comentario_IMP.gera(ses, com, mostra_autor, mostra_video, mostra_pai, mostra_nota, forcar_mostrar_texto)
