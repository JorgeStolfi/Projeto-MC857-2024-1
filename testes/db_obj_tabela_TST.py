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
  sys.stderr.write("    tipo resultado = \"" + str(type(res_cmp)) + "\"\n")
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
  ('nome',   type("foo"), 'TEXT',     3,     60,   ),
  ('email',  type("foo"), 'TEXT',     6,     60,   ),
  ('carro',  type("foo"), 'TEXT',     6,     30,   ),
  ('pernas', type(10),    'INTEGER',  2,   1000,   ),
  ('peso',   type(10.0),  'NUMERIC',  2.0, 1000.0, ),
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

carro1 = "Fort T" 
carro2 = "Cyberbrick"

nome_bob1 = "José Primeiro da Silva"
email_bob1 = "primeiro@gmail.com"
atrs_bob1 = {
  "nome": nome_bob1, 
  "email": email_bob1, 
  "carro": carro1, 
  "pernas": 4
}
num_elementos +=1
ind_bob1 = num_elementos
id_bob1 = f"X-{ind_bob1:08d}"
bob1 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs_bob1)
mostra_bob("bob1", bob1, id_bob1, atrs_bob1)

nome_bob2 = "José Segundo da Silva"
email_bob2 = "segundo@ic.unicamp.br"
atrs_bob2 = {
  "nome": nome_bob2, 
  "email": email_bob2, 
  "carro": carro2, 
  "pernas": 2
}
num_elementos +=1
ind_bob2 = num_elementos
id_bob2 = f"X-{ind_bob2:08d}"
bob2 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs_bob2)
mostra_bob("bob2", bob2, id_bob2, atrs_bob2)

nome_bob3 = "José Terceiro de Souza Toledo"
email_bob3 = "terceiro@ic.unicamp.br"
atrs_bob3 = {
  "nome": nome_bob3, 
  "email": email_bob3, 
  "carro": carro2, 
  "pernas": 4
}
num_elementos +=1
ind_bob3 = num_elementos
id_bob3 = f"X-{ind_bob3:08d}"
bob3 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs_bob3)
mostra_bob("bob3", bob3, id_bob3, atrs_bob3)

nome_bob4 = "José Quarto de Souza"
email_bob4 = "quarto@ic.unicamp.br"
atrs_bob4 = {
  "nome": nome_bob4, 
  "email": email_bob4, 
  "carro": carro1, 
  "pernas": 2
}
num_elementos +=1
ind_bob4 = num_elementos
id_bob4 = f"X-{ind_bob4:08d}"
bob4 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs_bob4)
mostra_bob("bob4", bob4, id_bob4, atrs_bob4)

nome_bob5 = "Jonas José Quinto de Souza"
email_bob5 = "quinto@gmail.com"
atrs_bob5 = {
  "nome": nome_bob5, 
  "email": email_bob5, 
  "carro": carro1, 
  "pernas": 2
}
num_elementos +=1
ind_bob5 = num_elementos
id_bob5 = f"X-{ind_bob5:08d}"
bob5 = db_obj_tabela.acrescenta_objeto(tab_bob, def_bob, atrs_bob5)
mostra_bob("bob5", bob5, id_bob5, atrs_bob5)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.obtem_objeto}:\n")

id_bob1_a = id_bob1
bob1_a = db_obj_tabela.obtem_objeto(tab_bob, def_bob, id_bob1_a)
mostra_bob("bob1_a", bob1_a, id_bob1, atrs_bob1)
assert type(bob1_a) is BoboClasse
verifica_resultado("BID_id" + id_bob1_a, bob1_a, bob1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.busca_por_indice}:\n")

ind_bob2_a = ind_bob2
bob2_a = db_obj_tabela.busca_por_indice(tab_bob, def_bob, ind_bob2_a)
mostra_bob("bob2_a", bob2_a, id_bob2, atrs_bob2)
assert type(bob2_a) is BoboClasse
verifica_resultado("BIND_ind" + str(ind_bob2), bob2_a, bob2 )

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.busca_por_campo} e {db_obj_tabela.busca_por_campos}:\n")

email_a = email_bob2

res_a = db_obj_tabela.busca_por_campo(tab_bob, 'email', email_a, None) 
assert type(res_a) is list or type(res_a) is tuple
res_a = list(res_a)
verifica_resultado("BC_a_email", res_a, [ id_bob2, ])

carro_b = carro1
res_b = db_obj_tabela.busca_por_campo(tab_bob, 'carro', carro_b, None)
assert type(res_b) is list or type(res_b) is tuple
res_b = list(res_b)
verifica_resultado("BC_b_carro", res_b, [ id_bob1, id_bob4, id_bob5, ])

# Campos exatos:
atrs_c = { 'carro': carro1, 'pernas': 4 }
res_c = db_obj_tabela.busca_por_campos(tab_bob, atrs_c, [ 'nome', 'carro' ])
assert type(res_c) is list or type(res_c) is tuple
res_c = list(res_c)
verifica_resultado("BCS_c_carro_pernas", res_c, [ (nome_bob1, carro1), ])

# Campo aproximado:
nome_m = "~José%"
res_m = db_obj_tabela.busca_por_campo(tab_bob, 'nome', nome_m, None)
assert type(res_m) is list or type(res_m) is tuple
res_m = list(res_m)
verifica_resultado("BCS_m_nomeParc", res_m, [ id_bob1, id_bob2, id_bob3, id_bob4, ])

# Campos aproximados:
atrs_d = { 'nome': "~%José%", 'carro': carro1 }
res_d = db_obj_tabela.busca_por_campos(tab_bob, atrs_d, None)
assert type(res_d) is list or type(res_d) is tuple
res_d = list(res_d)
verifica_resultado("BCS_d_nomeParc_carro", res_d, [ id_bob1, id_bob4, id_bob5, ])

atrs_e = { 'nome': "~%Quarto%", 'carro': carro1 }
res_e = db_obj_tabela.busca_por_campos(tab_bob, atrs_e, None) 
assert type(res_e) is list or type(res_e) is tuple
res_e = list(res_e)
verifica_resultado("BCS_e_nomeParc_carro", res_e, [ id_bob4, ])

atrs_f = { 'pernas': ( 0, 4, ) }
res_f = db_obj_tabela.busca_por_campos(tab_bob, atrs_f, None) 
assert type(res_f) is list or type(res_f) is tuple
verifica_resultado("BCS_f_pernas_intv", res_f, [ id_bob1, id_bob2, id_bob3, id_bob4, id_bob5, ])

atrs_g = { 'pernas': ( 0, 3, ) }
res_g = db_obj_tabela.busca_por_campos(tab_bob, atrs_g, None) 
assert type(res_g) is list or type(res_g) is tuple
verifica_resultado("BCS_g_pernas_intv", res_g, [ id_bob2, id_bob4, id_bob5, ])

atrs_h = { 'nome': "~%to %", }
res_h = db_obj_tabela.busca_por_campos(tab_bob, atrs_h, None) 
assert type(res_h) is list or type(res_h) is tuple
res_h = list(res_h)
verifica_resultado("BCS_h_nomeParc_bco", res_h, [ id_bob4, id_bob5, ])

atrs_i = { 'email': "~%@gmail%", }
res_i = db_obj_tabela.busca_por_campos(tab_bob, atrs_i, None) 
assert type(res_i) is list or type(res_i) is tuple
res_i = list(res_i)
verifica_resultado("BCS_i_emailParc", res_i, [ id_bob1, id_bob5, ])

atrs_j = { 'nome': "~%Qu%to%", }
res_j = db_obj_tabela.busca_por_campos(tab_bob, atrs_j, None) 
assert type(res_j) is list or type(res_j) is tuple
res_j = list(res_j)
verifica_resultado("BCS_j_emailParc", res_j, [ id_bob4, id_bob5, ])

atrs_k = { 'nome': "~% d_ S___a%", }
res_k = db_obj_tabela.busca_por_campos(tab_bob, atrs_k, None) 
assert type(res_k) is list or type(res_k) is tuple
res_k = list(res_k)
verifica_resultado("BCS_i_emailParc", res_k, [ id_bob1, id_bob2, id_bob3, id_bob4, id_bob5, ])

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.atualiza_objeto}:\n")

atrs_mod1 = {
  "nome": "Josegrosso de Souza",
  "email": "grosso@hotmail.com"
}
db_obj_tabela.atualiza_objeto(tab_bob, def_bob, id_bob1, atrs_mod1)
bob1_c = db_obj_tabela.obtem_objeto(tab_bob, def_bob, id_bob1)
for chave, val in atrs_mod1.items():
  atrs_bob1[chave] = val
mostra_bob("bob1_c", bob1_c, id_bob1, atrs_bob1)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {db_obj_tabela.num_entradas}:\n")
res = db_obj_tabela.num_entradas(tab_bob)
sys.stderr.write("   numero de entradas = \"" + str(res) + "\"\n")
# verifica o tipo
assert type(res) == int
# verifica o valor
assert res == num_elementos

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Alguns testes falharam.", True)

# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)

