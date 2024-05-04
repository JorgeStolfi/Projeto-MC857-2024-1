import obj_usuario
import obj_video
import html_elem_paragraph
import html_elem_button_simples

def gera(id_vid, atrs_vid, edita_titulo):
  
  # atrs_tb = ...
  # dados_linhas = ...
  # ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tb)
  
  # Botão de comentarios
  ht_comentarios = html_elem_button_simples.gera("Ver comentários", 'html_pag_ver_conversa', None, '#808080')

  mensagem = html_elem_paragraph.gera(None, "!!! html_bloco_dados_de_video não implementado ainda !!!")
  ht_table = mensagem + "<br>" + ht_comentarios
  
  
  return ht_table
