import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_sessao
import html_elem_form
import obj_sessao

def gera(ses_login, ses_a_ver, erros):

  # Validação de tipos (paranóia):
  assert ses_login == None or isinstance(ses_login, obj_sessao.Classe)
  assert ses_a_ver != None and isinstance(ses_a_ver, obj_sessao.Classe)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)

  ht_bloco_ses = html_bloco_dados_de_sessao.gera(ses_a_ver)

  para_admin = ses_login != None and obj_sessao.de_administrador(ses_login)
  para_proprio = ses_login != None and ( obj_sessao.obtem_dono(ses_login) == obj_sessao.obtem_dono(ses_a_ver) )
  if ((para_admin or para_proprio) and obj_sessao.aberta(ses_a_ver)):
    # O usuário pode fechar a sessão:
    cmd_args = {}
    cmd_args['sessao'] = obj_sessao.obtem_identificador(ses_a_ver)
    ht_bt_fechar = html_elem_button_simples.gera('Fechar sessão', 'fechar_sessao', cmd_args, None)
    ht_bloco_ses += ht_bt_fechar

  pag = html_pag_generica.gera(ses_login, ht_bloco_ses, erros)
  
  return pag
