import html_bloco_conversa
import html_bloco_titulo
import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_comentario
import html_elem_form
import obj_comentario

def gera(ses, titulo, conversa, erros):
  ht_titulo = html_bloco_titulo.gera(titulo)
  ht_conv = html_bloco_conversa.gera(conversa)
  pag = html_pag_generica.gera(ses, ht_titulo + ht_conv, erros)
  return pag
