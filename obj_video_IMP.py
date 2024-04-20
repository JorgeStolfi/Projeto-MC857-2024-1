import obj_raiz
import obj_video
import obj_usuario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql
import util_identificador
import util_valida_campo

from util_erros import ErroAtrib, erro_prog, mostra

from datetime import datetime, timezone
from math import log
import os
import subprocess
import json
import sys

# Uma instância de {db_obj_tabela} descrevendo a tabela de vídeos:
tabela = None

# Definição interna da classe {obj_video.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id_video, atrs):
    obj_raiz.Classe.__init__(self, id_video, atrs)

# Implementação das funções da interface:

def inicializa_modulo(limpa):
  global tabela

  # Só pode inicializar uma vez:
  if tabela != None: return

  nome_tb = "videos"         # Nome da tabela na base de dados.
  letra_tb = "V"             # Prefixo dos identificadores de vídeos
  classe = obj_video.Classe  # Classe dos objetos (linhas da tabela) na memória.

  # Descrição das colunas da tabela na base de dados:
  # Vide parâmetro {cols} de {db_obj_tabela.cria_tabela}.
  colunas = \
    (
      ( 'autor',   obj_usuario.Classe,  'TEXT',    False ), # Objeto/id do usuário que fez upload.
      ( 'arq',     type("foo"),         'TEXT',    False ), # Nome do arquivo no disco.
      ( 'titulo',  type("foo"),         'TEXT',    False ), # Título do video.
      ( 'data',    type("foo"),         'TEXT',    False ), # Momento do upload do video.
      ( 'duracao', type(418),           'INTEGER', False ), # Duração do video em milissegundos.
      ( 'largura', type(418),           'INTEGER', False ), # Largura de cada frame, em pixels.
      ( 'altura',  type(418),           'INTEGER', False ), # Altura de cada frame, em pixels.
    )

  tabela = db_obj_tabela.cria_tabela(nome_tb, letra_tb, classe, colunas, limpa)
  return

def cria(atrs):
  global tabela
  if tabela.debug: mostra(0, f"  > obj_comentario.cria({str(atrs)}) ...")

  atrs = atrs.copy() # Para alterar só localmente.

  # Data de upload:
  if 'data' in atrs: raise ErroAtrib("data não pode ser especificada")
  data = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %z")
  atrs['data'] = data

  # Obtem as dimensões:
  arq = atrs['arq']
  duracao, largura, altura = obtem_dimensoes_do_arquivo(arq)
  atrs['duracao'] = duracao
  atrs['largura'] = largura
  atrs['altura'] = altura

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  vid = obj_raiz.cria(atrs, tabela, def_obj_mem)
  assert type(vid) is obj_video.Classe
  if tabela.debug: sys.stderr.write(f"  < {obj_video.cria}\n")
  return vid

def muda_atributos(vid, mods_mem):
  global tabela
  if tabela.debug: sys.stderr.write(f"  > {obj_video.muda_atributos} {str(mods_mem)}\n")
  
  assert vid != None and isinstance(vid, obj_video.Classe)

  erros = valida_atributos(vid, mods_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  if tabela.debug: sys.stderr.write(f"    vid antes = {str(vid)}\n")
  obj_raiz.muda_atributos(vid, mods_mem, tabela, def_obj_mem)
  if tabela.debug: sys.stderr.write(f"    vid depois = {str(vid)}\n")

  if tabela.debug: sys.stderr.write(f"  < {obj_video.muda_atributos}\n")
  return

def obtem_identificador(vid):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_identificador(vid)

def obtem_atributos(vid):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_atributos(vid)

def obtem_atributo(vid, chave):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_atributo(vid, chave)

def obtem_usuario(vid):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_atributo(vid, 'autor')

def obtem_data_de_upload(vid):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_atributo(vid, 'data')

def busca_por_identificador(id_vid):
  global tabela
  if id_vid == None: return None
  vid = obj_raiz.busca_por_identificador(id_vid, tabela, def_obj_mem)
  return vid

def busca_por_campo(chave, val):
    global tabela
    lista_ids = obj_raiz.busca_por_campo(chave, val, False, tabela)
    return lista_ids

def busca_por_campos(args, unico):
  global tabela
  return obj_raiz.busca_por_campos(args, unico, tabela)
  
def busca_por_semelhanca(args, unico):
  global tabela
  return obj_raiz.busca_por_semelhanca(args, unico, tabela)

def busca_por_autor(id_autor):
  global tabela
  if id_autor == None: return [].copy()
  lista_ids_vid = obj_raiz.busca_por_campo('autor', id_autor, False, tabela)
  return lista_ids_vid

def busca_por_arquivo(arq):
  global tabela
  id_vid = obj_raiz.busca_por_campo('arq', arq, True, tabela)
  return id_vid
  
def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)

def cria_testes(verb):
  global tabela
  inicializa_modulo(True)
  # Identificadores esperados e atributos dos videos de teste:
  lista_ats = \
    [
      ( "V-00000001", "U-00000001", "eject.mp4", "Ejetar",    ),
      ( "V-00000002", "U-00000002", "fukup.mp4", "Fukushima", ),
      ( "V-00000003", "U-00000001", "pipoc.mp4", "Pipoca",    ),
      ( "V-00000004", "U-00000004", "virus.mp4", "Vírus",     ),
    ]
  for id_vid_esp, id_autor, arq, titulo in lista_ats:
    autor = obj_usuario.busca_por_identificador(id_autor)
    assert autor != None and type(autor) is obj_usuario.Classe
    atrs_cria = {
      'autor': autor,
      'arq': arq,
      'titulo': titulo
    }
    vid = cria(atrs_cria)
    assert vid != None and type(vid) is obj_video.Classe
    id_vid = obj_video.obtem_identificador(vid)
    assert id_vid == id_vid_esp
    autor_conf = obj_video.obtem_usuario(vid)
    id_autor_conf = obj_usuario.obtem_identificador(autor_conf)
    assert autor_conf == autor;
    if verb: sys.stderr.write("  video %s de %s criado\n" % (id_vid, id_autor))
  return

def verifica_criacao(vid, id_vid, atrs):
  return obj_raiz.verifica_criacao(vid, obj_video.Classe, id_vid, atrs, None, tabela, def_obj_mem)

def liga_diagnosticos(val):
  global tabela
  tabela.debug = val
  return

# FUNÇÕES INTERNAS

def obtem_dimensoes_do_arquivo(arq):
  """Examina o arquivo "videos/{arq}" no disco, que deve ter extensão ".mp4"
  e devolve as dimensões do vídeo: duração (em ms), largura, e altura (em pixels).
  Dá erro se não existe arquivo com esse nome."""
  
  #path = "videos/" + arq
  #assert os.path.exists(path)

  #command = [
  #  "ffprobe",
  #  "-v", 
  #  "error", 
  #  "-select_streams",
  #  "v:0",
  #  "-show_entries",
  #  "stream=width,height",
  #  "-of",
  #  "json",
  #  path
  #  ]

  #result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  #data = json.loads(result.stdout)
  
  #duracao = 5000 # !!! Tem que obter do arquivo também !!!
  #largura = data["streams"][0]["width"]
  #altura = data["streams"][0]["height"]
  duracao = 6000
  largura = 640
  altura = 480
  return (duracao, largura, altura)

def valida_atributos(vid, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {vid} é {None}, supõe que um novo objeto de sessão está sendo criado.
  Se {vid} não é {None}, supõe que {atrs} sao alterações a aplicar nessa
  sessão. """
  global tabela
  
  erros = [].copy();

  vid_id = obtem_identificador(vid) if vid is not None else None
  if 'arq' in atrs_mem:
    nome_arq = atrs_mem['arq']
    erros += util_valida_campo.nome_de_arq_video('arq', nome_arq, False)
    if busca_por_arquivo(nome_arq) != vid_id:
      erros.append(f"já existe um arquivo com o nome '{nome_arq}'")
  
  dur_min = 2000; dur_max = 6000000; # Intervalo permitido para duração (ms).
  if 'duracao' in atrs_mem:
    dur = atrs_mem['duracao']
    if dur < dur_min or dur > dur_max:
      erros.append(f"Duração do vídeo inaceitável ({dur} ms, devia estar em {dur_min}..{dur_max} ms)")
  else:
    if vid == None:
      erros.append(f"Duração do vídeo não especificada")
      dur = None
    else:
      alt = obj_video.obtem_atributos(vid)['duracao']
  
  alt_min = 48;   alt_max = 800;     # Intervalo permitido para altura.
  if 'altura' in atrs_mem:
    alt = atrs_mem['altura']
    if alt < alt_min or alt > alt_max:
      erros.append(f"Altura do vídeo inaceitável ({alt} pixels, devia estar em {alt_min}..{alt_max}")
  else:
    if vid == None:
      erros.append(f"Altura do vídeo não especificada")
      alt = None
    else:
      alt = obj_video.obtem_atributos(vid)['altura']
 
  lar_min = 64;   lar_max = 800;     # Intervalo permitido para largura.
  if 'largura' in atrs_mem:
    lar = atrs_mem['largura']
    if lar < lar_min or lar > lar_max:
      erros.append(f"Largura do vídeo inaceitável ({lar} pixels, devia estar em {lar_min}..{lar_max})")
  else:
    if vid == None:
      erros.append(f"Largura do vídeo não especificada")
      lar = None
    else:
      lar = obj_video.obtem_atributos(vid)['largura']
    
  if lar != None and alt != None:
    if abs(log(lar/alt) - log(4/3)) > log(1.35):
      erros.append(f"Razão largura:altura inaceitável ({lar}:{alt}, devia ser ~4:3")
    
  return erros

def def_obj_mem(obj, id_vid, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {obj_video.Classe} com
  identificador {id_vid} e atributos {atrs_SQL}, tais como extraidos
  da tabela de videos. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {obj_video.Classe}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela
  if tabela.debug: mostra(0, "obj_video_IMP.def_obj_mem(" + str(obj) + ", " + id_vid + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, False, db_tabelas_do_sistema.identificador_para_objeto)
    if tabela.debug: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = obj_video.Classe(id_vid, atrs_mem)
  else:
    assert obj.id == id_vid
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, True, db_tabelas_do_sistema.identificador_para_objeto)
    if tabela.debug: mostra(2, "modificando objeto, atrs_mem = " + str(atrs_mem))
    assert type(atrs_mem) is dict
    if len(atrs_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in atrs_mem.items():
      if not chave in obj.atrs:
        erro_prog(f"chave '{chave}' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog(f"tipo do campo '{chave}' incorreto")
      alteravel = False # No futuro pode haver campos alteraveis.
      if (not alteravel) and val != val_velho:
        erro_prog(f"campo '{chave}' não pode ser alterado - val = {str(val)} val_velho = {str(val_velho)}")
      obj.atrs[chave] = val
  if tabela.debug: mostra(2, "obj = " + str(obj))
  return obj
