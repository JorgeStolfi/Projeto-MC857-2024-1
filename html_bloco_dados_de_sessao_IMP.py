import obj_usuario
import obj_sessao
import html_elem_paragraph
import html_bloco_tabela_de_campos
import html_elem_button_simples

def gera(ses_id, para_admin, para_proprio):

  # Validação de tipos (paranóia):
  assert ses_id != None and isinstance(ses_id, str), "{ses_id} inválido"
  assert type(para_admin) is bool, "{para_admin} inválido"
  assert type(para_proprio) is bool, "{para_proprio} inválido"

  # Obtém a sessão a mostrar
  ses = obj_sessao.obtem_objeto(ses_id)
  assert ses != None, f"Sessão {ses_id} não existe"
  
  # Obtem os atributos {atrs_tab} a mostrar:
  atrs_tab = obj_sessao.obtem_atributos(ses).copy()
  
  # Acrescenta o identificador da sessão:
  atrs_tab['sessao'] = ses_id
  
  # Converte o atributo 'aberta' para "Sim"/"Não":
  atrs_tab['aberta'] = "Sim" if atrs_tab['aberta'] else "Não"

  # Linhas da tabela: 
  dados_linhas = \
    (
      ( "ID da sessão",       "text", 'sessao',     False, None, ),
      ( "Criada em",          "text", 'data_login', False, None, ),
      ( "Usuário criador",    "text", 'dono',       False, None, ),
      ( "Cookie",             "text", 'cookie',     False, None, ),
      ( "Status da sessão",   "text", 'aberta',     False, None, ),
    )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs_tab)

  # Acrescenta botões para ver outras coisas da sessão, se for o caso:
  ht_bt_fechar = None # A menos que tenha.
  assert ses_id != None
  cmd_args = { 'sessao': ses_id }
  if para_admin or para_proprio:
    ht_bt_fechar = html_elem_button_simples.gera(f"Fechar", "fechar_sessao", cmd_args, '#eeee55')

  ht_bloco = \
    ht_table + "<br/>" + \
    ( ht_bt_fechar + " " if ht_bt_fechar != None else "")
 
  return ht_bloco
