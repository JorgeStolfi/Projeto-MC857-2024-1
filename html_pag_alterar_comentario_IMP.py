import obj_comentario
import obj_sessao

import html_form_alterar_comentario
import html_pag_generica
import html_elem_button_simples

def gera(ses, id_com, atrs, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert type(id_com) is str, "Identificador inválido"
  assert atrs == None or type(atrs) is dict
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  # Obtem o comentário a ver:
  com = obj_comentario.busca_por_identificador(id_com) 
  assert com != None, f"Comentário {id_com} não existe"
  
  # Cria o formulário básico:
  ht_form = html_form_alterar_comentario.gera(id_com, atrs)
    
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
