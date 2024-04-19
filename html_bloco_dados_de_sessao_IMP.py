import obj_usuario
import obj_sessao
import html_elem_paragraph
import html_bloco_tabela_de_campos

def gera(ses):
  ses_id = obj_sessao.obtem_identificador(ses)
  ses_usr = obj_sessao.obtem_usuario(ses)
  ses_admin = obj_usuario.obtem_atributo(ses_usr, 'administrador')
  ses_usr_id = obj_usuario.obtem_identificador(ses_usr)
  ses_aberta = obj_sessao.aberta(ses)
  data_login = obj_sessao.obtem_data_de_criacao(ses)

  atrs = { 'sessao': ses_id, 'data_login': data_login, 'usuario': ses_usr_id, 'aberta': "Sim" if ses_aberta else "Não", }

  dados_linhas = \
    (
      ( "ID sessão",        "text", 'sessao',     False, None, ),
      ( "Criada em",        "text", 'data_login', False, None, ),
      ( "ID usuário",       "text", 'usuario',    False, None, ),
      ( "Status da sessão", "text", 'aberta',     False, None, ),
    )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs)

  return ht_table
