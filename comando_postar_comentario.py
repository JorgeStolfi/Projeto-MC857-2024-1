import comando_postar_comentario_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP
  "postar_comentario". Este comando é tipicamente emitido pelo browser
  do usuário quando este aperta o botão "Postar" num formulário de
  composição de comentário ou equivalente, depois de ter preenchido os
  dados do mesmo.
  
  O parâmetro {ses} é a sessão de login que emitiu o comentário.
  Não pode ser {None}; deve ser um objeto de tipo {obj_sessao.Classe},
  atualmente aberta.
  
  O parâmetro {cmd_args} é um dicionário com os argumentos do 
  comando HTTP.  Dever conter os campos 'video', 'pai', e 'texto'.
  O campo 'data', se existir, será ignorado. O campo 'autor', se
  existir, deve ser o dono da sessão {ses}.
  
  Se os dados forem aceitáveis, a função cria o novo comentário {com},
  acrescentando-o à base de dados; e retorna uma página que exibe o
  comentário. Veja {html_pag_ver_comentario.gera}.
  
  Se os dados não forem aceitáveis, a função devolve uma 
  página com o mesmo formulário de postar comntário, com os 
  campos inicializados com os valoers em {cmd_args}, com uma ou mais mensagens de erro
  adequadas.
  """
  return comando_postar_comentario_IMP.processa(ses, cmd_args)
