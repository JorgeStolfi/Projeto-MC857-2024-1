import comando_solicitar_pag_alterar_video_IMP

def processa(ses, cmd_args):
  """
  Esta função trata o comando HTTP "solicitar_pag_alterar_video"
  recebido pelo servidor do site. Esse comando tipicamente é emitido
  pelo browser quando o usuário aperta um botão "Alterar" ou equivalente
  para alterar os dados de um vídeo {vid} qualquer. A função retorna uma
  página que permite alterar atributos desse vídeo.
  
  O argumento {ses} é a sessão de login que emitiu o comando. Não pode
  ser {None} e deve ser um objeto de tipo {obj_sessao.Classe}
  representando uma sessão atualmente aberta.
  
  O parâmetro {cmd_args} deve ser um dicionário contendo os argumentos do comando.
  Deve conter um único campo 'video' com o identificador do vídeo a alterar.
  
  O dono da sessão {ses} deve ser um administrador ou o autor do vídeo {vid}.
  
  A função retorna uma página HTML {pag} com o formulário que mostra os
  dados do vídeo {vid}. Veja {html_pag_alterar_video.gera}. Alguns
  atributos do vídeo (como o autor, o nome do arquivo, e suas dimensões)
  serão exibidos mas não poderão ser alterados, nem mesmo pelo
  administrador. A página terá um botão de submissão "Confirmar" ou
  equivalente que emite um comando HTTP "alterar_video".
  """
  return comando_solicitar_pag_alterar_video_IMP.processa(ses, cmd_args)

