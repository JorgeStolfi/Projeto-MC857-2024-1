import html_bloco_lista_de_comentarios_IMP

def gera(lista_ids_com, mostra_autor, mostra_video, mostra_pai):
  """Retorna um trecho de HTML que descreve resumidamente os comentarios cujos 
  identificadores estão na lista {lista_ids_com}.  
  
  O resultado é uma "<table>...</table>" onde cada linha contém os dados
  principais do comentário, e botões que agem sobre o mesmo.
  Vide {html_linha_resumo_de_comentario.gera}.]
 
  Os booleanos {mostra_autor}, {mostra_video}, e {mostra_pai} dizem se em cada linha devem ser
  mostrados os atributos 'video', 'autor', e 'pai', respectivamente."""
  return html_bloco_lista_de_comentarios_IMP.gera(lista_ids_com, mostra_autor, mostra_video, mostra_pai)
