import html_bloco_bemvindo_IMP

def gera(usr):
  """Retorna um techo de HTML a ser incluído no alto de páginas de um usuário {usr}
  mostrando o avatar, "Bem-vindo {nome}!", e "Você tem {n} sessões abertas".
  
  Se {us} for {None}, tem apenas um "Bem-vindo" genérico.
  
  O resultado é um elemento "<nav>...</nav>". """
  return html_bloco_bemvindo_IMP.gera(usr)
