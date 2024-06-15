import comando_baixar_video_IMP

def processa(ses, cmd_args):
  """
  Esta função recebe como argumentos em {cmd_args}: 'video' (identificador de vídeo),
  'inicio', e 'fim' (strings que podem ser convertidos para tempos em segundos, fracionários).
  O comando utiliza a função {util_video.extrai_trecho}" se os dois parâmetros são diferentes,
  ou {util_video.extrai_quadro} se os parâmetros são iguais ou o 'fim' é {None}.
  Estas funções, por sua vez, retornam o nome do arquivo que contém o trecho ou quadro solicitado.
  A função {comando_baixar_video.processa} então devolve uma página com um botão "Baixar", que,
  quando clicado, pede para o usuário escolher uma pasta e baixa nela o vídeo escolhido.
  """
  return comando_baixar_video_IMP.processa(ses, cmd_args)
