import html_bloco_dados_de_usuario
import html_elem_form
import html_elem_button_simples
import html_elem_button_submit


def gera(id_usuario, atrs, admin, texto_bt, comando_bt):
  # Constrói tabela com dados:
  ht_table = html_bloco_dados_de_usuario.gera(id_usuario, atrs, admin)

  # Constrói formulário com botões 'Confirmar' e 'Cancelar':
  ht_submit = html_elem_button_submit.gera(texto_bt, comando_bt, None, '#55ee55')
  ht_cancel = html_elem_button_simples.gera("Cancelar", 'principal', None, '#ee5555')
  conteudo_form = \
    ( ht_table + "\n" ) + \
    ( "    " + ht_submit + "\n" ) + \
    ( "    " + ht_cancel + "\n" )

  ht_form = html_elem_form.gera(conteudo_form)
  
  return ht_form
