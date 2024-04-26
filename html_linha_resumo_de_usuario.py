import html_linha_resumo_de_usuario_IMP

def gera(usr):
  """Devolve um fragmento HTML que decreve o usuãrio {usr}, 
  um objeto da classe {obj_usuario.Classe}.
  
  O fragmento mostra apenas nome e email, e um botão "Ver" que
  dispara um comando HTTP "ver_usuario"
  para mostrar os dados correntes do usuário."""
  return html_linha_resumo_de_usuario_IMP.gera(usr)
