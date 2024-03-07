#! /usr/bin/python3

#Testes do módulo {db_tabela_generica}
import db_tabela_generica
import db_base_sql
from util_testes import erro_prog, mostra

# Para diagnóstico:
import sys

def mostra_obj(rotulo, obj, id, atrs):
  """Imprime usuário {obj} e compara seus atributos com {id,atrs}."""
  sys.stderr.write(rotulo + " = \n")
  if obj == None:
    sys.stderr.write("  None\n")
  elif type(obj) is str:
    sys.stderr.write("  " + obj + "\n")
    assert False
  elif type(obj) is ObjBobo:
    sys.stderr.write("  id = " + str(obj.id) + "\n")
    sys.stderr.write("  atrs = " + str(obj.atrs) + "\n")
    if atrs != None:
      id_confere = (obj.id == id)
      atrs_conferem = (obj.atrs == atrs)
      sys.stderr.write("  CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")
  else:
    erro_prog("resultado "  + str(obj) + " não é objeto do tipo correto")

def verifica_resultado(rotulo, res_cmp, res_esp):
  """Verifica se o resultado {res_cmp} de uma chamada é o resultado esperado {res_esp}."""
  sys.stderr.write(rotulo + ": ")
  sys.stderr.write("tipo resultado = \"" + str(type(res_cmp)) + "\"")
  assert type(res_cmp) is list or type(res_cmp) is tuple
  if res_cmp != res_esp:
    erro_prog("resultado = \"" + str(res_cmp) + "\" não é o esperado = \"" + str(res_esp) + "\"")
  else:
    sys.stderr.write(" CONFERE\n")

# ----------------------------------------------------------------------

sys.stderr.write("Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

class ObjBobo:
  # Classe para teste.  Por enquanto, os campos do objeto
  # são no formato SQL mesmo ({int}, {float}, e {str}) , para
  # não precisar de conversão.
  
  id = None
  atrs = None
  
  def __init__(self, id, atrs):
    self.id = id
    self.atrs = atrs.copy()
    

def def_obj(obj, id, atrs_SQL):
  """Cria ou altera o obejto da classe {ObjBobo}."""
  if obj == None:
    sys.stderr.write("  criando ObjBobo, id =" + id + ", atrs_SQL = " + str(atrs_SQL) + ")\n")
    obj = ObjBobo(id, atrs_SQL)
  else:
    mods_SQL = atrs_SQL
    sys.stderr.write("  alterando ObjBobo, obj = " + str(obj) + " mods_SQL = " + str(mods_SQL) + "\n")
    assert obj.id == id
    assert len(mods_SQL) <= len(obj.atrs)
    for k, v in mods_SQL.items():
      assert k in obj.atrs
      obj.atrs[k] = v
  return obj
    
cols = (
  ('nome',   type("foo"), 'TEXT',     3,   60),
  ('email',  type("foo"), 'TEXT',     6,   60),
  ('CPF',    type("foo"), 'TEXT',    14,   14),
  ('pernas', type(10),    'INTEGER',  2, 1000)
)

nome_tb = "objs"
let = "X"
cache = {}.copy()

sys.stderr.write("testando {db_tabela_generica.cria_tabela}:\n")
res = db_tabela_generica.cria_tabela(nome_tb, cols)
sys.stderr.write("Resultado = " + str(res) + "\n")
 
sys.stderr.write("testando {db_tabela_generica.limpa_tabela}:\n")
res = db_tabela_generica.limpa_tabela(nome_tb, cols)
sys.stderr.write("Resultado = " + str(res) + "\n")

# ----------------------------------------------------------------------
sys.stderr.write("testando {db_tabela_generica.acrescenta}:\n")
nome1 = "José Primeiro"
email1 = "primeiro@ic.unicamp.br"
CPF1 = "123.456.789-00" 
atrs1 = {
  "nome": nome1, 
  "email": email1, 
  "CPF": CPF1, 
  "pernas": 4
}
id1 = "X-00000001"
obj1 = db_tabela_generica.acrescenta(nome_tb, cache, let, cols, def_obj, atrs1)
mostra_obj("obj1", obj1, id1, atrs1)

nome2 = "João Segundo"
email2 = "segundo@ic.unicamp.br"
CPF2 = "987.654.321-99"
atrs2 = {
  "nome": nome2, 
  "email": email2, 
  "CPF": CPF2, 
  "pernas": 2
}
id2 = "X-00000002"
obj2 = db_tabela_generica.acrescenta(nome_tb, cache, let, cols, def_obj, atrs2)
mostra_obj("obj2", obj2, id2, atrs2)

nome3 = "Juca Terceiro"
email3 = "terceiro@ic.unicamp.br"
CPF3 = "333.333.333-33"
atrs3 = {
  "nome": nome3, 
  "email": email3, 
  "CPF": CPF3, 
  "pernas": 2
}
id3 = "X-00000003"
obj3 = db_tabela_generica.acrescenta(nome_tb, cache, let, cols, def_obj, atrs3)
mostra_obj("obj3", obj3, id3, atrs3)

# ----------------------------------------------------------------------
sys.stderr.write("testando {db_tabela_generica.busca_por_identificador}:\n")

obj1_a = db_tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, def_obj, id1)
mostra_obj("obj1_a", obj1_a, id1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("testando {db_tabela_generica.busca_por_campo}:\n")

em_a = email2
res = db_tabela_generica.busca_por_campo(nome_tb, let, cols, 'email', em_a, None) 
verifica_resultado("email" + em_a, res, [id2,])

CPF_b = CPF1
res = db_tabela_generica.busca_por_campo(nome_tb, let, cols, 'CPF', CPF_b, None)
verifica_resultado("CPF" + CPF_b, res, [id1,])

pernas_c = 2
res = db_tabela_generica.busca_por_campo(nome_tb, let, cols, 'pernas', 2, ('nome', 'CPF'))
verifica_resultado("pernas" + str(pernas_c), res, [(nome2, CPF2), (nome3, CPF3)])

# ----------------------------------------------------------------------
sys.stderr.write("testando {db_tabela_generica.atualiza}:\n")

alts1 = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
db_tabela_generica.atualiza(nome_tb, cache, let, cols, def_obj, id1, alts1)
obj1_c = db_tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, def_obj, id1)
for k, v in alts1.items():
  atrs1[k] = v
mostra_obj("obj1_c", obj1_c, id1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("destruindo a tabela com {db_base_sql.executa_comando_DROP_TABLE}:\n")
res = db_base_sql.executa_comando_DROP_TABLE(nome_tb)
sys.stderr.write("Resultado = " + str(res) + "\n")
