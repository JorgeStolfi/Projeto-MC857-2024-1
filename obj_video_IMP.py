import obj_raiz
import obj_video
import obj_usuario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql
import util_identificador
import util_valida_campo

# import cv2
import os
import re

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
  data = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
  atrs['data'] = data

  # Determina o identificador esperado do vídeo:
  ind_vid = db_obj_tabela.num_entradas(tabela) + 1  # Índice na tabela.
  id_vid = util_identificador.de_indice("V", ind_vid)

  # Nome do arquivo de vídeo:
  nome_arq = f"videos/{id_vid}.mp4"

  if 'conteudo' in atrs:
    # Grava o conteúdo em disco:
    conteudo = atrs['conteudo']
    wr = open(nome_arq, 'wb')
    wr.write(conteudo)
    wr.close()
    atrs.pop('conteudo') # Pois não será atributo do objeto.
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
  # fluxo = cv2.VideoCapture(nome_arq)

  # Obtém o frame 0 do vídeo:
  # successo, capa = fluxo.read()
  # assert successo, "captura de frame falhou"
  # fluxo.release()

  nome_thumb = f"{thumb_dir}/{id_vid}.png"
  # cv2.imwrite(nome_thumb, capa)

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  vid = obj_raiz.cria(atrs, tabela, def_obj_mem)
  assert type(vid) is obj_video.Classe

  # Verifica se o identificador foi previsto corretamente:
  assert obj_video.obtem_identificador(vid) == id_vid
  
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

def obtem_objeto(id_vid):
  global tabela
  if id_vid == None: return None
  vid = obj_raiz.obtem_objeto(id_vid, tabela, def_obj_mem)
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
 
def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)

def cria_testes(verb):
  global tabela
  inicializa_modulo(True)
  # Identificadores esperados e atributos dos videos de teste:
  lista_ats = \
    [
      ( "V-00000001", "U-00000001", "Ejetar",    ),
      ( "V-00000002", "U-00000002", "Fukushima", ),
      ( "V-00000003", "U-00000001", "Pipoca",    ),
      ( "V-00000004", "U-00000004", "Vírus",     ),
    ]
  for id_vid_esp, id_autor, titulo in lista_ats:
    autor = obj_usuario.obtem_objeto(id_autor)
    assert autor != None and type(autor) is obj_usuario.Classe
    atrs_cria = {
      'autor': autor,
      'titulo': titulo
    }
    vid = cria(atrs_cria)
    assert vid != None and type(vid) is obj_video.Classe
    id_vid = obj_video.obtem_identificador(vid)
    assert id_vid == id_vid_esp
    autor_conf = obj_video.obtem_autor(vid)
    id_autor_conf = obj_usuario.obtem_identificador(autor_conf)
    assert autor_conf == autor;
    if verb: sys.stderr.write("  video %s de %s criado\n" % (id_vid, id_autor))
  return

def verifica_criacao(vid, id_vid, atrs):
  ignore = [ 'conteudo' ]
  return obj_raiz.verifica_criacao(vid, obj_video.Classe, id_vid, atrs, ignore, tabela, def_obj_mem)

def valida_titulo(chave, val, nulo_ok, parcial):

  # Erro crasso de programa, não deveria acontecer:
  assert val == None or type(val) is str, "argumento de tipo inválido"
  
  # !!! Tratar o parâmetro {parcial} !!!
 
  erros = [].copy() 

  if val is None:
    if not nulo_ok: erros.append(f"campo '{chave}' não pode ser omitido")
  else:
    n = len(val)
    nmin = 10
    nmax = 60
    if len(val) < nmin:
      erros.append(f"campo '{chave}' = \"{str(val)}\" muito curto ({n} caracteres, mínimo {nmin})")
    elif len(val) > nmax:
      erros.append(f"campo '{chave}' = \"{str(val)}\" muito longo ({n} caracteres, máximo {nmax})")

    if not val[0].isupper():
      erros.append(f"campo '{chave}' = \"{str(val)}\" a primeira letra deve ser maiúscula")

    if val[-1].isspace():
      erros.append(f"campo '{chave}' = \"{str(val)}\" não pode terminar com espaços")

    if "  "  in val:
      erros.append(f"campo '{chave}' = \"{str(val)}\" não pode conter dois espaços seguidos")

    # Caracterers válidos ISO-Latin-1:
    padrao = r'^[A-Za-z0-9À-ÖØ-öø-ÿ!"#$%&\'()*+,\-./:;<=>?@\[\]^_`{|}~\s]+$'
    if not re.match(padrao, val):
      erros.append(f"campo '{chave}' = \"{str(val)}\" contém caracteres não permitidos")

  return erros

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
  
  erros = [].copy();

  vid_id = obtem_identificador(vid) if vid is not None else None

  if vid != None:
    # Os campos de {atrs} são alterações a aplicar no vídeo {vid}.
    for chave in 'duracao', 'altura', 'largura':
      if chave in atrs_mem:
        val_novo = atrs_mem[chave]
        val_prev = obj_video.obtem_atributos(vid)[chave]
        if val_novo != val_prev:
          erros.append(f"Atributo {chave} do vídeo {vid_id} não pode ser alterado")
  else:
    # Os campos de {atrs} são os atributos de um vídeo sendo criado:
    atrs_min = { 'duracao':   2000, 'altura':  48, 'largura':  48, }
    atrs_max = { 'duracao': 600000, 'altura': 800, 'largura': 800, }
    for chave in 'duracao', 'altura', 'largura':
      if chave in atrs_mem:
        val_def = atrs_mem[chave]
        val_min = atrs_min[chave]
        val_max = atrs_max[chave]
        if val_def < val_min:
          erros.append(f"Atributo {chave} do vídeo muito pequeno ({val_def}, mínimo {val_min})")
        elif val_def > val_max:
          erros.append(f"Atributo {chave} do vídeo muito grande ({val_def}, máximo {val_max})")
      else:
        erros.append(f"Atributo {chave} do vídeo não está especificado")

    # Razão lagura:altura máxima, um pouco maior que HDTV e celular:
    lar_max = 17  # Nominal.
    alt_min = 9   # Nominal.
    asp_max = lar_max/alt_min
    
    if len(erros) == 0:
      # Verifica aspecto (razão largura:altura):
      lar_def = atrs_mem['largura']
      alt_def = atrs_mem['altura']
      asp_def = lar_def/alt_def
      if abs(log(asp_def)) > abs(log(asp_max)):
        d = gcd(lar_def,alt_def)
        lar_red, alt_red = lar_def//d, alt_def//d
        if lar_def > alt_def:
          erros.append(f"Razão largura:altura muito grande ({lar_red}:{alt_red}, máximo {lar_max}:{alt_min})")
        else:
          erros.append(f"Razão largura:altura muito pequena ({lar_red}:{alt_red}, mínimo {alt_min}:{lar_max})")

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
      alteravel = (chave == 'titulo') # No futuro pode haver mais campos alteraveis.
      if (not alteravel) and val != val_velho:
        erro_prog(f"campo '{chave}' não pode ser alterado - val = {str(val)} val_velho = {str(val_velho)}")
      obj.atrs[chave] = val
  if tabela.debug: mostra(2, "obj = " + str(obj))
  return obj
