import comando_solicitar_pag_buscar_videos_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP
  "buscar_videos". Geralmente esse comando é emitido pelo browser de um
  usuário quando ele aperta o botão "Buscar Vídeos" no menu principal. A
  função devolve uma página com campos editáveis e botões para fazer a
  busca.

  O parâmetro {ses} deve ser a sessão de login que emitiu o comando.
  Pode ser {None} (indicando que o usuário não está logado) ou um objeto
  de tipo {obg_sessao.Classe}, atualmente aberta. Não precisa ser de 
  administrador.
  
  O parâmetro {cmd_args} deve ser {None} ou um dicionário com os 
  argumentos do comando HTTP. Atualmente deve ser vazio.

  A função retorna uma página HTML {pag} com o formulário que mostra
  atributos que podem ser usados para busca de vídeos, com valores
  editáveis. Veja {html_pag_buscar_videos.gera}. O formulário vai conter
  também um botão de sumbissão "Buscar" que emite o comando
  "buscar_videos".
  """
  return comando_solicitar_pag_buscar_videos_IMP.processa(ses, cmd_args)
