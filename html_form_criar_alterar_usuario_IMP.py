import html_bloco_dados_de_usuario
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit


def gera(id_usr, atrs, ses_admin, texto_bt, comando_bt):

  # Validação de argumentos (paranóia):
  assert id_usr == None or type(id_usr) is str
  assert atrs == None or type(atrs) is dict
  assert type(ses_admin) is bool
  assert type(texto_bt) is str
  assert type(comando_bt) is str

  # Se {ses_admin} for {False} e {id_usr} não é {None}, supõe que {id_usr} é o dono da sessão:
  auto = id_usr != None and not ses_admin 

  # Constrói tabela com dados:
  ht_table = html_bloco_dados_de_usuario.gera(id_usr, atrs, ses_admin, auto)

  # Constrói formulário com botões 'Confirmar' e 'Cancelar':
  ht_submit = html_elem_button_submit.gera(texto_bt, comando_bt, None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'pag_principal', None, '#ee5555')
  conteudo_form = \
    ( ht_table + "<br/>\n" ) + \
    ( ht_submit + " " ) + \
    ( ht_cancel + "\n" )

  ht_form = html_elem_form.gera(conteudo_form, False)
  
  return ht_form
