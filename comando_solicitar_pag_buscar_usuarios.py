import comando_solicitar_pag_buscar_usuarios_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Buscar Usuários"
  no menu geral da pagina do administrador.

  A função retorna uma página HTML {pag} com o formulário que mostra
  campos que podem ser usados para busca de usuários, com campos editáveis.
  O formulário deve conter um botão de sumbissão "Buscar".

  O argumento {ses} deve ser uma sessão atualmente aberta.

  A sessão aberta deve ser de um administrador, que pode realizar uma busca
  para encontrar qualquer usuário cadastrado"""
  return comando_solicitar_pag_buscar_usuarios_IMP.processa(ses, args)
