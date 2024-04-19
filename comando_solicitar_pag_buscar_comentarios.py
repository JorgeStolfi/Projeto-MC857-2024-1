import comando_solicitar_pag_buscar_comentarios_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP
  "buscar_comentarios". Geralmente esse comando é emitido pelo browser
  de um usuário quando este aperta o botão "Buscar Comentários" no menu
  principal. A função devolve uma página com campos editáveis e botões
  para fazer a busca.

  O parâmetro {ses} deve ser a sessão de login que emitiu o comando.
  Pode ser {None} (indicando que o usuário não está logado), ou um objeto
  de tipo {obg_sessao.Classe} atualmente aberta. Não precisa
  ser de administrador.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando HTTP. Atualmente deve ser vazio.

  A função retorna uma página HTML {pag} com o formulário que mostra
  atributos que podem ser usados para busca de comentários, com valores
  editáveis. Veja {html_pag_buscar_comentarios.gera}. O formulário vai
  conter um botão de sumbissão "Buscar" que emite o comando
  "buscar_comentarios".
  """
  return comando_solicitar_pag_buscar_comentarios_IMP.processa(ses, cmd_args)
