import obj_sessao
import obj_usuario

import html_elem_span
import html_elem_button_simples
import html_elem_label

def gera(ses, bt_ver, bt_fechar):
  ses_id = obj_sessao.obtem_identificador(ses)
  # Pega/monta atributos a mostrar:
  ses_usuario = obj_sessao.obtem_atributo(ses, 'usr')
  ses_aberta = obj_sessao.obtem_atributo(ses, 'abrt')
  ses_cookie = obj_sessao.obtem_atributo(ses, 'cookie')
  ses_data = obj_sessao.obtem_atributo(ses, 'criacao')

  # Formata informações em HTML:
  ht_ses_id = formata_texto(ses_id)
  ht_codigo_usuario = formata_texto(obj_usuario.obtem_identificador(ses_usuario))
  ht_estado = formata_texto("Aberta" if ses_aberta else "Fechada")
  ht_cookie = formata_texto(ses_cookie)
  ht_data = formata_texto(ses_data)

  ht_campos = [ ht_ses_id, ht_codigo_usuario, ht_estado, ht_cookie, ht_data ]
  
  args_bt = {'id_ses': ses_id} # Argumentos para os botões.
  cor_bt_admin = '#FFA700' # Cor para botões de adminstrador.

  # O comando para tratar a url "ver_detalhes_sessao" ainda não existe, e deverá ser implementado
  # no futuro.
  if bt_ver:
    ht_bt_fechar = html_elem_button_simples.gera("Ver", 'ver_sessao', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_fechar)

  if bt_fechar and ses_aberta:
    ht_bt_fechar = html_elem_button_simples.gera("Fechar", 'fechar_sessao', args_bt, cor_bt_admin)
    ht_campos.append(ht_bt_fechar)

  return ht_campos

def formata_texto(txt):
  """Formata o texto {txt} com um estilo apropriado."""
  estilo = "font-weight:bold"
  return html_elem_span.gera(estilo, txt)

