import comando_ver_comentario_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando o servidor recebe um comando HTTP "ver_comentario".
  Este comando é tipicamente emitido pelo browser de um usuário quando este
  aperta um botão de "Ver comentário" ou equivalente, para
  examinar um comentário {com}.
  
  O parâmetro {ses} deve ser a sessão de login que emitiu o comando.
  Pode ser {None} (significando que o usuário não está logado), ou um
  objeto de tipo {obj_sessao.Classe}, atualmente aberto.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do comando.
  Deve ter um único campp com chave 'comentario', cujo valor
  deve ser o identificador "C-{NNNNNNNN}" do comentário {com} a ver. 
  
  Normalmente a função devolve uma página que
  exibe o comentario, criada por {html_pag_ver_comentario.gera}. Se o comando
  falhou (por exemplo, se o campo {cmd_args['comentario']} está faltando
  ou é {None}, ou o vídeo indicado não existe), devolve a página principal do site
  com as mensagens de erro apropriadas.
  """
  return comando_ver_comentario_IMP.processa(ses, cmd_args)

