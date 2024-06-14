import comando_ver_grade_de_videos_IMP

def processa(ses, cmd_args):
  """
  Retorna uma página que exibe uma amostra aleatória de
  vídeos, em forma de uma grade de capas.
  
  O parâmetro {ses} deve ser a sessão de login que pediu a página (um objeto de 
  tipo {obj_sessao.Classe}, ainda aberta) ou {None} (se o usuário que pediu não
  está logado).
  
  O parãmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando. Pode ser vazio, ou conter um único argumento 'ordem' cujo
  valor deve ser um string cujo primeiro caractere deve ser "+" ou "-"
  e os caracteres seguintes a chave de ordenação, 'nota', 'vistas', ou 'data'. Por exemplo:
  "+nota" = por nota em ordem crescente, "-vistas" = por visualizações
  em ordem decrescente. Caso a chave 'ordem' esteja ausente ou tenha valor {None},
  a amostra será ordenada de maneira aleatória.
  """
  return comando_ver_grade_de_videos_IMP.processa(ses, cmd_args)
