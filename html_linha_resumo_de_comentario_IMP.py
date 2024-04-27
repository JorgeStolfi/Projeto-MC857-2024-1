import obj_comentario
import obj_usuario
import obj_video

import html_elem_paragraph
import html_elem_span
import html_elem_button_simples

def gera(com, mostra_autor, mostra_video, mostra_pai):
  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
  estilo_texto = f"font-family: Courier; font-size: 20px; font-weight: bold; padding: 2px; text-align: left; color: #263238;"

  com_atrs = obj_comentario.obtem_atributos(com)
  itens_resumo = []

  if mostra_autor:
    autor = com_atrs['autor']
    autor_id = obj_usuario.obtem_identificador(autor)
    ht_autor = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, autor_id))
    itens_resumo.append(ht_autor)
  
  if mostra_video:
    video = com_atrs['video']
    video_id = obj_video.obtem_identificador(video)
    ht_video = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, video_id))
    itens_resumo.append(ht_video)

  if mostra_pai:
    pai = com_atrs['pai']
    if pai != None:
      pai_id = obj_comentario.obtem_identificador(pai)
      ht_pai = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, pai_id))
    else:
      ht_pai = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, pai))
    itens_resumo.append(ht_pai)

  data = com_atrs['data']
  ht_data = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, data))
  itens_resumo.append(ht_data)

  texto = com_atrs['texto']
  max_texto = 30
  ht_texto = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, texto[:max_texto]))
  itens_resumo.append(ht_texto)

  bt_args = { 'comentario': obj_comentario.obtem_identificador(com) }
  bt_ver = html_elem_button_simples.gera("Ver", "buscar_comentarios_de_video", bt_args, "#eeeeee")
  itens_resumo.append(bt_ver)

  return itens_resumo
