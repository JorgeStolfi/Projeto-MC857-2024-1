import comando_buscar_videos_de_usuario_IMP

def processa(ses, cmd_args):
  """Esta função lista os vídeos postados por um determinado usuário.
  
  O parãmetro {ses} deve {None} ou um objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando, recebidos por HTTP. Normalmente deve ter um único
  campo 'usuario' com o identificador ("U-{NNNNNNNN}") do usuário 
  cujos videos devem ser listados.  Se {cmd_args} for vazio ou
  o valor de 'usuario' for {None}, mostra as sessões do usuário 
  da sessão {ses}.

  A função retorna uma página HTML com a lista resumida dos vídeos."""
  return comando_buscar_videos_de_usuario_IMP.processa(ses, cmd_args)
