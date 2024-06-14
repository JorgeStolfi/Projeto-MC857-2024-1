import obj_raiz
import obj_video
import obj_usuario
import obj_comentario

import db_obj_tabela
import db_tabelas_do_sistema
import db_conversao_sql

import util_identificador
import util_data
import util_booleano
import util_titulo_de_video
import util_video

from util_erros import ErroAtrib, erro_prog, mostra

import re
import time
import random
import os
import sys
from datetime import datetime, timezone
from math import log, gcd, sin

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
      ( 'autor',     obj_usuario.Classe,  'TEXT',    False ), # Objeto/id do usuário que fez upload.
      ( 'titulo',    type("foo"),         'TEXT',    False ), # Título do video.
      ( 'nota',      type(418.1),         'FLOAT',   False ), # Nota média do video (0 a 4).
      ( 'vistas',    type(418),           'INTEGER', False ), # Número de vezes que foi assistido.
      ( 'bloqueado', type(False),         'INTEGER', False ), # O vídeo foi bloqueado.
      ( 'data',      type("foo"),         'TEXT',    False ), # Data e hora do upload do video.
      ( 'duracao',   type(418),           'INTEGER', False ), # Duração do video em milissegundos.
      ( 'largura',   type(418),           'INTEGER', False ), # Largura de cada frame, em pixels.
      ( 'altura',    type(418),           'INTEGER', False ), # Altura de cada frame, em pixels.
    )

  tabela = db_obj_tabela.cria_tabela(nome_tb, letra_tb, classe, colunas, limpa)
  return

def cria(atrs):
  global tabela
  if tabela.debug: mostra(0, f"  > obj_comentario.cria({str(atrs)}) ...")

  erros = []
  
  atrs = atrs.copy() # Para alterar só localmente.

  # Data de upload:
  if not 'data' in atrs:
    data = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    atrs['data'] = data

  # Determina o identificador esperado do vídeo:
  vid_indice = db_obj_tabela.num_entradas(tabela) + 1  # Índice na tabela.
  vid_id = util_identificador.de_indice("V", vid_indice)

  conteudo = atrs.pop('conteudo', None)

  duracao, largura, altura, NQ = util_video.grava_arquivos(vid_id, conteudo)
  assert NQ == 6 # Por enquanto.
  
  atrs['duracao'] = duracao
  atrs['largura'] = largura
  atrs['altura'] = altura
  
  erros += valida_atributos(None, atrs)
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
  lista_ids = busca_por_campos( { chave: val }, unico = False)
  return lista_ids

def busca_por_campos(args, unico):
  global tabela
  args = obj_raiz.converte_campo_em_padrao(args, 'titulo');
  return obj_raiz.busca_por_campos(args, unico, tabela)
 
def obtem_amostra(n):
  global tabela

  ult_vid_id = obj_video.ultimo_identificador()
  ult_vid_index = int(ult_vid_id[2:])

  # Caso o número de vídeos seja insucificente, devolve uma lista menor:
  if n > ult_vid_index: n = ult_vid_index

  res_indices = random.sample(range(1, ult_vid_index + 1), n)
  res_ids = list(map(lambda index: f"V-{index:08d}", res_indices))
  return res_ids

def ordena_identificadores(lista_ids, chave, ordem):
  res_ids = lista_ids.copy()
  if ordem != 0:
    pares = []
    for vid_id in res_ids:
      vid = obj_video.obtem_objeto(vid_id)
      assert vid != None
      nota = obj_video.obtem_atributo(vid, chave)
      pares.append(( vid_id, nota,))
    if ordem == +1:
      decr = False
    elif ordem == -1:
      decr = True
    else:
      assert False, f"parâmetro inválido ordem = {ordem}"
    pares.sort(key = lambda x: x[1], reverse = decr)
    res_ids = [ x[0] for x in pares ]
  
  return res_ids

def ultimo_identificador():
  global tabela
  return obj_raiz.ultimo_identificador(tabela)

def cria_testes(verb):
  global tabela

  inicializa_modulo(True)
  
  if tabela.debug: sys.stderr.write("> {obj_video.cria_testes}\n")

  # Identificadores esperados e atributos dos videos de teste:
  lista_ats = \
    [
      ( "V-00000001", "U-00000001", "Ejetar de verdade",           3.0, True,  ),
      ( "V-00000002", "U-00000002", "Fukushima #3",                3.6, False,  ),
      ( "V-00000003", "U-00000001", "Pipoca pipocando",            1.0, False,  ),
      ( "V-00000004", "U-00000004", "Vírus do POVRAY",             1.4, False,  ),
      ( "V-00000005", "U-00000006", "Eletrostática",               1.7, False,  ),
      ( "V-00000006", "U-00000004", "Apocalipsevirus",             1.5, True,   ),
      ( "V-00000007", "U-00000002", "Libração da Lua",             2.1, False,  ),
      ( "V-00000008", "U-00000005", "Árvore galhofeira",           0.5, False,  ),
      ( "V-00000009", "U-00000005", "Formigando",                  1.8, False,  ),
      ( "V-00000010", "U-00000005", "Balões errantes",             3.1, False,  ),
      ( "V-00000011", "U-00000002", "Pesca aérea",                 3.8, False,  ),        
      ( "V-00000012", "U-00000001", "Testes nucleares 1952-1957",  3.9, False,  ),
      ( "V-00000013", "U-00000001", "Batata-doce-roxa",            2.1, False,  ),
      ( "V-00000014", "U-00000006", "Moendo isopor",               2.7, False,  ),
      ( "V-00000015", "U-00000006", "Isopor moído",                2.8, False,  ),
      ( "V-00000016", "U-00000006", "Octopus vulgaris",            2.8, False,  ),
      ( "V-00000017", "U-00000006", "Engenho engenhoso",           2.8, True,   ),
      ( "V-00000018", "U-00000006", "Teino de sumo",               2.8, False,  ),
      ( "V-00000019", "U-00000006", "Beroe abyssicola",            2.8, False,  ),
      ( "V-00000020", "U-00000006", "Stentor muelleri",            2.8, False,  ),
      ( "V-00000021", "U-00000006", "Huygens descendo em Titã",    2.8, False,  ),
      ( "V-00000022", "U-00000006", "Nadando com orcas",           2.8, False,  ),
      ( "V-00000023", "U-00000006", "Erupção do Taal",             2.8, False,  ),
      ( "V-00000024", "U-00000006", "Formiga vermelha",            2.8, False,  ),
    ] 
  for vid_id_esp, autor_id, titulo, nota, bloqueado in lista_ats:
    if tabela.debug: sys.stderr.write(f"  criando {vid_id_esp}\n")
    autor = obj_usuario.obtem_objeto(autor_id)
    assert autor != None and type(autor) is obj_usuario.Classe
    dia = vid_id_esp[-2:]
    data = "2024-01-" + dia + " 08:33:25 UTC"
    vistas = int(100*(1 + sin(int(vid_id_esp[2:]))))
    atrs_cria = {
        'autor': autor,
        'titulo': titulo,
        'nota': nota,
        'vistas': vistas,
        'data': data,
        'bloqueado': bloqueado,
      }
    vid = cria(atrs_cria)
    assert vid != None and type(vid) is obj_video.Classe
    vid_id = obj_video.obtem_identificador(vid)
    assert vid_id == vid_id_esp
    autor_conf = obj_video.obtem_autor(vid)
    autor_id_conf = obj_usuario.obtem_identificador(autor_conf)
    assert autor_conf == autor;
    if verb: sys.stderr.write("  video %s de %s criado\n" % (vid_id, autor_id))
  
  if tabela.debug: sys.stderr.write("< {obj_video.cria_testes}\n")
  return

def verifica_criacao(vid, vid_id, atrs):
  ignore = [ 'conteudo' ]
  ok = obj_raiz.verifica_criacao(vid, obj_video.Classe, vid_id, atrs, ignore, tabela, def_obj_mem)
  if ok: ok = util_video.verifica_arquivo(vid_id)
  if ok: ok = util_video.verifica_capa(vid_id)
  if ok: ok = util_video.verifica_quadros(vid_id)
  return ok

def liga_diagnosticos(val):
  global tabela
  tabela.debug = val
  return

# FUNÇÕES INTERNAS

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
    elif chave == 'bloqueado':
      nulo_ok = False
      mais_erros = util_booleano.valida(chave, val, nulo_ok)
      erros += mais_erros
    elif chave == 'titulo':
      nulo_ok = False
      mais_erros = util_titulo_de_video.valida(chave, val, nulo_ok)
      erros += mais_erros
    elif chave == 'nota':
      nota_min = 0.0
      nota_max = 4.0
      if not isinstance(val, float):
        erros.append(f"O atributo 'nota'{vid_id_msg} não é um float")
      elif val < nota_min or val > nota_max:
        erros.append(f"O atributo 'nota'{vid_id_msg} = {val} fora da faixa [{nota_min:.0f} _ {nota_max:.0f}]")
    elif chave == 'vistas':
      if not isinstance(val, int):
        erros.append(f"O atributo 'vistas'{vid_id_msg} não é um int")
      elif val < 0:
        erros.append(f"O atributo 'vistas'{vid_id_msg} = {val} é negativo")
    elif chave == 'duracao' or chave == 'altura' or chave == 'largura':
      if not isinstance(val, int):
        erros.append(f"O atributo '{chave}'{vid_id_msg} não é um inteiro")
    else:
      erros.append(f"Atributo inválido '{chave}' = {val}")

    if vid != None and len(erros) == 0:
      # Tentativa de alterar o campo {chave} para {val}.
      campos_alteraveis = { 'nota', 'vistas', 'titulo', 'bloqueado', }
      if not chave in campos_alteraveis: 
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
  
  # Intervalo dos atributos
  atrs_val = { 'duracao': duracao, 'altura':  altura, 'largura':  largura, }
  atrs_min = { 'duracao':    2000, 'altura':      48, 'largura':       48, }
  atrs_max = { 'duracao':  600000, 'altura':     800, 'largura':      800, }
  
  erros = []
  
  for chave in atrs_val.keys():
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
      campos_alteraveis = { 'nota', 'vistas', 'titulo', 'bloqueado', }
      if not chave in campos_alteraveis and val != val_velho:
        erro_prog(f"Campo '{chave}' não pode ser alterado - val = {str(val)} val_velho = {str(val_velho)}")
      obj.atrs[chave] = val
  if tabela.debug: mostra(2, "obj = " + str(obj))
  return obj

