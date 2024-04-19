import comando_solicitar_pag_buscar_usuarios_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP
  "solicitar_pag_buscar_usuarios". Este comando é tipicamente emitido
  pelo browser do usuário quando este aperta o botão "Buscar Usuários"
  no menu geral, ou equivalente. O resultado é uma página HTML que
  permite ao usuário especificar os parâmetros da busca.

  O parâmetro {ses} será a sessão de login corrente, a que emitiu o comando.
  Pode ser {None} (se o usuário que emitiu não está logado)
  ou um objeto de tipo {obj_sessao.Classe}, atualmente aberta. 
  
  O parâmetro {cmd_args} será um um {dict} com os argumentos do comando,
  recebidos por HTTP.  Atualmente deve ser {None} ou vazio, e é ignorado.
  
  A função retorna uma página HTML {pag} contendo um formulário que mostra
  campos que podem ser usados para busca de usuários, com valores editáveis.
  Veja {html_pag_buscar_usuarios.gera}.  A página vai conter
  um botão de sumbissão "Buscar", que emite o comando "buscar_usuarios". 
  
  Alguns atributos de usuário, como 'email', só poderão ser usados
  na busca se quem pediu a página (o dono da sessão {ses}) for
  um administrador.
  """
  return comando_solicitar_pag_buscar_usuarios_IMP.processa(ses, cmd_args)
