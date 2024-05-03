# Implementação do módulo {objeto} e da classe {obj_raiz.Classe}.

import obj_raiz

import db_obj_tabela
import db_conversao_sql

import util_identificador
import util_testes
import util_valida_campo
from util_erros import erro_prog, aviso_prog, mostra

import sys

# VARIÁVEIS GLOBAIS DO MÓDULO
  
orz_debug = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

class Classe_IMP:

  def __init__(self, id, atrs):
    self.id = id
    self.atrs = atrs.copy()

# Implementação das funções:

def cria(atrs_mem, tabela, def_obj_mem):
  global orz_debug
  if orz_debug: mostra(0,"obj_raiz_IMP.cria(" + str(atrs_mem) + ") ...")
  assert tabela != None and tabela.colunas != None, "{tabela} é {None} -- módulo não inicializado?"

  # Converte atibutos para formato SQL.
  atrs_SQL = db_conversao_sql.dict_mem_para_dict_SQL(atrs_mem, tabela.colunas, False)
  # Insere na base de dados e obtém o índice na mesma:
  obj = db_obj_tabela.acrescenta_objeto(tabela, def_obj_mem, atrs_SQL)
  return obj

def muda_atributos(obj, mods_mem, tabela, def_obj_mem):
  assert tabela != None and tabela.colunas != None, "{tabela} é {None} -- módulo não inicializado?"
  
  # Converte valores de formato memória para formato SQL.
  mods_SQL = db_conversao_sql.dict_mem_para_dict_SQL(mods_mem, tabela.colunas, True)
  res = db_obj_tabela.atualiza_objeto(tabela, def_obj_mem, obj.id, mods_SQL)
  assert res == obj
  return

def obtem_identificador(obj):
  assert obj != None
  return obj.id

def obtem_atributos(obj):
  return obj.atrs.copy()

def obtem_atributo(obj, chave):
  return obj.atrs[chave]

def obtem_objeto(id_obj, tabela, def_obj_mem):
  assert tabela != None and tabela.colunas != None, "{tabela} é {None} -- módulo não inicializado?"
  if id_obj == None:
    obj = None
  else:
    obj = db_obj_tabela.obtem_objeto(tabela, def_obj_mem, id_obj)
  return obj

def busca_por_campo(chave, val, unico, tabela):
  assert tabela != None and tabela.colunas != None, "{tabela} é {None} -- módulo não inicializado?"
  lista_ids = db_obj_tabela.busca_por_campo(tabela, chave, val, None)
  if unico:
    return util_testes.unico_elemento(lista_ids)
  else:
    return lista_ids
    
def busca_por_campos(args, unico, tabela):
  assert tabela != None and tabela.colunas != None, "{tabela} é {None} -- módulo não inicializado?"
  res = db_obj_tabela.busca_por_campos(tabela, args, None)
  if res == None: res = [].copy() # Just in case.
  if type(res) is list or type(res) is tuple:
    return res
  elif type(res) is str:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    erro_prog("busca na tabela devolveu resultado inválido, res = \"" + str(res) + "\"")

def ultimo_identificador(tabela):
  assert tabela != None and tabela.colunas != None, "{tabela} é {None} -- módulo não inicializado?"
  num_ents = db_obj_tabela.num_entradas(tabela)
  id_ult = util_identificador.de_indice(tabela.letra, num_ents)
  return id_ult

# FUNÇÕES PARA DEPURAÇÃO

def liga_diagnosticos(val):
  global orz_debug
  orz_debug = val
  return

def verifica_criacao(obj, tipo, id_obj, atrs, ignore, tabela, def_obj_mem): 
  if orz_debug: sys.stderr.write("  > {obj_raiz.obtem_verifica_criacao()}:\n")

  ok = True # Este teste deu OK?
  if obj == None:
    if orz_debug: sys.stderr.write("    > obj == None\n")
    pass
  elif not type(obj) is tipo:
    aviso_prog("tipo do objeto " + str(type(obj)) + " inválido", True)
    ok = False
  else:
    if orz_debug: sys.stderr.write("    > testando {obj_raiz.obtem_identificador()}:\n")
    id_obj_cmp = obtem_identificador(obj)
    if id_obj_cmp != id_obj:
      aviso_prog("retornou " + str(id_obj_cmp) + ", deveria ter retornado " + str(id_obj), True)
      ok = False

    if orz_debug: sys.stderr.write("    > testando {obj_raiz.obtem_atributos()}:\n")
    atrs_cmp = obtem_atributos(obj)
    atrs_esp = atrs.copy()
    
    # Remove atributos que podem diferir:
    if ignore != None:
      for chave in ignore:
        if chave in atrs_cmp: del atrs_cmp[chave]
        if chave in atrs_esp: del atrs_esp[chave]
      
    for chave in atrs_esp.keys():
      assert chave in atrs_cmp, f"chave {chave} falta nos atributos do objeto"
      if atrs_cmp[chave] != atrs_esp[chave]:
        aviso_prog("retornou " + str(atrs_cmp[chave]) + ", deveria ter retornado " + str(atrs_esp[chave]), True)
        ok = False
    
    if orz_debug: sys.stderr.write("  > testando {obj_raiz.obtem_objeto()}:\n")
    obj1 = obtem_objeto(id_obj, tabela, def_obj_mem)
    if obj1 != obj:
      aviso_prog("retornou " + str(obj1) + ", deveria ter retornado " + str(obj), True)
      ok = False

  return ok
