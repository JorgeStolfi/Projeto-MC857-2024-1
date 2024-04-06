
import html_pag_generica
import html_bloco_lista_de_comentarios
import obj_comentario

def processa(ses, id_video):
  # Modulo que nao existem ainda foram comentados
  lista_ids_comentarios = []
  bloco = ""

  #lista_ids_comentarios = obj_comentario.busca_por_id_video(id_video)
  #bloco = html_bloco_lista_de_comentarios.gera(lista_ids_comentarios)

  pag = html_pag_generica.gera(ses, bloco, None)
  return pag
