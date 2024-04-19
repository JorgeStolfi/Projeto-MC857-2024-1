# Este módulo processa o acionamento do botão "Upload Video" do menu principla pelo usuário.

import comando_solicitar_pag_upload_video_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada pelo servidor do sistema para processar o
  comadno HTTP "solicitar_pag_upload_video". Este comando é tipicamente
  emitido pelo browser do usuário quando este aperta o botão "Upload
  Video" no menu geral de uma página qualquer.
  
  O parâmetro {ses} é a sessão de login que emitiu o comando. Não pode
  ser {None}, e deve ser um objeto de tipo {obj_sessao.Classe},
  atualmente aberto.
  
  O parãmetro {cmd_args} é um dicionário que contém os argumentos do
  comando. Atualmente deve ser vazio.
  
  A função normalmente retorna uma página HTML {pag} que inclui o
  formulário para o usuário fazer upload do video. Veja
  {html_pag_upload_video.gera}. Nessa página o usuário poderá
  especificar o título do vídeo e o arquivo (na sua máquina) a ser
  acrescentado ao sistema. A página vai conter um botão de sumbissão
  "Enviar" ou similar que emite o comando 'fazer_upload_video' (vide
  {comando_fazer_upload_video.py}).
  """
  return comando_solicitar_pag_upload_video_IMP.processa(ses, cmd_args)

