import comando_solicitar_pag_alterar_usuario_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o usuário aperta o botão "Minha Conta"
  no menu geral de uma página qualquer.  
  
  A função retorna uma página HTML {pag} com o formulário que mostra os
  dados de um certo usuário {usr}, com campos editáveis.
  O formulário deve conter um botão de submissão "Alterar".
  
  O argumento {ses} deve ser uma sessão atualmente aberta.
  
  O dicionário de argumentos {cmd_args} pode ser vazio ou conter um único 
  campo com chave 'id_usr'. 
  
  Se o campo {cmd_args['id_usr']} não existir ou for {None},
  o formulário vai mostrar os dados do usuário {usr} que é o dono
  da sessão {ses}.
  
  Se o campo {cmd_args['id_usr']} existir e não
  for {None}, o formulário vai mostrar os dados do usuário {usr}
  cujo identificador é {cmd_args['id_usr']}.  Nesse caso, o 
  usuário que é dono da sessão {ses} deve ser o próprio {usr}, ou 
  um administrador do site."""
  return comando_solicitar_pag_alterar_usuario_IMP.processa(ses, cmd_args)

