import comando_solicitar_pag_cadastrar_usuario_IMP

def processa(ses, args):
  """Esta função é chamada quando o usuário aperta o botão "Cadastrar"
  no menu geral de uma página qualquer.
  
  A função retorna uma página HTML {pag} contendo o formulário para definir um
  os atributos do novo usuário, e um botão de sumbissão "Cadastrar".
  
  O dicionário de argumentos {args} é irrelevantes e pode ser {None}.
  
  A sessão corrente {ses} pode ser {None}; se não for, deve estar
  aberta. Se {ses} não for {None} e o dono dela for um administrador do
  site, a página retornada terá a opção de tornar o novo usuário um
  administrador, também.
  
  Se a sessão corrente {ses} for {None}, ou o dono dela não for um administrador,
  a página retornada não terá essa opção e só permitirá criar outro usuário
  comum (cliente)."""
  return comando_solicitar_pag_cadastrar_usuario_IMP.processa(ses, args)

