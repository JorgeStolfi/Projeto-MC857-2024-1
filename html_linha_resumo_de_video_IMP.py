import obj_video
import obj_usuario
import html_elem_paragraph
import html_elem_span
import html_elem_button_simples

def gera(vid):
  atrs = obj_video.obtem_atributos(vid)

  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
  estilo_texto = f"font-family: Courier; font-size: 20px; font-weight: bold; padding: 2px; text-align: left; color: #263238;"

  autor = atrs['autor']
  id_autor = obj_usuario.obtem_identificador(autor)
  ht_usr = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, id_autor))

  arq = atrs['arq']
  ht_arq = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, arq))

  titulo = atrs['titulo']
  ht_titulo = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, titulo))

  data = atrs['data']
  ht_data = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, data))

  duracao = atrs['duracao']
  ht_duracao = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, str(duracao)))

  largura = atrs['largura']
  ht_largura = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, str(largura)))

  altura = atrs['altura']
  ht_altura = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, str(altura)))

  # TODO: ver_video precisa ser implementado
  bt_arg = {'video': obj_video.obtem_identificador(vid)}
  bt_ver = html_elem_button_simples.gera("Ver", "ver_video", bt_arg, "#eeeeee")

  return [ht_usr, ht_arq, ht_titulo, ht_data, ht_duracao, ht_largura, ht_altura, bt_ver]
