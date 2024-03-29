import obj_usuario
import obj_sessao
import html_elem_paragraph

def gera(ses):
  ses_id = obj_sessao.obtem_identificador(ses)
  ses_usr = obj_sessao.obtem_usuario(ses)
  ses_usr_id = obj_usuario.obtem_identificador(ses_usr)
  ses_aberta = obj_sessao.aberta(ses)
  data_login = obj_sessao.obtem_data_de_criacao(ses)

  #estilo_parag = "width: 600px; margin-top: 10px; margin-bottom: 2px; text-indent: 0px;  line-height: 75%;"
  #ht_ses = html_elem_paragraph.gera(estilo_parag, ses_id)
  #ht_usr = html_elem_paragraph.gera(estilo_parag, ses_usr_id)
  #ht_ses_aberta = html_elem_paragraph.gera(estilo_parag, str(ses_aberta))
  #ht_bloco = ht_ses + ht_usr + ht_ses_aberta
  #return ht_bloco

  #Formata um linha em html que exibe todos os atributos da sessao. Esta linha pode ser concatenada com outras linhas do mesmo tipo sem perder forma
  status_clr = "green" if ses_aberta else "red"
  status_txt = "Aberta" if ses_aberta else "Fechada"
  linha_formatada = \
    f'<hr/><p><b>ID sessao:</b> {ses_id} | ' + \
    f'<b>ID usuario:</b> {ses_usr_id} | ' + \
    f'<b>criacao:</b> {data_login} | ' + \
    f'<b>Status sessao:</b> <font color="{status_clr}">{status_txt}</font><p>'

  return linha_formatada
