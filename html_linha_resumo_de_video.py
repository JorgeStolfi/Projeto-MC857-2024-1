import html_linha_resumo_de_video_IMP

def gera(vid):
  """Devolve um fragmento HTML que decreve o vídeo {vid}, 
  um objeto da classe {obj_video.Classe}.
  
  O fragmento mostra o id do usuário que fez o upload, nome
  do arquivo no disco, título do vídeo, momento do upload,
  duração em milissegundos, largura e altura de cada frame em pixels,
  e um botão "Ver" que dispara um comando HTTP "ver_video"
  para mostrar o video"""
  return html_linha_resumo_de_video_IMP.gera(vid)
  
