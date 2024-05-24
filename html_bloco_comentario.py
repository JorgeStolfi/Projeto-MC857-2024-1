import html_bloco_comentario_IMP

def gera(com, largura, mostra_id, mostra_data, mostra_video, mostra_pai, bt_conversa, bt_responder, bt_editar, bt_calcnota):
  """
  Retorna um fragmento HTML que exibe atributos de um comentário.
 
  O parâmetro {com} deve ser um objeto de tipo {obj_comentario.Classe}

  O parâmetro inteiro {largura} especifica a largura do texto do 
  comentário.
  
  Os parâmetros booleanos {mostra_id}, {mostra_data}, {mostra_video} e {mostra_pai}
  especificam se devem ser exibidos o identificador e os atributos 'video' e 'pai' 
  do comentário, respectivamente.
   
  Os parâmetros booleanos {bt_conversa}, {bt_responder}, e {bt_editar}
  especificam a inclusão de certos botões sob o texto:
  
    * Se {bt_conversa} for {True}, haverá um botão
    "Ver respostas" que, quando clicado, emitirá um comando
    "ver_conversa" para mostrar a árvore de comentários
    resultante a este.
  
    * Se {bt_responder} for {True}, haverá botão "Responder" que, quando
    clicado, emitirá um comando "solicitar_pag_postar_comentario".
  
    * Se {bt_editar} for {True}, haverá um botão "Editar" que, quando clicado,
    emitirá um comando "solicitar_pag_alterar_comentario".
    
  Os argumentos dos comandos emitidos por esses botões serão
  {{ 'comentário': com_id }}.
  """
  return html_bloco_comentario_IMP.gera(com, largura, mostra_id, mostra_data, mostra_video, mostra_pai, bt_conversa, bt_responder, bt_editar, bt_calcnota)

