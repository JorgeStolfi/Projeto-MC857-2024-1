import html_elem_button_submit
import html_elem_form
import html_bloco_tabela_de_campos

def gera():

  dados_linhas = []
  
  dados_linhas.append( ( "E-mail", "email",    'email', True, "xxx@yyy.zzz" ) )
  dados_linhas.append( ( "Senha",  "password", 'senha', True, None ) )

  # Monta a tabela com os fragmentos HTML:
  ht_tabela = html_bloco_tabela_de_campos.gera(dados_linhas, {})

  ht_bt_login = html_elem_button_submit.gera("Entrar", 'fazer_login', None, None)

  ht_conteudo = \
    ht_tabela + "\n" + \
    ht_bt_login

  ht_form = html_elem_form.gera(ht_conteudo, False)

  return ht_form
  
