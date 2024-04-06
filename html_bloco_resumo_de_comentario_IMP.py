import obj_comentario
import obj_usuario
import html_elem_paragraph
import html_elem_span
import html_elem_button_simples

def gera(com):
  atrs = obj_comentario.obtem_atributos(com)
  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
  estilo_texto = f"font-family: Courier; font-size: 20px; font-weight: bold; padding: 2px; text-align: left; color: #263238;"

  autor = atrs['autor']
  autor_id = obj_usuario.obtem_identificador(autor)
  ht_nome = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, autor_id))

  texto = atrs['texto']
  ht_email = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, texto))

  bt_arg = {'id_comentario': obj_comentario.obtem_identificador(com)}
  bt_ver = html_elem_button_simples.gera("Ver", "solicitar_pag_alterar_comentario", bt_arg, "#eeeeee")

  return [ht_nome, ht_email, bt_ver]