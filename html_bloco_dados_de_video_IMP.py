import obj_usuario
import obj_video
import html_elem_paragraph
import html_bloco_tabela_de_campos
import html_elem_button_submit


def gera(id_vid, atrs_vid, edita_titulo):
  
  # atrs_tb = ...
  # dados_linhas = ...
  # ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tb)

  ht_answer = html_elem_button_submit.gera("Responder", "postar_comentario", None, '#55ee55')

  mensagem = html_elem_paragraph.gera(None, "!!! html_bloco_dados_de_video não implementado ainda !!!")
  ht_table = mensagem

  return ht_table
