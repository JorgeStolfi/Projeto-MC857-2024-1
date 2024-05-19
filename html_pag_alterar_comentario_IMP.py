import html_bloco_titulo
import html_elem_button_simples
import html_form_postar_alterar_comentario
import html_pag_generica
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video

def gera(ses, com, atrs_mod, erros):

  # Validação de tipos (paranóia):
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  assert com != None and isinstance(com, obj_comentario.Classe)
  assert atrs_mod != None and isinstance(atrs_mod, dict)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)
  
  if atrs_mod == None: atrs_mod = {}
  
  if ses != None and obj_sessao.aberta(ses):
    para_admin = obj_sessao.de_administrador(ses)
  else:
    para_admin = False
  
  com_id = obj_comentario.obtem_identificador(com) 
  com_atrs = obj_comentario.obtem_atributos(com) 
  
  ht_pag_tit = html_bloco_titulo.gera(f"Editando o comentário {com_id}")
  
  texto_bt = "Salvar alterações"
  cmd_bt = "alterar_comentario"
  ed_nota = para_admin

  autor = com_atrs['autor']
  ses_dono = obj_sessao.obtem_dono(ses)
  ed_voto = para_admin or autor == ses_dono

  ht_form = html_form_postar_alterar_comentario.gera(com_id, atrs_mod, ed_nota, ed_voto)

  ht_pag_conteudo = \
    ht_pag_tit + \
    ht_form
  
  pag = html_pag_generica.gera(ses, ht_pag_conteudo, erros)

  return pag
