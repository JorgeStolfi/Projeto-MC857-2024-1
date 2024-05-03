import obj_usuario
import obj_sessao

import html_form_criar_alterar_usuario
import html_pag_generica
import html_elem_button_simples

def gera(ses, id_usr, atrs, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert id_usr == None or type(id_usr) is str
  assert atrs == None or type(atrs) is dict
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  # Obtem o usuário da sessão:
  usr_ses = obj_sessao.obtem_usuario(ses) if ses != None else None
  
  # Obtem o usuário a ver:
  if id_usr == None:
    assert usr_ses != None, "Usuário não especificado"
    usr = usr_ses
    id_usr = obj_usuario.obtem_identificador(usr)
  else:
    usr = obj_usuario.obtem_objeto(id_usr) 
    assert usr != None, f"Usuário {id_usr} não existe"

  # Nesta altura devemos ter o usuário a ver:
  assert usr != None and id_usr != None
  
  # Determina privilégios do usuário da sessão:
  admin = obj_sessao.de_administrador(ses) if ses != None else False
  
  # Cria o formulário básico:
  ht_form = html_form_criar_alterar_usuario.gera(id_usr, atrs, admin, "Confirmar alterações", "alterar_usuario")
    
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
