import obj_sessao
import obj_usuario
import html_form_cadastrar_usuario
import html_pag_generica

def gera(ses, atrs, erros):

  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert atrs == None or isinstance(atrs, dict)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)

  # Obtém dono da sessão {ses}:
  if ses != None:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    para_admin = obj_usuario.eh_administrador(ses_dono)
  else:
    ses_dono = None
    para_admin = False
  
  atrs_pag = atrs.copy() if atrs != None else { }

  # Constrói formulário com dados:
  ht_form = html_form_cadastrar_usuario.gera(atrs_pag, para_admin)

  ht_conteudo = ht_form

  # Monta a página:
  pagina = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pagina
