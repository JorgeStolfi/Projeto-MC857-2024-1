import obj_usuario
import obj_sessao
import html_elem_paragraph
import html_bloco_tabela_de_campos

def gera(ses):
  ses_id = obj_sessao.obtem_identificador(ses)
  ses_usr = obj_sessao.obtem_usuario(ses)
  admin = obj_usuario.obtem_atributo(ses_usr, 'administrador')
  ses_usr_id = obj_usuario.obtem_identificador(ses_usr)
  ses_abrt = obj_sessao.aberta(ses)
  data_login = obj_sessao.obtem_data_de_criacao(ses)

  atrs = { 'id_ses': ses_id, 'data_login': data_login, 'id_usr': ses_usr_id, 'abrt': "Sim" if ses_abrt else "Não", }

  dados_linhas = \
    (
      ( "ID sessão",        "text", 'id_ses',     None, False, ),
      ( "Criada em",        "text", 'data_login', None, False, ),
      ( "ID usuário",       "text", 'id_usr',     None, False, ),
      ( "Status da sessão", "text", 'abrt',       None, False, ),
    )

  ht_table = html_bloco_tabela_de_campos.gera(dados_linhas, atrs, admin)

  return ht_table
