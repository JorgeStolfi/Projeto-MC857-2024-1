import html_bloco_lista_de_comentarios_IMP

def gera(ses, com_ids, mostra_autor, mostra_video, mostra_pai, mostra_nota):
  """Retorna um trecho de HTML que descreve resumidamente os comentarios cujos 
  identificadores estão na lista {com_ids}.  
  
  O resultado é uma "<table>...</table>" onde cada linha contém os dados
  principais do comentário, e botões que agem sobre o mesmo.
  Vide {html_linha_resumo_de_comentario.gera}.]
 
  Os booleanos {mostra_autor}, {mostra_video}, {mostra_pai}, e {mostra_nota}
  dizem se em cada linha devem ser mostrados os atributos 'video', 'autor', 'pai', e 'nota',
  respectivamente."""
  return html_bloco_lista_de_comentarios_IMP.gera(ses, com_ids, mostra_autor, mostra_video, mostra_pai, mostra_nota)
