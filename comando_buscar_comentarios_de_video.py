import comando_buscar_comentarios_de_video_IMP

def processa(ses, cmd_args):
  """Esta função lista os comentarios associados a um determinado video.
   
  O parãmetro {ses} deve ser {None} ou um objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando, recebidos por HTTP.  Deve ter um único
  campo 'video' com o identificador ("V-{NNNNNNNN}") do vídeo
  cujos comentários devem ser listados.

  O resultado será uma página com os comentarios encontrados.
  Veja {html_bloco_lista_de_comentarios.gera}. """
  return comando_buscar_comentarios_de_video_IMP.processa(ses, cmd_args)
