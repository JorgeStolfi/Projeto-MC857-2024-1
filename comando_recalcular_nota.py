import comando_recalcular_nota_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o usuário aperta o botão "Recalcular nota"
  (ou equivalente) em uma página que mostra um vídeo ou comentário.
  
  O parâmetro {ses} não pode ser {None} e deve ser um objeto de tipo
  {obj_sessao.Class}. A sessão deve estar aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário contendo um campo 'comentario'
  cujo valor é o identificador de um comentário {com_id}, ou um campo
  'video' cujo valor é o identificador de um vídeo {vid_id}. Não deve
  ter ambos.
  
  Se os dados forem aceitáveis, esta função recalcula a nota de {vid} ou {com},
  altera esse atributo do objeto, e devolve uma página que mostra esse objeto
  ({html_pag_ver_comentario.gera} ou {html_pag_ver_video.gera}).
  caso contrário, a função devolve uma página de erro."""
  return comando_recalcular_nota_IMP.processa(ses, cmd_args)
