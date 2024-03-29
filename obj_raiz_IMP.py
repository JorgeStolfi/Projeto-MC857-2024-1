# Implementação do módulo {objeto} e da classe {Objeto}.

import obj_raiz

import db_tabela_generica
import db_conversao_sql

import util_identificador
import util_valida_campo; from util_valida_campo import ErroAtrib
from util_testes import erro_prog, aviso_prog, mostra

import sys

# VARIÁVEIS GLOBAIS DO MÓDULO
  
orz_debug = False
  # Quando {True}, mostra comandos e resultados em {stderr}.

class Classe_IMP:

  def __init__(self, id, atrs):
    self.id = id
    self.atrs = atrs.copy()

# Implementação das funções:

def cria(atrs_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  global orz_debug
  if orz_debug: mostra(0,"obj_raiz_IMP.cria(" + str(atrs_mem) + ") ...")

  # Converte atibutos para formato SQL.
  atrs_SQL = db_conversao_sql.dict_mem_para_dict_SQL(atrs_mem, colunas, False)
  # Insere na base de dados e obtém o índice na mesma:
  obj = db_tabela_generica.acrescenta(nome_tb, cache, letra_tb, colunas, def_obj_mem, atrs_SQL)
  return obj

def muda_atributos(obj, mods_mem, cache, nome_tb, letra_tb, colunas, def_obj_mem):

  # Converte valores de formato memória para formato SQL.
  mods_SQL = db_conversao_sql.dict_mem_para_dict_SQL(mods_mem, colunas, True)
  res = db_tabela_generica.atualiza(nome_tb, cache, letra_tb, colunas, def_obj_mem, obj.id, mods_SQL)
  assert res == obj
  return

def obtem_identificador(obj):
  assert obj != None
  return obj.id

def obtem_atributos(obj):
  return obj.atrs.copy()

def obtem_atributo(obj, chave):
  return obj.atrs[chave]

def busca_por_identificador(id_obj, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  if id_obj == None:
    obj = None
  else:
    obj = db_tabela_generica.busca_por_identificador(nome_tb, cache, letra_tb, colunas, def_obj_mem, id_obj)
  return obj

def busca_por_campo(chave, val, unico, cache, nome_tb, letra_tb, colunas):
  lista_ids = db_tabela_generica.busca_por_campo(nome_tb, letra_tb, colunas, chave, val, None)
  if unico:
    return util_identificador.unico_elemento(lista_ids)
  else:
    return lista_ids
    
def busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas):
  res = db_tabela_generica.busca_por_campos(nome_tb, letra_tb, colunas, args, None)
  if res == None: res = [].copy() # Just in case.
  if type(res) is list or type(res) is tuple:
    return res
  elif type(res) is str:
    erro_prog("busca na tabela falhou, res = " + res)
  else:
    erro_prog("busca na tabela devolveu resultado inválido, res = \"" + str(res) + "\"")

# FUNÇÕES PARA DEPURAÇÃO

def liga_diagnosticos(val):
  global orz_debug
  orz_debug = val
  return

def verifica_criacao(obj, tipo, id_obj, atrs, ignore, cache, nome_tb, letra_tb, colunas, def_obj_mem): 
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
      
    if atrs_cmp != atrs_esp:
      aviso_prog("retornou " + str(atrs_cmp) + ", deveria ter retornado " + str(atrs_esp), True)
      ok = False
    
    if orz_debug: sys.stderr.write("  > testando {obj_raiz.busca_por_identificador()}:\n")
    obj1 = busca_por_identificador(id_obj, cache, nome_tb, letra_tb, colunas, def_obj_mem)
    if obj1 != obj:
      aviso_prog("retornou " + str(obj1) + ", deveria ter retornado " + str(obj), True)
      ok = False

  return ok
