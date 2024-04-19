import comando_ver_sessao_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servido do site recebe um comando HTTP "ver_sessao".
  Este comando é tipicamente emitido pelo browser do usuário quandoe ste 
  aperta um botão "Ver sessão" ou similar, para examinar os atributos de
  uma determinada sessão um objeto de tipo {obj_sessao.Classe}).
  
  O parâmetro {ses} é a sessão de login corrente, que emitiu o comando.
  Não pode ser {None}; deve ser um objeto de tipo {obj_sessao.Classe} e
  deve estar aberta.
  
  O parãmetro {cmd_args} deve ser um dicionário com os parâmetros do comando.
  Deve conter um único campo com chave 'sessao', cujo valor deve ser o
  identificador (um string da forma "S-{NNNNNNNN}") da sessão {ses_a_ver}
  a ser examinada.  Se esse campo estiver faltando ou for {None},
  {ses-a-ver} será a própria sessão corrente {ses}. 
  
  Se o usuário que é dono da sessão corrente {ses} não for administrador, a sessão
  a examinar {ses_a_ver} deve pertencer a esse usuário.

  Normalmente, a função devolve uma página HTML que mostra os atributos
  da sessão {ses_a_ver}. Veja {html_bloco_dados_de_sessao.gera}. Em caso
  de erro, a função devolve a página principal com as mensagens de erro
  relevantes.
  """
  return comando_ver_sessao_IMP.processa(ses, cmd_args)
