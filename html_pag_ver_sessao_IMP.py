import html_pag_generica
import html_elem_button_simples
import html_bloco_dados_de_sessao
import html_elem_form
import obj_sessao

def gera(ses_login, ses_a_ver, erros):

  editavel = False
  para_admin = obj_sessao.de_administrador(ses_login)
  para_proprio = ( obj_sessao.obtem_dono(ses_login) ==  obj_sessao.obtem_dono(ses_a_ver) )
  ht_bloco_ses = html_bloco_dados_de_sessao.gera(ses_a_ver, editavel, para_admin, para_proprio)

  if ((para_admin or para_proprio) and obj_sessao.aberta(ses_a_ver)):
    # O usuário pode fechar a sessão:
    cmd_args = {}
    cmd_args['sessao'] = obj_sessao.obtem_identificador(ses_a_ver)
    fecha_btn = html_elem_button_simples.gera('Fechar sessão', 'fechar_sessao', cmd_args, '#FF7700')
    ht_bloco_ses += fecha_btn
    
  ht_form_ses = html_elem_form.gera(ht_bloco_ses, False)

  pag = html_pag_generica.gera(ses, ht_bloco_ses, erros)
  return pag
