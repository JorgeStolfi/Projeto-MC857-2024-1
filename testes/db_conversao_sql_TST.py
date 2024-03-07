#! /usr/bin/python3

#Testes do módulo {db_conversao_sql}
import db_base_sql
import obj_usuario
import obj_sessao
import db_tabelas
import db_conversao_sql
from util_testes import erro_prog, aviso_prog, mostra

# Para diagnóstico:
import sys

# ----------------------------------------------------------------------
sys.stderr.write("Conectando com base de dados...\n")
db_base_sql.conecta("DB", None, None)

db_tabelas.inicializa_todas(True)
db_tabelas.cria_todos_os_testes(True)

usr1_id = "U-00000001"
usr1 = obj_usuario.busca_por_identificador(usr1_id)  

usr2_id = "U-00000002"
usr2 = obj_usuario.busca_por_identificador(usr2_id)  

ses1_id = "S-00000001"
ses1 = obj_sessao.busca_por_identificador(ses1_id)  

ok_global = True # Vira {False} se um teste falha.

# ----------------------------------------------------------------------
# TESTES DE CONVERSÃO DE VALORES

def verifica_valor(rotulo, val_mem, tipo_mem, val_SQL, tipo_SQL, nulo_ok):
  """Testa {valor_mem_para_valor_SQL} e {valor_SQL_para_valor_mem}."""
  global ok_global
  ok = True # Estado deste teste.
  
  # Mostra parâmetros:
  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write(rotulo + "\n")
  sys.stderr.write("  val_mem = " + str(val_mem) + " tipo_mem = " + str(tipo_mem) + "\n")
  sys.stderr.write("  val_SQL = " + str(val_SQL) + " tipo_SQL = " + str(tipo_SQL) + "\n")
   
  # Testa {valor_mem_para_valor_SQL}:
  val_SQL_cmp = db_conversao_sql.valor_mem_para_valor_SQL(rotulo, val_mem, tipo_mem, tipo_SQL, nulo_ok)
  if val_SQL_cmp != val_SQL:
    aviso_prog("{valor_mem_para_valor_SQL} valor SQL não bate = '" + str(val_SQL_cmp) + "'",True)
    ok = False

  # Testa {valor_SQL_para_valor_mem}:
  val_mem_cmp = \
    db_conversao_sql.valor_SQL_para_valor_mem(rotulo, val_SQL, tipo_SQL, tipo_mem, nulo_ok, db_tabelas.id_para_objeto)
  if val_mem_cmp != val_mem:
    aviso_prog("{valor_SQL_para_valor_mem} não bate = '" + str(val_mem_cmp) + "'",True)
    ok = False
      
  # Veredito do teste:
  if ok:
    sys.stderr.write("  verifica_valor: ok\n")
  ok_global = ok_global and ok
  sys.stderr.write("%s\n" % ("-" * 70))
  return

# Testes de valor único:

verifica_valor("inteiro",        418,       type(418),        418,  'INTEGER',   False )
verifica_valor("float",     418.4615,     type(418.1),   418.4615,  'FLOAT',     False )
verifica_valor("string",   "Qüêntão",     type("foo"),  "Qüêntão",  'TEXT',      False )
verifica_valor("booleano",      True,      type(True),          1,  'INTEGER',   False )
verifica_valor("usuario",       usr1,     type(usr1),     usr1_id,  'TEXT',      False )
verifica_valor("sessao",        ses1,     type(ses1),     ses1_id,  'TEXT',      False )
verifica_valor("nulo",          None,     type("foo"),       None,  'TEXT',      True  )

# ----------------------------------------------------------------------
# TESTES DE CONVRSÃO DE DICIONÁRIOS

# define uma tabela boba só para conversao:
colunas = (
  ('nome',    type("foo"), 'TEXT',    False ),
  ('email',   type("foo"), 'TEXT',    False ),
  ('CPF',     type("foo"), 'TEXT',    True  ),
  ('pernas',  type(10),    'INTEGER', False ),
  ('volume',  type(412.2), 'FLOAT',   False ),
  ('chato',   type(True),  'INTEGER', False ),
  ('bobagem', type(usr1),  'TEXT',    False )
)

def verifica_dict(rotulo, dic_mem, falta_ok, dic_SQL):
  """Testa {dict_mem_para_dict_SQL} e {dict_SQL_para_dict_mem}."""
  global ok_global
  ok = True # Estado deste teste.

  # Mostra parâmetros:
  sys.stderr.write("%s\n" % ("-" * 70))
  sys.stderr.write(rotulo + "\n")
  sys.stderr.write("  dic_mem =     '" + str(dic_mem) + "' falta_ok = " + str(falta_ok) + "\n")
  sys.stderr.write("  dic_SQL =     '" + str(dic_SQL) + "'\n")
  
  # Verifica conversão memória --> SQL:
  dic_SQL_cmp = db_conversao_sql.dict_mem_para_dict_SQL(dic_mem, colunas, falta_ok)
  sys.stderr.write("    dic_SQL_cmp = '" + str(dic_SQL_cmp) + "'\n")
  if dic_SQL_cmp != dic_SQL:
    aviso_prog("{dict_mem_para_dict_SQL} não bate",True)
    ok = False

  # Verifica conversão SQL --> memória:
  dic_mem_cmp = db_conversao_sql.dict_SQL_para_dict_mem(dic_SQL, colunas, falta_ok, db_tabelas.id_para_objeto)
  sys.stderr.write("    dic_mem_cmp = '" + str(dic_mem_cmp) + "'\n")
  for chave, tipo_mem, tipo_SQL, nulo_ok in colunas:
    if tipo_mem is list or tipo_mem is tuple or tipo_mem is dict:
      # Campo não deve estar em {dic_SQL} nem em {dic_mem_cmp}:
      if chave in dic_SQL: 
        aviso_prog("chave " + chave + " não deveria estar em {dic_SQL}",True)
        ok = False
      elif chave in dic_mem_cmp: 
        aviso_prog("chave " + chave + " não deveria estar em {dic_mem_cmp}",True)
        ok = False
    else:
      # Campo deve estar ou não estar em ambos:
      if (chave in dic_SQL) != (chave in dic_mem_cmp):
        aviso_prog("chave " + chave + " com presença incongruente",True)
        ok = False
      elif chave in dic_SQL:
        val_mem = dic_mem[chave]
        val_mem_cmp = dic_mem_cmp[chave]
        if val_mem_cmp != val_mem:
          aviso_prog("campo " + chave + " com valor incongruente",True)
          ok = False
  if len(dic_mem_cmp) != len(dic_SQL):
    aviso_prog("campos espúrios em {dic_mem_cmp",True)
    ok = False

  # Veredito do teste:
  if ok:
    sys.stderr.write("  verifica_dict: ok\n")
  ok_global = ok_global and ok
  sys.stderr.write("%s\n" % ("-" * 70))
  return

# ----------------------------------------------------------------------
# Testes de dicionário sem erro:

dic1_mem = { 
  'nome':   "José da Silva",
  'email':  "josi@gmail.com",
  'CPF':    None,
  'pernas':  2,
  'volume':  418.4634,
  'chato':   True,
  'bobagem': usr1
}
dic1_SQL = {
  'nome':   "José da Silva",
  'email':  "josi@gmail.com",
  'CPF':    None,
  'pernas':  2,
  'volume':  418.4634,
  'chato':   1,
  'bobagem': usr1_id
}

verifica_dict("dicionario {dic1}", dic1_mem, False, dic1_SQL)

dic2_mem = { 
  'nome':   "Juca",
  'email':  "josi@gmail.com",
  'pernas':  1001,
  'volume':  420.4634,
  'bobagem': usr2
}
dic2_SQL = {
  'nome':   "Juca",
  'email':  "josi@gmail.com",
  'pernas':  1001,
  'volume':  420.4634,
  'bobagem': usr2_id
}

verifica_dict("dicionario {dic2}, T", dic2_mem, True, dic2_SQL)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Teste terminou sem detectar erro\n")
else:
  erro_prog("- teste falhou")
