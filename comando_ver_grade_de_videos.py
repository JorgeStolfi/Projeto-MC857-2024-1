import comando_ver_grade_de_videos_IMP

def processa(ses, cmd_args):
  """
  retirna uma página que exibe uma amostra aleatória de
  vídeos, em forma de uma grade de thumbnails.
  
  O parâmetro {ses} deve ser a sessão de login que pediu a página (um objeto de 
  tipo {obj_sessao.Classe}, ainda aberta) ou {None} (se o usuário que pediu não
  está logado).
  
  O parãmetro {cmd_args} deve ser um dicionário com os argumentos
  do comando. Atualmente deve ser um dicionário vazio {{}}.
  """
  return comando_ver_grade_de_videos_IMP.processa(ses, cmd_args)
