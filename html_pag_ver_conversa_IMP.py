import html_bloco_conversa
import html_bloco_titulo
import html_pag_generica
import html_elem_button_simples
import html_elem_form
import obj_comentario
import obj_sessao

def gera(ses, titulo, conversa, erros):
 
  # Verificação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(titulo, str)
  assert conversa == None or isinstance(conversa, list) or isinstance(conversa, tuple) 
  assert erros == None or isinstance(erros, str) or isinstance(erros, list) or isinstance(erros, tuple) 
  
  if erros == None: erros = [ ]
  if isinstance(erros, str): erros = [ erros, ]
  erros = list(erros.copy())

  ses_aberta = obj_sessao.aberta(ses) if ses != None else False
  ses_dono = obj_sessao.obtem_dono(ses) if ses != None and ses_aberta else None

  ht_titulo = html_bloco_titulo.gera(titulo)
  ht_conv = html_bloco_conversa.gera(conversa, ses_dono)
  
  pag = html_pag_generica.gera(ses, ht_titulo + ht_conv, erros)
  
  return pag
