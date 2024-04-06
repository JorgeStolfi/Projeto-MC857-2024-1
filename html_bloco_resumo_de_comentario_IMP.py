import obj_comentario
import obj_usuario
import obj_video
import html_elem_paragraph
import html_elem_span
import html_elem_button_simples

def gera(com):
  atrs = obj_comentario.obtem_atributos(com)
  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
  estilo_texto = f"font-family: Courier; font-size: 20px; font-weight: bold; padding: 2px; text-align: left; color: #263238;"

  video = atrs['video']
  video_id = obj_video.obtem_identificador(video)
  ht_video = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, video_id))

  autor = atrs['autor']
  autor_id = obj_usuario.obtem_identificador(autor)
  ht_autor = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, autor_id))

  data = atrs['data']
  ht_data = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, data))

  pai = atrs['pai']
  if pai != None:
    pai_id = obj_comentario.obtem_identificador(pai)
    ht_pai = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, pai_id))
  else:
    ht_pai = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, pai))

  texto = atrs['texto']
  ht_texto = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, texto))

  bt_arg = {'id_comentario': obj_comentario.obtem_identificador(com)}
  bt_ver = html_elem_button_simples.gera("Ver", "ver_comentarios_de_video", bt_arg, "#eeeeee")

  return [ht_video, ht_autor, ht_data, ht_pai, ht_texto, bt_ver]