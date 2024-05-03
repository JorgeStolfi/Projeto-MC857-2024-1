import comando_ver_conversa_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP "ver_conversa".
  Este comando é tipicamente emitido pelo browser de um usuário quando este
  aperta um botão de "Ver conversa" ou equivalente, para
  examinar os comentários de um vídeo {vid} ou as respostas a um 
  comentário {com}, e as respostas às respostas, etc, recursivamente.
  
  O resultado normal é uma página que mostra todos esses comentários na
  forma de uma árvore como a do "Reddit", onde as respostas de cada
  comentário {com[i]} estão abaixo do mesmo, indentadas.
  
  O parâmetro {ses} deve ser a sessão de login que emitiu o comando.
  Pode ser {None} (significando que o usuário não está logado), ou um
  objeto de tipo {obj_sessao.Classe}, atualmente aberto.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do comando.
  Deve ter um campo com chave 'comentario' ou 'video', cujo valor
  deve ser o identificador "C-{NNNNNNNN}" do comentário {com} ou 
  "V-{NNNNNNNN}" do vídeo {vid}, respectivamente. 
  
  Se o comando falhou (por exemplo, se {cmd_args} não tem nem 'video'
  nem 'comentario', ou o objeto indicado não existe), a função devolve a
  página principal do site com as mensagens de erro apropriadas.
  """
  return comando_ver_conversa_IMP.processa(ses, cmd_args)

