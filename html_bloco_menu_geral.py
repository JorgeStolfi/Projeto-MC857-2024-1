import html_bloco_menu_geral_IMP

def gera(logado, nome_usuario, admin):
  """Retorna o menu geral, que será mostrado no alto da maioria das páginas do site.  
  
  O parâmetro {logado} deve ser {True} se o usuário estiver logado; 
  nesse caso {nome_usuario} deve ser seu nome.  Se for {False}, o nome
  será ignorado.
  O parâmetro booleano {admin} diz se o usuário é administrador"""
  return html_bloco_menu_geral_IMP.gera(logado, nome_usuario, admin)
