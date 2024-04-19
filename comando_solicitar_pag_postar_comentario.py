import comando_solicitar_pag_postar_comentario_IMP

def processa(ses, cmd_args):
  """
  Esta função trata o comando HTTP "solicitar_pag_postar_comentario"
  recebido pelo servidor do site. Esse comando tipicamente é emitido
  pelo browser quando o usuário aperta o botão "Comentar" (ou similar)
  em alguma página que mostra um vídeo, ou "Responder" (ou similar) em
  alguma página que mostra um comentário anteriormente postado.
  
  O argumento {ses} não pode ser {None} e deve ser um objeto de
  tipo {obj_sessao.Classe} representando uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário contendo os argumentos
  do comando. Pode conter um único campo 'video' com o identificador do
  vídeo ao qual o novo comentário deve ser associado. O dono da sessão
  {ses} não preoisa ser o autor do vídeo.
  
  Alternativamente, {cmd_args} pode conter um único campo 'pai' com o
  identificador do comentário do qual o novo comentário será uma
  resposta. O dono da sessão {ses} não precisa ser o autor do comentário
  pai nem do vídeo a que este está associado.
  
  A função retorna uma página HTML {pag} com o formulário onde o usuário
  pode digitar o texto do comentário. Veja {html_pag_postar_comentario.gera}.
  A página terá um botão de submissão "Enviar" ou
  equivalente que emite um comando HTTP "postar_comentario".
  """
  return comando_solicitar_pag_postar_comentario_IMP.processa(ses, cmd_args)

