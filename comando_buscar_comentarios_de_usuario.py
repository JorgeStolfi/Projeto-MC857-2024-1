import comando_buscar_comentarios_de_usuario_IMP

def processa(ses, cmd_args):
  """Esta função lista os comentarios postados por um determinado usuário.
   
  O parãmetro {ses} deve {None} ou um objeto {obj_sessao.Classe}
  de uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário com os argumentos do
  comando, recebidos por HTTP. Normalmente deve ter um único
  campo 'usuario' com o identificador ("U-{NNNNNNNN}") do usuário 
  cujos comentários devem ser listados.  Se {cmd_args} for vazio ou
  o valor de 'usuario' for {None}, mostra os comentários do usuário 
  da sessão {ses}.

  O resultado será uma página com os comentarios encontrados.
  Veja {html_bloco_lista_de_comentarios.gera}. """
  return comando_buscar_comentarios_de_usuario_IMP.processa(ses, cmd_args)
