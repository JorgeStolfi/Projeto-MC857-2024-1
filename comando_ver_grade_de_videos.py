import comando_ver_grade_de_videos_IMP

def processa(ses, cmd_args):
  """
  Retorna uma página que exibe uma amostra aleatória de
  vídeos, em forma de uma grade de thumbnails.
  
  O parâmetro {ses} deve ser a sessão de login que pediu a página (um objeto de 
  tipo {obj_sessao.Classe}, ainda aberta) ou {None} (se o usuário que pediu não
  está logado).
  
  O parãmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando. Pode ser vazio, ou conter um único argumento 'ordem' cujo
  valor deve ser um string conversível para inteiro que especifica a
  ordenação dos vídeos por nota: "+1" = crescente, "-1" = decrescente,
  "0" = aleatória (o default).
  """
  return comando_ver_grade_de_videos_IMP.processa(ses, cmd_args)
