# Implementação do módulo {db_base_sql}.

import sqlite3, sys

from util_erros import erro_prog, mostra

# VARIÁVEIS GLOBAIS DO MÓDULO

db_conexao = None 
  # O objeto retornado por {sqlite3.connect(...)}.  
  # Os métodos deste objeto permitem acessar a base no disco."""
  
db_debug = False
  # Quando {True}, mostra comandos SQL e resultados em {stderr}.

# IMPLEMENTAÇÔES

def conecta(dir, uid, senha):
  # Ignora {uid} e {senha} por enquanto.
  global db_conexao
  mostra(4,"db_base_sql_IMP.conecta: conectando com a base")
  if db_conexao != None: 
    mostra(6,"db_base_sql_IMP.conecta: !! Já conectada")
    return None
  try:
    db_conexao = sqlite3.connect(dir + "/MC857.sqlite3")
    if db_debug: mostra(6,"db_base_sql_IMP.conecta: base {sqlite3}, versao = " + sqlite3.version)
    return None
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.conecta: !! erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_CREATE_TABLE(nome_tb, descr_cols):
  global db_conexao
  try:
    cursor = db_conexao.cursor()
    cmd = "CREATE TABLE IF NOT EXISTS " + nome_tb + "( " + descr_cols + " )"
    if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_CREATE_TABLE: cmd = \"" + str(cmd) + "\"")
    cursor.execute(cmd)
    return None
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_CREATE_TABLE: !! erro = \"" + str(msg) + "\"")
    return msg

def num_entradas(nome_tb, nome_indice):
  global db_conexao
  try:
    cursor = db_conexao.cursor()
    cmd = 'SELECT max(' + nome_indice + ') FROM ' + nome_tb
    if db_debug: mostra(4,"db_base_sql_IMP.num_entradas: cmd = \"" + str(cmd) + "\"")
    cursor.execute(cmd)
    max_ind = cursor.fetchone()[0]
    if db_debug: mostra(6,"max_ind = " + str(max_ind))
    if max_ind == None:
      max_ind = 0
    return max_ind
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.num_entradas: !! erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_INSERT(nome_tb, atrs):
  global db_conexao
  chaves = ""
  valores = ""
  for ch in atrs.keys():
    val = codifica_valor(atrs[ch]);
    # Acrescenta a chave {ch} à lista de nomes de colunas:
    if chaves != "": chaves = chaves + ","
    chaves = chaves + ch
    # Acrescent o valor {val} à lista de valores de colunas:
    if valores != "": valores = valores + ","
    valores = valores + val
  cmd = "INSERT INTO " + nome_tb + " ( " + chaves + " ) VALUES (" + valores + ")"
  if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_INSERT: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = db_conexao.cursor()
    cursor.execute(cmd)
    db_conexao.commit()
    ind = cursor.lastrowid
    if db_debug: mostra(6,"lastrowid = " + str(ind))
    return ind
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_INSERT: !! erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_UPDATE(nome_tb, cond, atrs):
  global db_conexao
  pares = ""
  for ch in atrs.keys():
    val = codifica_valor(atrs[ch]);
    # Acrescenta "{ch} = {val}" à lista de alterações de colunas:
    if pares != "": pares = pares + ","
    pares = pares + ch + " = " + val
  cmd = "UPDATE " + nome_tb + " SET " + pares + " WHERE " + cond
  if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_UPDATE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = db_conexao.cursor()
    cursor.execute(cmd)
    db_conexao.commit()
    return None
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_UPDATE: !! erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_SELECT(nome_tb, cond, nomes_cols):
  global db_conexao
  cols = ""
  for cn in nomes_cols:
    # Acrescenta "{cn} à lista de nomes de colunas:
    if cols != "": cols = cols + ","
    cols = cols + cn

  cmd = "SELECT " + cols + " FROM " + nome_tb + " WHERE " + cond
  if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_SELECT: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = db_conexao.cursor()
    iterador = cursor.execute(cmd)
    res = cursor.fetchall() # Converte o iterador em lista.
    cursor.close()
    if db_debug: mostra(6,"db_base_sql_IMP.executa_comando_SELECT: len(res) = " + str(len(res)))
    return res
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_SELECT: !! erro = \"" + str(msg) + "\"")
    mostra(4,"  cmd = \"" + str(cmd) + "\"")
    return msg

def executa_comando_DELETE(nome_tb, cond):
  global db_conexao
  cmd = "DELETE FROM " + nome_tb + " WHERE " + cond
  if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_DELETE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = db_conexao.cursor()
    cursor.execute(cmd)
    db_conexao.commit()
    cursor.close()
    return None
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_DELETE: !! erro = \"" + str(msg) + "\"")
    return msg

def executa_comando_DROP_TABLE(nome_tb):
  global db_conexao
  cmd = "DROP TABLE IF EXISTS " + nome_tb
  if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_DROP_TABLE: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = db_conexao.cursor()
    cursor.execute(cmd)
    db_conexao.commit()
    cursor.close()
    return None
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_DROP_TABLE: !! erro = \"" + str(msg) + "\"")
    return msg
    
def executa_comando_TABLE_EXISTS(nome_tb):
  global db_conexao
  # Cozinhada obtida da internet:
  cmd_core = f"SELECT name FROM sqlite_schema WHERE type='table' AND name='{nome_tb}'"
  cmd = f"SELECT EXISTS ({cmd_core})"
  if db_debug: mostra(4,"db_base_sql_IMP.executa_comando_TABLE_EXISTS: cmd = \"" + str(cmd) + "\"")
  try:
    cursor = db_conexao.cursor()
    cursor.execute(cmd)
    res = cursor.fetchall() # Converte o iterador em lista.
    cursor.close()
    res_num = res
    while type(res_num) is list or type(res_num) is tuple:
      res_num = res_num[0]
    if type(res_num) is int and res_num >= 0 and res_num <= 1:
      # Convert to boolean
      return res_num == 1
    else:
      msg = f"resultado {str(res)} de tipo inválido"
      mostra(4,"db_base_sql_IMP.executa_comando_TABLE_EXISTS: !! erro = \"" + str(msg) + "\"")    
      return msg
  except sqlite3.Error as msg:
    mostra(4,"db_base_sql_IMP.executa_comando_TABLE_EXISTS: !! erro = \"" + str(msg) + "\"")
    return msg

def codifica_valor(val):
  global db_conexao
  if val == None:
    return "NULL"
  elif type (val) is int:
    return str(val)
  elif type(val) is str:
    # !!! Precisa proteger caracteres especiais em {val}, como [']. !!!
    return "'" + val + "'"
  elif type(val) is float:
    return ("%.2f" % val)
  elif type(val) is bool:
    if val:
      return "1"
    else:
      return "0"
  else:
    erro_prog("valor " + str(val) + " tipo = " + str(type(val)) + " invalido")
    return None

def liga_diagnosticos(val):
  global db_debug
  db_debug = val
  return
