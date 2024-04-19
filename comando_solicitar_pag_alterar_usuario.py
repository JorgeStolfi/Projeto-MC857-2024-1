import comando_solicitar_pag_alterar_usuario_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o servidor recebe um comando HTTP
  "solicitar_pag_alterar_usuario".  Tipicamente esse comando é emitido 
  pelo browser de um usuário quando ele aperta o botão "Minha Conta"
  no menu geral de uma página qualquer, ou o administrador aperta
  "Alterar" numa página que mostra os dados de outro usuário.  
  Em qualquer caso, o resultado é uma página que permite alterar alguns dados 
  de um usuário específico {usr}.
  
  O parâmetro {ses} deve ser a sessão de login que emitiu o
  comando. Deve ser um objeto de tipo {obj_sessao.Classe}
  descrevendo uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos
  especificados no comando HTTP.  Se não for vazio, deve conter um único 
  campo com chave 'usuario' cujo valor é o identificador do usuário {usr}
  a alterar (um string "U-{NNNNNNNN}"). 
  
  Se o campo {cmd_args['usuario']} não existir ou for {None}, a função
  entende que o usuário {usr} a alterar é o prórpio dono
  da sessão {ses}.
  
  Em qualquer caso, o dono da sessão {ses} deve ser o próprio {usr}, ou 
  um administrador do site.
  
  A função retorna uma página HTML {pag} com o formulário que mostra os
  dados de um certo usuário {usr}, com campos editáveis.
  Veja {html_pag_alterar_usuario.gera}
  O formulário vai conter um botão de submissão "Alterar"
  que emite o comando "alterar_usuario".
  """
  return comando_solicitar_pag_alterar_usuario_IMP.processa(ses, cmd_args)

