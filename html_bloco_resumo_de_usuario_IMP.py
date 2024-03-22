import obj_usuario
import html_elem_paragraph
import html_elem_span
import html_elem_button_simples

def gera(usr):
  atrs = obj_usuario.obtem_atributos(usr)

  estilo_parag = "\n display:block; word-wrap:break-word;  width: 100%;\n  margin-top: 10px;\n  margin-bottom: 2px;\n  text-indent: 0px;\n  line-height: 75%;"
  estilo_texto = f"font-family: Courier; font-size: 20px; font-weight: bold; padding: 2px; text-align: left; color: #263238;"

  nome = atrs['nome']
  ht_nome = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, nome))

  email = atrs['email']
  ht_email = html_elem_paragraph.gera(estilo_parag, html_elem_span.gera(estilo_texto, email))

  # solicitar_pag_alterar_usuario precisa ser um dicionário com um único campo id_usr
  bt_arg = {'id_usr': obj_usuario.obtem_identificador(usr)}
  bt_ver = html_elem_button_simples.gera("Ver", "solicitar_pag_alterar_usuario", bt_arg, "#eeeeee")

  ht_final = ht_nome + ht_email + bt_ver
  bloco_final = html_elem_span.gera("\n display: inline-block;", ht_final)

  width_pct = ("33%")
  estilo_final = f"width: {width_pct}; padding: 15px; border-radius: 15px 50px 20px; display: flex; align-items: center;"
  bloco_final = html_elem_span.gera(estilo_final, bloco_final)
  return bloco_final
