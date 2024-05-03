import html_bloco_menu_geral_IMP

def gera(usr):
  """Retorna o menu geral, que será mostrado no alto da maioria das páginas do site.  
  
  Se {usr} for {None}, a função supõe que a página foi pedida por um usuário 
  não logado.  Senão, {usr} deve ser um objeto de tipo {obj_usuario.Classe}
  e a função supõe que esse usuário está logado e foi quem pediu a página.
  
  Os botões oferecidos no menu são diferente nos dois casos. No segundo caso,
  eles também dependem de se {usr} é administrador ou não."""
  return html_bloco_menu_geral_IMP.gera(usr)
