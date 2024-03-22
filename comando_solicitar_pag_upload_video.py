# Este módulo processa o acionamento do botão "Upload Video" do menu principla pelo usuário.

import comando_solicitar_pag_upload_video_IMP

def processa(ses, cmd_args):
  """Esta função é chamada quando o usuário aperta o botão "Upload Video"
  no menu geral de uma página qualquer.  
  
  A sessão corrente {ses} e o dicionário de argumentos {cmd_args}
  são irrelevantes e podem ser {None}.
  
  A função retorna a página HTML {pag}, com o formulário para o usuário
  fazer upload do video. A página terá um campo editável "Arquivo"
  (chave 'arq') para escolher o arquivo na máquina do usuário, e um
  campo texto editável "Título" (chave 'titulo'). A página terá também
  um botão de sumbissão "Upload" wie emite o comando 'fazer_upload_video'
  (vide {comando_fazer_upload_video.py})."""
  return comando_solicitar_pag_upload_video_IMP.processa(ses, cmd_args)

