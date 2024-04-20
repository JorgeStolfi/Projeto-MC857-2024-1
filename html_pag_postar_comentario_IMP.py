import html_form_postar_comentario
import html_pag_generica
import obj_sessao

def gera(ses, atrs, erros):

  # Estas condições deveriam ser garantidas para pedidos gerados pelo site:
  assert ses != None and obj_sessao.aberta(ses), "Sessao inválida"
  assert type(atrs) is dict
  assert erros == None or type(erros) is list or type(erros) is tuple
 
  ht_form = html_form_postar_comentario.gera(atrs)

  pag = html_pag_generica.gera(ses, ht_form, erros)
  return pag
  
