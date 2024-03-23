import comando_ver_comentarios_IMP

def processa(ses, id_video):
  """
  Esta função é chamada para listar os comentarios de um video.
  
  O parâmetro {ses} é uma sessão atualmente aberta.
  
  O parâmetro {id_video} é o id do video aberto.

  O resultado deve ser uma página com os comentarios encontrados, gerada
  por {html_pag_lista_de_comentarios.gera}.
  """
  return comando_ver_comentarios_IMP.processa(ses, id_video)
