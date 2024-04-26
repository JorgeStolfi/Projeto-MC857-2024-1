import html_elem_label
import html_elem_input
import html_elem_table
import html_elem_button_submit
import html_elem_form

def gera():
  linhas = [].copy()
  
  ht_rot_campo = html_elem_label.gera("E-mail", ": ")
  ht_campo = html_elem_input.gera("text", "email", None, None, None, True, "nome@provedor", None, False)
  linhas.append((ht_rot_campo, ht_campo,))
  
  ht_rot_campo = html_elem_label.gera("Senha", ": ")
  ht_campo = html_elem_input.gera("password", "senha", None, None, None, True, None, None, False)
  linhas.append((ht_rot_campo, ht_campo,))

  # Monta a tabela com os fragmentos HTML:
  ht_table = html_elem_table.gera(linhas, None)

  ht_bt_login = html_elem_button_submit.gera("Entrar", 'fazer_login', None, '#55ee55')

  ht_campos = \
    ht_table + \
    ht_bt_login

  ht = html_elem_form.gera(ht_campos, False)
  return ht
  
