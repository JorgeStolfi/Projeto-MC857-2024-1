import html_bloco_dados_de_comentario
import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_comentario
import html_elem_form
import obj_comentario

def gera(ses, com, erros):
  
  id_com = obj_comentario.obtem_identificador(com) if com != None else None
  atrs_com = obj_comentario.obtem_atributos(com) if com != None else {}
  edita_texto = False
  ht_bloco_com = html_bloco_dados_de_comentario.gera(id_com, atrs_com, edita_texto)

  ht_form_com = html_elem_form.gera(ht_bloco_com, False)

  pag = html_pag_generica.gera(ses, ht_form_com, erros)
  return pag
