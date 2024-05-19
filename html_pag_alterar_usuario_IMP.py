import obj_usuario
import obj_sessao

import html_form_alterar_usuario
import html_pag_generica
import html_elem_button_simples

def gera(ses, usr_id, atrs, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert usr_id != None and type(usr_id) is str, "Identificador de usuário inválido"
  assert atrs == None or type(atrs) is dict
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  # Obtem o usuário a alterar. Nesta altura deve existir:
  usr = obj_usuario.obtem_objeto(usr_id) 
  assert usr != None, f"Usuario {usr_id} não existe"
  
  # Obtem o usuário da sessão, para determinar que campos são editáveis:
  ses_dono = obj_sessao.obtem_dono(ses)
  assert ses_dono != None
  
  # Cria o formulário básico:
  para_admin = obj_usuario.eh_administrador(ses_dono)
  ht_form = html_form_alterar_usuario.gera(usr_id, atrs, para_admin)
    
  ht_bt_cancela = html_elem_button_simples.gera("Cancelar", "pag_principal", None, None)
  
  ht_conteudo = \
    ht_form + "\n" + \
    ht_bt_cancela

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
