import util_video_IMP

def grava_arquivos(vid_id,conteudo):
  """Grava os bytes {conteudo} no arquivo "videos/{vid_id}.mp4". Se
  {conteudo} for {None}, o arquivo já deve existir. Em qualquer caso,
  também extrai a imagem de capa "capas/{vid_id}.png" e um certo número
  {NQ} de quadros-indice "quadros/{vid_id}-{NNN}.png" para {NNN}
  variando de 0 a {NQ-1}. Devolve as dimensões {duracao} (ms), {largura}
  (px), {altura} (px), e o número de quadros {NQ}."""
  return util_video_IMP.grava_arquivos(vid_id, conteudo)
  
def extrai_trecho(vid_id,inicio,fim):
  """Extrai do arquivo "videos/{vid_id}.mp4" um trecho contido entre os tempos {inicio} e {fim},
  que devem ser {float}s em segundos e frações, com {0 <= inicio < fim}.  
  Supõe que o {fim} não excede a duração do vídeo. Grava o arquivo
  em "videos/{vid_id}-{RRRRRRRR}.mp4" onde {RRRRRRRRR} é uma cadeia aleatória de 8 algarismos.
  Devolve o nome desse arquivo."""
  return util_video_IMP.extrai_trecho(vid_id,inicio,fim)
  
def extrai_quadro(vid_id,tempo):
  """Extrai do arquivo "videos/{vid_id}.mp4" um quadro no momento {tempo} dado.
 O {tempo} deve ser um {float} não-negativo em segundos e fração.  
  Supõe que o {tempo} não excede a duração do vídeo.  Grava o quadro
  em "quadros/{vid_id}-{RRRRRRRR}.mp4" onde {RRRRRRRRR} é uma cadeia aleatória de 8 algarismos.
  Devolve o nome desse arquivo."""
  return util_video_IMP.extrai_quadro(vid_id,tempo)

def verifica_arquivo(vid_id):
  """Verifica se o arquivo "videos/{vid_id}.mp4" foi gravado.
  Em caso afirmativo, devolve {True}. Em caso negativo, imprime 
  mensagem de erro."""
  return util_video_IMP.verifica_arquivo(vid_id)

def obtem_dimensoes_do_arquivo(arq_video):
  """Examina o arquivo {arq_video} no disco, que deve ter extensão ".mp4"
  e devolve as dimensões do vídeo: duração (em ms), largura, e altura (em pixels).
  Dá erro se não existe arquivo com esse nome."""
  return util_video_IMP.obtem_dimensoes_do_arquivo(arq_video)
  
def extrai_capa(vid_id):
  """Extrai o primeiro quadro do arquivo "videos/{vid_id}.mp4",
  supostamente a capa, e grava como "capas/{vid_id}.png"."""
  return util_video_IMP.extrai_capa(vid_id)

def verifica_capa(vid_id):
  """Verifica se o arquivo "capas/{vid_id}.png" foi gravado.
  Em caso afirmativo, devolve {True}. Em caso negativo, implrime 
  mensagem de erro."""
  return util_video_IMP.verifica_capa(vid_id)
  
def extrai_quadros_indice(vid_id,duracao,largura,altura):
  """Extrai um certo número {NQ} de quadros igualmente espaçados 
  do vídeo, com altura padronizada, e grava em "quadros/{vid_id}-{NNN}.png" onde 
  {NNN} é um índice de 3 algarismos que varia de 0 até {NQ-1}.
  Devolve o valor de {NQ}."""
  return util_video_IMP.extrai_quadros_indice(vid_id,duracao,largura,altura)

def verifica_quadros(vid_id):
  """Verifica se os quadros-índice "quadros/{vid_id}-{NNN}.png" existem.
  Em caso afirmativo, devolve {True}. Em caso negativo, implrime 
  mensagem de erro."""
  return util_video_IMP.verifica_quadros(vid_id)
