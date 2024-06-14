import obj_video
import obj_usuario
import html_elem_span
import html_elem_button_simples
import html_estilo_texto
import html_elem_link_img
import html_elem_link_text
import util_bloqueado
import util_nota
import util_testes
import obj_sessao

def gera(vid, mostra_autor):

  assert vid != None, "precisa especificar um vídeo"

  vid_id = obj_video.obtem_identificador(vid)
  atrs = obj_video.obtem_atributos(vid)
  

  descr = atrs['titulo']
  altura = 64
  ht_janela = html_elem_img.gera(f"capas/{vid_id}.png", descr, altura)
  
  texto_atributos = "!!! {html_linha_catalogo_de_videos.gera} NÃO IMPLEMENTADA !!!"
  ht_atributos = texto_atributos

  hts_linha = [ ht_janela, ht_atributos ]
  
  return hts_linha
