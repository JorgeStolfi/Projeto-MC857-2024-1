import obj_raiz
import obj_video
import obj_usuario

import db_tabela_generica
import db_tabelas
import db_conversao_sql
import util_identificador
import util_valida_campo; from util_valida_campo import ErroAtrib
from util_testes import erro_prog, mostra
import sys

from datetime import datetime, timezone

# VARIÁVEIS GLOBAIS DO MÓDULO

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {obj_video.Classe} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

nome_tb = "videos"
  # Nome da tabela na base de dados.

letra_tb = "V"
  # Prefixo comum dos identificadores de video.

colunas = None
  # Descrição das colunas da tabela na base de dados.

vid_debug = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

# Definição interna da classe {obj_usuario.Classe}:

class Classe_IMP(obj_raiz.Classe):

  def __init__(self, id_video, atrs):
    global cache, nome_tb, letra_tb, colunas
    obj_raiz.Classe.__init__(self, id_video, atrs)


# Implementações:

def inicializa_modulo(limpa):
  global cache, nome_tb, letra_tb, colunas
  colunas = \
    (
      ( "usr",          obj_usuario.Classe,     'TEXT',    False ),  # Objeto/id do usuário que fez upload.
      ( "arq",          type("foo"),            'TEXT',    False ),  # Nome do arquivo no disco.
      ( "titulo",       type("foo"),            'TEXT',    False ),  # Título do video.
      ( "data",         type("foo"),            'TEXT',    False ),  # Momento do upload do video.
      ( "duracao",      type(418),              'INTEGER', False ),  # Duração do video em milissegundos.
      ( "largura",      type(418),              'INTEGER', False ),  # largura de cada frame, em pixels.
      ( "altura",       type(418),              'INTEGER', False ),  # atura de cada frame, em pixels.
    )
  if limpa:
    db_tabela_generica.limpa_tabela(nome_tb, colunas)
  else:
    db_tabela_generica.cria_tabela(nome_tb, colunas)

def cria(atrs):
  global cache, nome_tb, letra_tb, colunas

  erros = valida_atributos(None, atrs)
  if len(erros) != 0: raise ErroAtrib(erros)

  vid = obj_raiz.cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  assert type(vid) is obj_video.Classe
  return vid

def obtem_identificador(vid):
  global cache, nome_tb, letra_tb, colunas
  assert (vid != None) and type(vid) is obj_video.Classe
  return obj_raiz.obtem_identificador(vid)

def obtem_atributos(vid):
  global cache, nome_tb, letra_tb, colunas
  assert (vid != None) and type(vid) is obj_video.Classe
  return obj_raiz.obtem_atributos(vid)

def obtem_atributo(vid, chave):
  global cache, nome_tb, letra_tb, colunas
  assert (vid != None) and type(vid) is obj_video.Classe
  return obj_raiz.obtem_atributo(vid, chave)

def obtem_usuario(vid):
  global cache, nome_tb, letra_tb, colunas
  assert (vid != None) and type(vid) is obj_video.Classe
  return obj_raiz.obtem_atributo(vid, 'usr')

def obtem_data_de_upload(vid):
  global cache, nome_tb, letra_tb, colunas
  assert (vid != None) and type(vid) is obj_video.Classe
  return obj_raiz.obtem_atributo(vid, 'data')

def busca_por_identificador(id_vid):
  global cache, nome_tb, letra_tb, colunas
  if id_vid == None: return None
  vid = obj_raiz.busca_por_identificador(id_vid, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return vid

def busca_por_campo(chave, val):
    global cache, nome_tb, letra_tb, colunas
    lista_ids = obj_raiz.busca_por_campo(chave, val, False, cache, nome_tb, letra_tb, colunas)
    return lista_ids

def busca_por_usuario(id_usr):
  global cache, nome_tb, letra_tb, colunas
  if id_usr == None: return [].copy()
  lista_ids_vid = obj_raiz.busca_por_campo('usr', id_usr, False, cache, nome_tb, letra_tb, colunas)
  return lista_ids_vid

def busca_por_arquivo(arq):
  global cache, nome_tb, letra_tb, colunas
  id_vid = obj_raiz.busca_por_campo('arq', arq, True, cache, nome_tb, letra_tb, colunas)
  return id_vid

def muda_atributos(vid, atrs_mod_mem):
  global cache, nome_tb, letra_tb, colunas

  erros = valida_atributos(vid, atrs_mod_mem)
  if len(erros) != 0: raise ErroAtrib(erros)

  obj_raiz.muda_atributos(vid, atrs_mod_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  return

def cria_testes(verb):
  global cache, nome_tb, letra_tb, colunas
  inicializa_modulo(True)
  # Identificador de usuários e cookie de cada sessão:
  lista_ats = \
    [
      ( "U-00000001", "eject ", "Ejetando o floppy",  "2024-03-09 19:07:49.14 UTC",   6200, 460, 344, ), # V-00000000
      ( "U-00000002", "fukup ", "Explosão de reator", "2024-03-09 19:08:13.11 UTC",  13760, 640, 360, ), # V-00000001
      ( "U-00000001", "pipoc ", "Pipoca",             "2024-03-09 19:08:27.92 UTC",   3200, 384, 384, ), # V-00000002
      ( "U-00000004", "virus ", "Vírus",              "2024-03-06 14:56:40.24 UTC",   3000, 800, 800, ), # V-00000003
    ]
  for id_usr, arq, titulo, data, duracao, largura, altura in lista_ats:
    usr = obj_usuario.busca_por_identificador(id_usr)
    assert usr != None and type(usr) is obj_usuario.Classe
    atrs_cria = {
      'usr': usr,
      'arq': arq,
      'titulo': titulo, 
      'data': data,
      'duracao': duracao, 
      'largura': largura,
      'altura': altura
    }
    vid = cria(atrs_cria)
    assert vid != None and type(vid) is obj_video.Classe
    id_vid = obj_video.obtem_identificador(vid)
    usr_conf = obj_video.obtem_usuario(vid)
    id_usr_conf = obj_usuario.obtem_identificador(usr_conf)
    assert usr_conf == usr;
    if verb: sys.stderr.write("  video %s de %s criado\n" % (id_vid, id_usr))
  return

def verifica_criacao(vid, id_vid, atrs):
  return obj_raiz.verifica_criacao(vid, obj_video.Classe, id_vid, atrs, None, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def liga_diagnosticos(val):
  global vid_debug
  vid_debug = val
  return

# FUNÇÕES INTERNAS

def valida_atributos(vid, atrs_mem):
  """Faz validações específicas nos atributos {atrs_mem}. Devolve uma lista
  de strings com descrições dos erros encontrados.

  Se {vid} é {None}, supõe que um novo objeto de sessão está sendo criado.
  Se {vid} não é {None}, supõe que {atrs} sao alterações a aplicar nessa
  sessão. """
  global cache, nome_tb, letra_tb, colunas
  erros = [].copy();
  # !!! Completar !!!
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
  global cache, nome_tb, letra_tb, colunas
  if vid_debug: mostra(0, "obj_video_IMP.def_obj_mem(" + str(obj) + ", " + id_vid + ", " + str(atrs_SQL) + ") ...")
  if obj == None:
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, db_tabelas.identificador_para_objeto)
    if vid_debug: mostra(2, "criando objeto, atrs_mem = " + str(atrs_mem))
    obj = obj_video.Classe(id_vid, atrs_mem)
  else:
    assert obj.id == id_vid
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, db_tabelas.identificador_para_objeto)
    if vid_debug: mostra(2, "modificando objeto, atrs_mem = " + str(atrs_mem))
    assert type(atrs_mem) is dict
    if len(atrs_mem) > len(obj.atrs):
      erro_prog("numero excessivo de atributos a alterar")
    for chave, val in atrs_mem.items():
      if not chave in obj.atrs:
        erro_prog("chave '" + chave + "' inválida")
      val_velho = obj.atrs[chave]
      if not type(val_velho) is type(val):
        erro_prog("tipo do campo '" + chave + "' incorreto")
      if chave == 'usr' and val != val_velho:
        erro_prog("campo '" + chave + "' não pode ser alterado")
      obj.atrs[chave] = val
  if vid_debug: mostra(2, "obj = " + str(obj))
  return obj
