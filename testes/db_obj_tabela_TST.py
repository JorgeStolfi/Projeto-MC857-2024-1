#! /usr/bin/python3

import db_obj_tabela
import db_base_sql
from util_erros import erro_prog, mostra
import sys

ok_global = True

def mostra_bob(rot_teste, bob, id_bob, atrs):
  """Imprime o objeto {bob} de tipo {BoboClasse} e compara seus atributos com {id_bob,atrs}."""
  if bob == None:
    sys.stderr.write("    bob = None\n")
  elif type(bob) is str:
    sys.stderr.write(f"    bob = {bob}\n")
    assert False
  elif type(bob) is BoboClasse:
    sys.stderr.write(f"   bob id = {bob.id} atrs = {str(bob.atrs)}\n")
    if atrs != None:
      id_confere = (bob.id == id_bob)
      atrs_conferem = (bob.atrs == atrs)
      sys.stderr.write("    CONFERE: " + str(id_confere) + ", " + str(atrs_conferem) + "\n")
  else:
    aviso_prog("resultado "  + str(bob) + " não é objeto do tipo correto", True)

def verifica_resultado(rot_teste, res_cmp, res_esp):
  """Verifica se o resultado {res_cmp} de uma chamada é o resultado esperado {res_esp}."""
  global ok_global
  sys.stderr.write("    tipo resultado = \"" + str(type(res_cmp)) + "\"")
  if res_cmp != res_esp:
    erro_prog("    ERRO - resultado = \"" + str(res_cmp) + "\" não é o esperado = \"" + str(res_esp) + "\"")
    ok_global = FALSE
  else:
    sys.stderr.write("    CONFERE\n")

# ----------------------------------------------------------------------

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB", None, None)
assert res == None

# ----------------------------------------------------------------------

class BoboClasse:
  # Classe para teste.  Por enquanto, os campos do objeto
  # são no formato SQL mesmo ({int}, {float}, e {str}) , para
  # não precisar de conversão.
  
  id = None
  atrs = None
  
  def __init__(self, id, atrs):
    self.id = id
    self.atrs = atrs.copy()
    
# Colunas da tabela de objetos {BoboClasse}:

colunas_bob = (
  ('nome',   type("foo"), 'TEXT',     3,   60),
  ('email',  type("foo"), 'TEXT',     6,   60),
  ('CPF',    type("foo"), 'TEXT',    14,   14),
  ('pernas', type(10),    'INTEGER',  2, 1000)
)
nome_bob = "bobs"
letra_bob = "X"

def def_bob(bob, id_bob, atrs_SQL):
  """Cria ou altera o objeto da classe {BoboClasse}."""
  if bob == None:
    sys.stderr.write("  > criando BoboClasse, id =" + id_bob + ", atrs_SQL = " + str(atrs_SQL) + ")\n")
    bob = BoboClasse(id_bob, atrs_SQL)
  else:
    mods_SQL = atrs_SQL
    sys.stderr.write("  > alterando BoboClasse, bob = " + str(bob) + " mods_SQL = " + str(mods_SQL) + "\n")
    assert bob.id == id_bob
    assert len(mods_SQL) <= len(bob.atrs)
    for chave, val in mods_SQL.items():
      assert chave in bob.atrs
      bob.atrs[chave] = val
  return bob

# numero de elementos que foram inseridos na tabela para o teste

limpa = True # Testar com os dois casos, em rodadas diferentes.
num_elementos = 0 if limpa else 4

sys.stderr.write("  testando {db_obj_tabela.cria_tabela} limpa = {%s}:\n" % limpa)
tab_bob = db_obj_tabela.cria_tabela(nome_bob, letra_bob, BoboClasse, colunas_bob, limpa)
sys.stderr.write("    resultado = " + str(tab_bob) + "\n")

db_obj_tabela.muda_diagnosticos(tab_bob, True)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.acrescenta_objeto}:\n")

nome1 = "José Primeiro da Silva"
email1 = "primeiro@ic.unicamp.br"
CPF1 = "123.456.789-00" 
atrs1 = {
  "nome": nome1, 
  "email": email1, 
  "CPF": CPF1, 
  "pernas": 4
}
num_elementos +=1
ind_bob1 = num_elementos
id_bob1 = f"X-{ind_bob1:08d}"
bob1 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs1)
mostra_bob("bob1", bob1, id_bob1, atrs1)

nome2 = "João Segundo da Silva"
email2 = "segundo@ic.unicamp.br"
CPF2 = "987.654.321-99"
atrs2 = {
  "nome": nome2, 
  "email": email2, 
  "CPF": CPF2, 
  "pernas": 2
}
num_elementos +=1
ind_bob2 = num_elementos
id_bob2 = f"X-{ind_bob2:08d}"
bob2 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs2)
mostra_bob("bob2", bob2, id_bob2, atrs2)

nome3 = "Juca Terceiro de Souza"
email3 = "terceiro@ic.unicamp.br"
CPF3 = "333.333.333-33"
atrs3 = {
  "nome": nome3, 
  "email": email3, 
  "CPF": CPF3, 
  "pernas": 2
}
num_elementos +=1
ind_bob3 = num_elementos
id_bob3 = f"X-{ind_bob3:08d}"
bob3 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs3)
mostra_bob("bob3", bob3, id_bob3, atrs3)

nome4 = "Júlo Quarto de Souza"
email4 = "terceiro@ic.unicamp.br"
CPF4 = "333.333.333-33"
atrs4 = {
  "nome": nome4, 
  "email": email4, 
  "CPF": CPF4, 
  "pernas": 2
}
num_elementos +=1
ind_bob4 = num_elementos
id_bob4 = f"X-{ind_bob4:08d}"
bob4 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs4)
mostra_bob("bob4", bob4, id_bob4, atrs4)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.busca_por_identificador}:\n")

id_bob1_a = id_bob1
bob1_a = db_obj_tabela.busca_por_identificador(tab_bob, def_bob, id_bob1_a)
mostra_bob("bob1_a", bob1_a, id_bob1, atrs1)
assert type(bob1_a) is BoboClasse
verifica_resultado("BID_id" + id_bob1_a, bob1_a, bob1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.busca_por_indice}:\n")

ind_bob2_a = ind_bob2
bob2_a = db_obj_tabela.busca_por_indice(tab_bob, def_bob, ind_bob2_a)
mostra_bob("bob2_a", bob2_a, id_bob2, atrs2)
assert type(bob2_a) is BoboClasse
verifica_resultado("BIND_ind" + str(ind_bob2), bob2_a, bob2 )

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.busca_por_campo}:\n")

email_a = email2
res_a = db_obj_tabela.busca_por_campo(tab_bob, 'email', email_a, None) 
assert type(res_a) is list or type(res_a) is tuple
res_a = list(res_a)
verifica_resultado("BC_email" + email_a, res_a, [ id_bob2, ])

CPF_b = CPF1
res_b = db_obj_tabela.busca_por_campo(tab_bob, 'CPF', CPF_b, None)
assert type(res_b) is list or type(res_b) is tuple
res_b = list(res_b)
verifica_resultado("BC_CPF" + CPF_b, res_b, [ id_bob1, ])

pernas_c = 2
res_c = db_obj_tabela.busca_por_campos(tab_bob, { 'pernas': pernas_c }, [ 'nome', 'CPF' ])
assert type(res_c) is list or type(res_c) is tuple
res_c = list(res_c)
verifica_resultado("BCS_pernas" + str(pernas_c), res_c, [(nome2, CPF2), (nome3, CPF3), (nome4, CPF4), ])

nome_d = "Souza"
pernas_d = 2
res_d = db_obj_tabela.busca_por_semelhanca(tab_bob, { 'nome': nome_d, 'pernas': pernas_d }, None)
assert type(res_d) is list or type(res_d) is tuple
res_d = list(res_d)
verifica_resultado("BS_nome" + nome_d + "pernas" + str(pernas_d), res_d, [ id_bob3, id_bob4, ])

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.atualiza_objeto}:\n")

alts1 = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
db_obj_tabela.atualiza_objeto(tab_bob, def_bob, id_bob1, alts1)
bob1_c = db_obj_tabela.busca_por_identificador(tab_bob, def_bob, id_bob1)
for chave, val in alts1.items():
  atrs1[chave] = val
mostra_bob("bob1_c", bob1_c, id_bob1, atrs1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.num_entradas}:\n")
res = db_obj_tabela.num_entradas(tab_bob)
sys.stderr.write("   numero de entradas = \"" + str(res) + "\"\n")
# verifica o tipo
assert type(res) == int
# verifica o valor
assert res == num_elementos

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_erro("Alguns testes falharam", True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)

