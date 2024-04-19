import comando_solicitar_pag_buscar_sessoes_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP
  "solicitar_pag_buscar_sessoes". Este comando é tipicamente emitido
  pelo browser do usuário quando este  usuário aperta o botão 
  "Buscar Sessões" no menu geral.  O resultado é uma página HTML que
  permite ao usuário especificar os parâmetros da busca.

  O parâmetro {ses} será a sessão de login corrente, a que emitiu o comando.
  deve uma sessão atualmente aberta de um usuário administrador.
  A busca por sessões não é permitida a usuários comuns ou não logados.
  
  O parâmetro {cmd_args} deve ser um {dict} com os argumentos do comando,
  recebidos por HTTP.  Atualmente deve ser vazio, e é ignorado.

  A função retorna uma página HTML {pag} contendo um formulário que
  mostra campos que podem ser usados para busca de sessões, com valores
  editáveis. Veja {html_pag_buscar_sessoes.gera}. O formulário vai
  incluir um botão de sumbissão "Buscar", que emite o comando
  "buscar_sessoes".
  """
  return comando_solicitar_pag_buscar_sessoes_IMP.processa(ses, cmd_args)
