import obj_sessao
import obj_usuario

import html_elem_span
import html_elem_button_simples
import html_elem_label

def gera(ses, bt_ver, bt_fechar):
  ses_id = obj_sessao.obtem_identificador(ses)
  # Pega/monta atributos a mostrar:
  ses_usr = obj_sessao.obtem_atributo(ses, 'usr')
  ses_aberta = obj_sessao.obtem_atributo(ses, 'aberta')
  ses_cookie = obj_sessao.obtem_atributo(ses, 'cookie')
  ses_data = obj_sessao.obtem_atributo(ses, 'criacao')

  # Formata informações em HTML:
  ht_ses_id = formata_texto(ses_id)
  ht_usr_id = formata_texto(obj_usuario.obtem_identificador(ses_usr))
  ht_aberta = formata_texto("Aberta" if ses_aberta else "Fechada")
  ht_cookie = formata_texto(ses_cookie)
  ht_data = formata_texto(ses_data)

  ht_campos = [ ht_ses_id, ht_usr_id, ht_aberta, ht_cookie, ht_data ]
  
  args_bt = {'id_ses': ses_id} # Argumentos para os botões.
  cor_bt_admin = '#FFA700' # Cor para botões de adminstrador.

  if bt_ver:
    ht_bt_ver = html_elem_button_simples.gera("Ver", 'ver_sessao', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_ver)

  if bt_fechar:
    if ses_aberta:
      ht_bt_fechar = html_elem_button_simples.gera("Fechar", 'fechar_sessao', args_bt, cor_bt_admin)
    else:
      ht_bt_fechar = formata_texto(" ")
    ht_campos.append(ht_bt_fechar)

  return ht_campos

def formata_texto(txt):
  """Formata o texto {txt} com um estilo apropriado."""
  estilo = "font-weight:bold"
  return html_elem_span.gera(estilo, txt)

