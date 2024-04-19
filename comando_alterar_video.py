import comando_alterar_video_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o usuário aperta o botão "Confirmar alterações"
  (ou equivalente) em um formulário para editar dados de um vídeo {vid}, 
  após ter preenchido os campos do mesmo.  Veja html_form_alterar_video.gera}.
  Os novos dados do vídeo com eventuais alterações devem estar definidos
  no dicionário {cmd_args}.   
  
  O parâmetro {ses} não pode ser {None} e deve ser um objeto de tipo
  {obj_sessao.Class}.  A sessão deve estar aberta.   O dicionário {cmd_args}
  deve ter um campo 'video' não nulo, cujo valor é o identificador do
  vídeo {vid} a alterar.
  
  Por enquanto o único campo que pode ser alterado é o 'titulo'
  do vídeo, e só se o dono da sessão {ses} for um 'administrador' 
  ou o autor do vídeo {vid}.
  
  Se os dados forem aceitáveis, a função altera o vídeo {vid} na
  base de dado; e retorna outra página mostrando os dados do
  vídeo, para o usuário conferir. Veja
  {html_pag_ver_video.gera}.

  Se os dados não forem aceitáveis, a função devolve outra vez uma
  página com o formulário de alterar vídeo, porém com os mesmos dados
  {cmd_args} e mais uma ou mais mensagens de erro adequadas."""
  return comando_alterar_video_IMP.processa(ses, cmd_args)
