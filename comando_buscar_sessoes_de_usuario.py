import comando_buscar_sessoes_de_usuario_IMP

def processa(ses, cmd_args):
  """Esta função lista as sessões de um determinado usuário.
   
  O parãmetro {ses} deve {None} ou um objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando, recebidos por HTTP.  Normalmente deve ter um único
  campo 'usuario' com o identificador ("U-{NNNNNNNN}") do usuário
  cujas sessões devem ser listadas.  Se {cmd_args} for vazio ou
  o valor de 'usuario' for {None}, mostra as sessões do usuário 
  da sessão {ses}.

  A função retorna uma página HTML com a lista resumida das sessões."""
  return comando_buscar_sessoes_de_usuario_IMP.processa(ses, cmd_args)
