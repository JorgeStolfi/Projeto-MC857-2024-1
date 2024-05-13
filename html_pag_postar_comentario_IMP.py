import html_bloco_titulo
import html_elem_button_simples
import html_form_postar_alterar_comentario
import html_pag_generica
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video

def gera(ses, atrs, erros):

  # Validação de tipos (paranóia):
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  assert atrs == None or isinstance(atrs, dict)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)
  
  if atrs == None: atrs = {}
  
  ht_pag_tit = html_bloco_titulo.gera(f"Novo comentário")
  
  ht_form = html_form_postar_alterar_comentario.gera(None, atrs)

  ht_pag_conteudo = \
    ht_pag_tit + \
    ht_form
  
  pag = html_pag_generica.gera(ses, ht_pag_conteudo, erros)

  return pag
  
