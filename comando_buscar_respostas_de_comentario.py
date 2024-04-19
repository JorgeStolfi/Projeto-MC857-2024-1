import comando_buscar_respostas_de_comentario_IMP

def processa(ses, cmd_args):
  """Esta função lista os comentarios que são respostas a
  um determinado comentário.
   
  O parãmetro {ses} deve {None} ou um objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando, recebidos por HTTP.  Deve ter um único
  campo 'comentario' com o identificador ("C-{NNNNNNNN}") do comentário
  cujas respostas devem ser listadas.

  O resultado será uma página com os comentarios encontrados.
  Veja {html_bloco_lista_de_comentarios.gera}. """
  return comando_buscar_respostas_de_comentario_IMP.processa(ses, cmd_args)
