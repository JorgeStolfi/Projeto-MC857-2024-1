import obj_video
import obj_sessao

import html_form_alterar_video
import html_pag_generica
import html_elem_button_simples

def gera(ses, id_vid, atrs, erros):

  # Páginas geradas pelo sistema deveriam satisfazer estas condições:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert type(id_vid) is str, "Identificador inválido"
  assert atrs == None or type(atrs) is dict
  assert erros == None or type(erros) is tuple or type(erros) is list
  
  # Obtem o vídeo a ver:
  vid = obj_video.busca_por_identificador(id_vid) 
  assert vid != None, f"Vídeo {id_vid} não existe"
  
  # Cria o formulário básico:
  ht_form = html_form_alterar_video.gera(id_vid, atrs)
    
  ht_conteudo = ht_form

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
