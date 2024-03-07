# Implementação do módulo {db_conversao_sql}

# CONVERSÃO DE VALORES MEMÓRIA <--> SQL

import db_conversao_sql
import obj_raiz
from util_testes import erro_prog, mostra

import sys

def valor_mem_para_valor_SQL(nome, val_mem, tipo_mem, tipo_SQL, nulo_ok):
  if val_mem == None:
    if nulo_ok: 
      return None
    else:
      erro_prog("atributo '" + nome + "' não pode ser {None}") 
  if type(val_mem) != tipo_mem:
    erro_prog("atributo " + str(val_mem) + " com tipo incorreto") 
  elif type(val_mem) is str:
    assert tipo_SQL == 'TEXT'
    val_SQL = val_mem
  elif type(val_mem) is int:
    assert tipo_SQL == 'INTEGER'
    val_SQL = val_mem
  elif type(val_mem) is float:
    assert tipo_SQL == 'FLOAT'
    val_SQL = val_mem
  elif type(val_mem) is bool:
    assert tipo_SQL == 'INTEGER'
    val_SQL = (1 if val_mem else 0)
  elif type(val_mem) is list or type(val_mem) is tuple or type(val_mem) is dict:
    erro_prog("valor " + str(val_mem) + " não pode ser convertido")
  else:
    # Supõe que é objeto.  Obtem o id:
    if tipo_SQL != 'TEXT':
      erro_prog("tipo SQL do atributo '" + nome + "' deveria ser 'TEXT' mas é '" + tipo_SQL + "'") 
    val_SQL = obj_raiz.obtem_identificador(val_mem)
  return val_SQL

def valor_SQL_para_valor_mem(nome, val_SQL, tipo_SQL, tipo_mem, nulo_ok, id_para_objeto):
  if val_SQL == None:
    if nulo_ok:
      return None
    else:
      erro_prog("atributo '" + nome + "' não pode ser {None}") 
  if tipo_mem is list or tipo_mem is tuple or tipo_mem is dict:
    erro_prog("valor " + str(val_SQL) + " não pode ser convertido para tipo " + str(tipo_mem))
  if tipo_SQL == 'TEXT':
    if issubclass(tipo_mem, obj_raiz.Classe):
      val_mem = id_para_objeto(val_SQL)
    else:
      assert type(val_SQL) is str
      val_mem = val_SQL
  elif tipo_SQL == 'FLOAT':
    assert type(val_SQL) is float
    val_mem = val_SQL
  elif tipo_SQL == 'INTEGER':
    assert type(val_SQL) is int
    # Tipo na memória pode ser {int}, {bool}, ou objeto
    if tipo_mem is int:
      val_mem = val_SQL
    elif tipo_mem is bool:
      if val_SQL < 0 or val_SQL > 1:
        erro_prog("valor booleano '" + nome + "' = " + str(val_SQL) + " inválido")
      val_mem = (val_SQL == 1)
    else:
      erro_prog("tipo_SQL INTEGER nao pode ser convertido para " + str(tipo_mem) + "")
  else:
    erro_prog("tipo SQL '" + str(tipo_SQL) + "' inválido")
  assert type(val_mem) is tipo_mem
  return val_mem

# CONVERSÃO DE DICIONÁRIOS MEMÓRIA <--> SQL

def dict_mem_para_dict_SQL(dic_mem, cols, falta_ok):
  if len(dic_mem) > len(cols):
    erro_prog("numero excessivo de atributos em " + str(dic_mem))
  dic_SQL = {}.copy()
  for chave, tipo_mem, tipo_SQL, nulo_ok in cols:
    if chave in dic_mem:
      val_mem = dic_mem[chave]
      if val_mem != None and not type(val_mem) is tipo_mem:
        erro_prog("valor " + str(val_mem) + " deveria ter tipo " + str(tipo_mem))
      val_SQL = valor_mem_para_valor_SQL(chave, val_mem, tipo_mem, tipo_SQL, nulo_ok)
      dic_SQL[chave] = val_SQL
    elif not falta_ok:
      erro_prog("atributo '" + chave + "' faltando")

  if len(dic_mem) > len(dic_SQL):
    erro_prog("atributos espúrios em " + str(dic_mem))
  return dic_SQL

def dict_SQL_para_dict_mem(dic_SQL, cols, falta_ok, id_para_objeto):
  if len(dic_SQL) > len(cols):
    erro_prog("numero excessivo de atributos em " + str(dic_SQL))
  dic_mem = {}.copy()
  for chave, tipo_mem, tipo_SQL, nulo_ok in cols:
    if chave in dic_SQL: 
      val_SQL = dic_SQL[chave]
      val_mem = valor_SQL_para_valor_mem(chave, val_SQL, tipo_SQL, tipo_mem, nulo_ok, id_para_objeto)
      dic_mem[chave] = val_mem
    elif not falta_ok:
      erro_prog("atributo '" + chave + "' faltando")
  if len(dic_SQL) > len(dic_mem):
    erro_prog("atributos espúrios em " + str(dic_SQL))
  return dic_mem

