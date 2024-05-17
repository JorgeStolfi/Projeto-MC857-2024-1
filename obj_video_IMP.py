import obj_raiz
import obj_video
import obj_usuario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql

import util_identificador
import util_data
import util_titulo_de_video

import cv2
import os
import re
import time
import random

from util_erros import ErroAtrib, erro_prog, mostra

from datetime import datetime, timezone
from math import log, gcd
import os
import subprocess
import json
import sys

# Uma instância de {db_obj_tabela} descrevendo a tabela de vídeos:
tabela = None

# Definição interna da classe {obj_video.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, video_id, atrs):
    obj_raiz.Classe.__init__(self, video_id, atrs)

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
      ( 'titulo',  type("foo"),         'TEXT',    False ), # Título do video.
      ( 'data',    type("foo"),         'TEXT',    False ), # Momento do upload do video.
      ( 'nota',    type(418.1),         'FLOAT',   False ), # Nota média do video (0 a 4).
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
  if not 'data' in atrs:
    data = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    atrs['data'] = data

  # Determina o identificador esperado do vídeo:
  vid_indice = db_obj_tabela.num_entradas(tabela) + 1  # Índice na tabela.
  vid_id = util_identificador.de_indice("V", vid_indice)

  # Nome do arquivo de vídeo:
  nome_arq = f"videos/{vid_id}.mp4"

  if 'conteudo' in atrs:
    # Grava o conteúdo em disco:
    conteudo = atrs['conteudo']
    wr = open(nome_arq, 'wb')
    wr.write(conteudo)
    wr.close()
    atrs.pop('conteudo', None) # Pois não será atributo do objeto.
  else:
    assert os.path.exists(nome_arq), f"Item 'conteudo' ausente e arquivo {nome_arq} não existe"
  
  duracao, largura, altura = obtem_dimensoes_do_arquivo(nome_arq)
  atrs['duracao'] = duracao
  atrs['largura'] = largura
  atrs['altura'] = altura

  # Extrai imagem thumb do video:
  thumb_dir = "thumbs"
  #verifica a existencia do diretório
  if not os.path.exists(thumb_dir):
    os.makedirs(thumb_dir)
  # Carrega o video !!! Má Idéia !!!
  fluxo = cv2.VideoCapture(nome_arq)

  # Obtém o frame 0 do vídeo:
  successo, capa = fluxo.read()
  assert successo, "captura de frame falhou"
  fluxo.release()

  nome_thumb = f"{thumb_dir}/{vid_id}.png"
  cv2.imwrite(nome_thumb, capa)

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  vid = obj_raiz.cria(atrs, tabela, def_obj_mem)
  assert type(vid) is obj_video.Classe

  # Verifica se o identificador foi previsto corretamente:
  assert obj_video.obtem_identificador(vid) == vid_id
  
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

def obtem_autor(vid):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_atributo(vid, 'autor')

def obtem_data_de_upload(vid):
  global tabela
  assert vid != None and isinstance(vid, obj_video.Classe)
  return obj_raiz.obtem_atributo(vid, 'data')

def obtem_objeto(vid_id):
  global tabela
  if vid_id == None: return None
  vid = obj_raiz.obtem_objeto(vid_id, tabela, def_obj_mem)
  return vid

def busca_por_autor(autor_id):
  global tabela
  if autor_id == None: return []
  vid_ids = obj_raiz.busca_por_campo('autor', autor_id, False, tabela)
  return vid_ids

def busca_por_campo(chave, val):
    global tabela
    lista_ids = obj_raiz.busca_por_campo(chave, val, False, tabela)
    return lista_ids

def busca_por_campos(args, unico):
  global tabela
  return obj_raiz.busca_por_campos(args, unico, tabela)
 
def obtem_amostra(n):
  ult_vid_id = obj_video.ultimo_identificador()
  ult_vid_index = int(ult_vid_id[2:])
  sys.stderr.write(f"  last video in system = {ult_vid_id}\n")
  if n > ult_vid_index:
    raise ErroAtrib(f"Número pedido = {n} excessivo, máximo {ult_vid_index}")
  # Lista de vídeos aleatórios:
  res_indices = random.sample(range(1, ult_vid_index + 1), n)
  res_ids = list(map(lambda index: f"V-{index:08d}", res_indices))
  assert len(res_ids) == n
  
  return res_ids

def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)

def cria_testes(verb):
  global tabela
  inicializa_modulo(True)
  # Identificadores esperados e atributos dos videos de teste:
  lista_ats = \
    [
      ( "V-00000001", "U-00000001", "Ejetar de verdade",           3.0, ),
      ( "V-00000002", "U-00000002", "Fukushima #3",                3.6, ),
      ( "V-00000003", "U-00000001", "Pipoca pipocando",            1.0, ),
      ( "V-00000004", "U-00000004", "Vírus do POVRAY",             1.4, ),
      ( "V-00000005", "U-00000006", "Eletrostática",               1.7, ),
      ( "V-00000006", "U-00000004", "Apocalipsevirus",             1.5, ),
      ( "V-00000007", "U-00000002", "Libração da Lua",             2.1, ),
      ( "V-00000008", "U-00000005", "Árvore galhofeira",           0.5, ),
      ( "V-00000009", "U-00000005", "Formigando",                  1.8, ),
      ( "V-00000010", "U-00000005", "Balões errantes",             3.1, ),
      ( "V-00000011", "U-00000002", "Pesca aérea",                 3.8, ),        
      ( "V-00000012", "U-00000001", "Testes nucleares 1952-1957",  3.9, ),
      ( "V-00000013", "U-00000001", "Batata-doce-roxa",            2.1, ),
      ( "V-00000014", "U-00000006", "Moendo isopor",               2.7, ),
      ( "V-00000015", "U-00000006", "Isopor moído",                2.8, ),
    ] 
  for vid_id_esp, autor_id, titulo, nota in lista_ats:
    autor = obj_usuario.obtem_objeto(autor_id)
    assert autor != None and type(autor) is obj_usuario.Classe
    dia = vid_id_esp[-2:]
    data = "2024-01-" + dia + " 08:33:25 UTC"
    atrs_cria = {
        'autor': autor,
        'titulo': titulo,
        'nota': nota,
        'data': data,
      }
    vid = cria(atrs_cria)
    assert vid != None and type(vid) is obj_video.Classe
    vid_id = obj_video.obtem_identificador(vid)
    assert vid_id == vid_id_esp
    autor_conf = obj_video.obtem_autor(vid)
    autor_id_conf = obj_usuario.obtem_identificador(autor_conf)
    assert autor_conf == autor;
    if verb: sys.stderr.write("  video %s de %s criado\n" % (vid_id, autor_id))
  return

def verifica_criacao(vid, vid_id, atrs):
  ignore = [ 'conteudo' ]
  return obj_raiz.verifica_criacao(vid, obj_video.Classe, vid_id, atrs, ignore, tabela, def_obj_mem)

def liga_diagnosticos(val):
  global tabela
  tabela.debug = val
  return

# FUNÇÕES INTERNAS

def obtem_dimensoes_do_arquivo(nome_arq):
  """Examina o arquivo "nome_arq" no disco, que deve ter extensão ".mp4"
  e devolve as dimensões do vídeo: duração (em ms), largura, e altura (em pixels).
  Dá erro se não existe arquivo com esse nome."""

  assert os.path.exists(nome_arq)

  command = [
    "ffprobe",
    "-v", 
    "error", 
    "-select_streams",
    "v:0",
    "-show_entries",
    "stream=width,height,duration",  # Incluindo duração
    "-of",
    "json",
    nome_arq
    ]

  result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
  data = json.loads(result.stdout)

  duracao = int(float(data["streams"][0]["duration"]) * 1000)  # Convertendo para milissegundos
  largura = int(data["streams"][0]["width"])
  altura = int(data["streams"][0]["height"])
  return duracao, largura, altura

def valida_atributos(vid, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {vid} é {None}, supõe que um novo objeto de sessão está sendo criado.
  Se {vid} não é {None}, supõe que {atrs} sao alterações a aplicar nessa
  sessão. """
  global tabela
  
  erros = []

  vid_id = obtem_identificador(vid) if vid is not None else None
  vid_atrs = obj_video.obtem_atributos(vid) if vid != None else { }
  vid_id_msg = " do vídeo {vid_id}" if vid is not None else ""

  # Valida tipos e valores dos atributos fornecidos, quer sejam mutáveis ou não:
  for chave, val in atrs_mem.items():
    if chave == 'autor':
      if not isinstance(val, obj_usuario.Classe):
        erros.append(f"O atributo 'autor'{vid_id_msg} não é um objeto usuário")
    elif chave == 'data':
      nulo_ok = False
      mais_erros = util_data.valida(chave, val, nulo_ok)
      erros += mais_erros
    elif chave == 'titulo':
      nulo_ok = False
      mais_erros = util_titulo_de_video.valida(chave, val, nulo_ok)
      erros += mais_erros
    elif chave == 'nota':
      nota_min = 0
      nota_max = 4
      if not isinstance(val, float):
        erros.append(f"O atributo 'nota'{vid_id_msg} não é um float")
      elif val < nota_min or val > nota_max:
        erros.append(f"O atributo 'nota'{vid_id_msg} = {val} fora da faixa [{nota_min} _ {nota_max}]")
    elif chave == 'duracao' or chave == 'altura' or chave == 'largura':
      if not isinstance(val, int):
        erros.append(f"O atributo '{chave}'{vid_id_msg} não é um inteiro")
    else:
      erros.append(f"Atributo inválido '{chave}' = {val}")

    if vid != None and len(erros) == 0:
      # Tentativa de alterar o campo {chave} para {val}.
      if not chave in { 'nota', 'titulo', }: 
        # O atributo é imutável:
        assert vid_atrs != None and chave in vid_atrs
        if val != vid_atrs[chave]:
          erros.append(f"O atributo '{chave}' do vídeo \"{vid_id}\" não pode ser alterado")
       
  if vid == None and len(erros) == 0:
    # Tentativa de criar um novo objeto.
    # Verifica se todos os atributos estão especificados:
    for col_desc in tabela.colunas:
      chave = col_desc[0] # Chave da coluna da tabela.
      if not chave in atrs_mem:
        erros.append(f"O atributo '{chave}' não foi especificado")

    # Valida as dimensões do novo vídeo:
    mais_erros = valida_dimensoes(atrs_mem['duracao'], atrs_mem['altura'], atrs_mem['largura'])
    erros += mais_erros

  return erros

def valida_dimensoes(duracao, altura, largura):
  """ Valida os atributos 'duracao', 'altura', e 'largura' de 
  um vídeo que está para ser criado.  Exige que os três
  sejam diferentes de {None} e inteiros, com valores e proporções
  em certos intervalos.
  
  Caso os parâmetros sejam válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings)."""
  
  # Intervalo dos atributos
  atrs_val = { 'duracao': duracao, 'altura':  altura, 'largura':  largura, }
  atrs_min = { 'duracao':    2000, 'altura':      48, 'largura':       48, }
  atrs_max = { 'duracao':  600000, 'altura':     800, 'largura':      800, }
  
  erros = []
  
  for chave in 'duracao', 'altura', 'largura':
    val = atrs_val[chave]
    if val == None:
      erros.append(f"O atributo '{chave}' não está definido")
    elif not isinstance(val, int):
      erros.append(f"O atributo '{chave}' = \"{val}\" não é inteiro")
    else:
      val_min = atrs_min[chave]
      val_max = atrs_max[chave]
      if val < val_min or val > val_max:
        erros.append(f"Atributo '{chave}' = {val} fora da faixa [{val_min} _ {val_max}]")

  if len(erros) == 0:
    # Verifica razão lagura:altura:
    # O máximo é um pouco maior que HDTV e celular:
    lar_max = 17  # Nominal.
    alt_min = 9   # Nominal.
    asp_max = lar_max/alt_min

    # Verifica aspecto (razão largura:altura):
    asp = largura/altura
    if abs(log(asp)) > abs(log(asp_max)):
      d = gcd(lar_def,alt_def)
      lar_red, alt_red = lar_def//d, alt_def//d
      if lar_def > alt_def:
        erros.append(f"Razão largura:altura muito grande ({lar_red}:{alt_red}, máximo {lar_max}:{alt_min})")
      else:
        erros.append(f"Razão largura:altura muito pequena ({lar_red}:{alt_red}, mínimo {alt_min}:{lar_max})")
  return erros

def def_obj_mem(obj, vid_id, atrs_SQL):
  """Se {obj} for {None}, cria um novo objeto da classe {obj_video.Classe} com
  identificador {vid_id} e atributos {atrs_SQL}, tais como extraidos
  da tabela de videos. O objeto *NÃO* é inserido na base de dados.

  Se {obj} não é {None}, deve ser um objeto da classe {obj_video.Classe}; nesse
  caso a função altera os atributos de {obj} conforme especificado em
  {atrs_SQL}. A entrada correspondente na base de dados *NÃO* é alterada.

  Em qualquer caso, os valores em {atr_SQL} são convertidos para valores
  equivalentes na memória."""
  global tabela
  if tabela.debug: mostra(0, "obj_video_IMP.def_obj_mem(" + str(obj) + ", " + vid_id + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, False, db_tabelas_do_sistema.identificador_para_objeto)
    if tabela.debug: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = obj_video.Classe(vid_id, atrs_mem)
  else:
    assert obj.id == vid_id
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, tabela.colunas, True, db_tabelas_do_sistema.identificador_para_objeto)
    if tabela.debug: mostra(2, "modificando objeto, atrs_mem = " + str(atrs_mem))
    assert type(atrs_mem) is dict
    if len(atrs_mem) > len(obj.atrs):
      erro_prog("Número excessivo de atributos a alterar")
    for chave, val in atrs_mem.items():
      if not chave in obj.atrs:
        erro_prog(f"Chave '{chave}' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog(f"Tipo do campo '{chave}' incorreto")
      campos_alteraveis = { 'nota', 'titulo', } # No futuro pode haver mais campos alteraveis.
      if not chave in campos_alteraveis and val != val_velho:
        erro_prog(f"Campo '{chave}' não pode ser alterado - val = {str(val)} val_velho = {str(val_velho)}")
      obj.atrs[chave] = val
  if tabela.debug: mostra(2, "obj = " + str(obj))
  return obj
