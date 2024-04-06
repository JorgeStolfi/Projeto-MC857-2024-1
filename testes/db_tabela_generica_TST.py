#! /usr/bin/python3

#Testes do módulo {db_tabela_generica}
import db_tabela_generica
import db_base_sql
from util_testes import erro_prog, mostra

# Para diagnóstico:
import sys

def mostra_bob(rotulo, bob, id_bob, atrs):
  """Imprime {ObjBobo} {bob} e compara seus atributos com {id_bob,atrs}."""
  if bob == None:
    sys.stderr.write("    bob = None\n")
  elif type(bob) is str:
    sys.stderr.write(f"    bob = {bob}\n")
    assert False
  elif type(bob) is ObjBobo:
    sys.stderr.write(f"   bob id = {bob.id} atrs = {str(bob.atrs)}\n")
    if atrs != None:
      id_confere = (bob.id == id_bob)
      atrs_conferem = (bob.atrs == atrs)
      sys.stderr.write("    CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")
  else:
    erro_prog("resultado "  + str(bob) + " não é objeto do tipo correto")

def verifica_resultado(rotulo, res_cmp, res_esp):
  """Verifica se o resultado {res_cmp} de uma chamada é o resultado esperado {res_esp}."""
  sys.stderr.write("    tipo resultado = \"" + str(type(res_cmp)) + "\"")
  assert type(res_cmp) is list or type(res_cmp) is tuple
  if res_cmp != res_esp:
    erro_prog("    resultado = \"" + str(res_cmp) + "\" não é o esperado = \"" + str(res_esp) + "\"")
  else:
    sys.stderr.write("    CONFERE\n")

# ----------------------------------------------------------------------

sys.stderr.write("  Conectando com base de dados...\n")
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
    

def def_bob(bob, id_bob, atrs_SQL):
  """Cria ou altera o obejto da classe {ObjBobo}."""
  if bob == None:
    sys.stderr.write("  > criando ObjBobo, id =" + id_bob + ", atrs_SQL = " + str(atrs_SQL) + ")\n")
    bob = ObjBobo(id_bob, atrs_SQL)
  else:
    mods_SQL = atrs_SQL
    sys.stderr.write("  > alterando ObjBobo, bob = " + str(bob) + " mods_SQL = " + str(mods_SQL) + "\n")
    assert bob.id == id_bob
    assert len(mods_SQL) <= len(bob.atrs)
    for k, v in mods_SQL.items():
      assert k in bob.atrs
      bob.atrs[k] = v
  return bob
    
cols = (
  ('nome',   type("foo"), 'TEXT',     3,   60),
  ('email',  type("foo"), 'TEXT',     6,   60),
  ('CPF',    type("foo"), 'TEXT',    14,   14),
  ('pernas', type(10),    'INTEGER',  2, 1000)
)

# numero de elementos que foram inseridos na tabela para o teste
num_elementos = 0
nome_tb = "bobs"
let = "X"
cache = {}.copy()

sys.stderr.write("  testando {db_tabela_generica.cria_tabela}:\n")
res = db_tabela_generica.cria_tabela(nome_tb, cols)
sys.stderr.write("    resultado = " + str(res) + "\n")
 
sys.stderr.write("  testando {db_tabela_generica.limpa_tabela}:\n")
res = db_tabela_generica.limpa_tabela(nome_tb, cols)
sys.stderr.write("    resultado = " + str(res) + "\n")

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_tabela_generica.acrescenta}:\n")
nome1 = "José Primeiro"
email1 = "primeiro@ic.unicamp.br"
CPF1 = "123.456.789-00" 
atrs1 = {
  "nome": nome1, 
  "email": email1, 
  "CPF": CPF1, 
  "pernas": 4
}
id_bob1 = "X-00000001"
bob1 = db_tabela_generica.acrescenta(nome_tb, cache, let, cols, def_bob, atrs1)
num_elementos +=1
mostra_bob("bob1", bob1, id_bob1, atrs1)

nome2 = "João Segundo"
email2 = "segundo@ic.unicamp.br"
CPF2 = "987.654.321-99"
atrs2 = {
  "nome": nome2, 
  "email": email2, 
  "CPF": CPF2, 
  "pernas": 2
}
id_bob2 = "X-00000002"
bob2 = db_tabela_generica.acrescenta(nome_tb, cache, let, cols, def_bob, atrs2)
num_elementos +=1
mostra_bob("bob2", bob2, id_bob2, atrs2)

nome3 = "Juca Terceiro"
email3 = "terceiro@ic.unicamp.br"
CPF3 = "333.333.333-33"
atrs3 = {
  "nome": nome3, 
  "email": email3, 
  "CPF": CPF3, 
  "pernas": 2
}
id_bob3 = "X-00000003"
bob3 = db_tabela_generica.acrescenta(nome_tb, cache, let, cols, def_bob, atrs3)
num_elementos +=1
mostra_bob("bob3", bob3, id_bob3, atrs3)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_tabela_generica.busca_por_identificador}:\n")

bob1_a = db_tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, def_bob, id_bob1)
mostra_bob("bob1_a", bob1_a, id_bob1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_tabela_generica.busca_por_campo}:\n")

em_a = email2
res = db_tabela_generica.busca_por_campo(nome_tb, let, cols, 'email', em_a, None) 
verifica_resultado("email" + em_a, res, [id_bob2,])

CPF_b = CPF1
res = db_tabela_generica.busca_por_campo(nome_tb, let, cols, 'CPF', CPF_b, None)
verifica_resultado("CPF" + CPF_b, res, [id_bob1,])

pernas_c = 2
res = db_tabela_generica.busca_por_campo(nome_tb, let, cols, 'pernas', 2, ('nome', 'CPF'))
verifica_resultado("pernas" + str(pernas_c), res, [(nome2, CPF2), (nome3, CPF3)])

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_tabela_generica.atualiza}:\n")

alts1 = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
db_tabela_generica.atualiza(nome_tb, cache, let, cols, def_bob, id_bob1, alts1)
bob1_c = db_tabela_generica.busca_por_identificador(nome_tb, cache, let, cols, def_bob, id_bob1)
for k, v in alts1.items():
  atrs1[k] = v
mostra_bob("bob1_c", bob1_c, id_bob1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_tabela_generica.num_entradas}:\n")
res = db_tabela_generica.num_entradas(nome_tb)
sys.stderr.write("   numero de entradas = \"" + str(res) + "\"\n")
# verifica o tipo
assert type(res) == int
# verifica o valor
assert res == num_elementos

# ----------------------------------------------------------------------
sys.stderr.write("  destruindo a tabela com {db_base_sql.executa_comando_DROP_TABLE}:\n")
res = db_base_sql.executa_comando_DROP_TABLE(nome_tb)
sys.stderr.write("    resultado = " + str(res) + "\n")

sys.stderr.write("Testes terminados normalmente.\n")
