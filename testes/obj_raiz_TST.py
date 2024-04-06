#! /usr/bin/python3

import obj_raiz
import db_tabela_generica
import db_tabelas
import db_base_sql
import util_testes
import db_conversao_sql
from util_testes import erro_prog, aviso_prog, mostra
import sys
from obj_raiz import ultimo_identificador

# ----------------------------------------------------------------------
sys.stderr.write("  Conectando com base de dados...\n")
db_base_sql.conecta("DB", None, None)

# ----------------------------------------------------------------------
# Funções de teste:

ok_global = True # Vira {False} se um teste falha.

# ----------------------------------------------------------------------
# Classe de objeto para teste:

class ClasseDeTeste(obj_raiz.Classe):
  
  def __init__(self, id, atrs):
    obj_raiz.Classe.__init__(self, id, atrs)

obj0 = ClasseDeTeste("X-00000000", { }) # An object just to get its type

# ----------------------------------------------------------------------

nome_tb = "objtestes"
sys.stderr.write(f"  Criando uma tabela '{nome_tb} para teste':\n")

letra_tb = "X"
  # Prefixo dos identificadores de testes

cache = {}.copy()
  # Dicionário que mapeia identificadores para os objetos {ClasseDeTeste} na memória.
  # Todo objeto dessa classe que é criado é acrescentado a esse dicionário,
  # a fim de garantir a unicidade dos objetos.

colunas = \
  (
    ( 'coisa',         type(100),   'INTEGER', False ),
    ( 'treco',         type(100),   'INTEGER', False ),
    ( 'lhufas',        type("foo"), 'TEXT',    False ),
  )
  # Descrição das colunas da tabela na base de dados.
 
db_tabela_generica.limpa_tabela(nome_tb, colunas)

# ----------------------------------------------------------------------
def def_obj_mem(obj, id_obj, atrs_SQL):
  """Função que cria ou modifica objeto na memória."""
  global cache, nome_tb, letra_tb, colunas
  if obj == None:
    atrs_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, False, db_tabelas.identificador_para_objeto)
    obj = ClasseDeTeste(id_obj, atrs_mem)
  else:
    assert obj.id == id_obj
    mods_mem = db_conversao_sql.dict_SQL_para_dict_mem(atrs_SQL, colunas, True, db_tabelas.identificador_para_objeto)
    # Modifica os atributos:
    for chave, val in mods_mem.items():
      val_velho = obj.atrs[chave]
      obj.atrs[chave] = val
  return obj

# ----------------------------------------------------------------------
# Funções auxiliares de teste

def verifica_objeto(rotulo, obj, id_obj, atrs, ignore):
  """Testes básicos de consistência do objeto {obj} da classe {ClasseDeTeste}, dados 
  {id_obj} e {atrs} esperados."""
  global ok_global

  sys.stderr.write("  %s\n" % ("-" * 70))
  sys.stderr.write("  verificando usuário %s\n" % rotulo)
  ok = obj_raiz.verifica_criacao(obj, type(obj0), id_obj, atrs, ignore, cache, nome_tb, letra_tb, colunas, def_obj_mem)

  if not ok:
    aviso_prog("teste falhou", True)
    ok_global = False

  sys.stderr.write("  %s\n" % ("-" * 70))
  return
 
def testa_cria_objeto(rotulo, id_obj, atrs):
  """Testa criação de objeto com atributos com {atrs}. Retorna o usuário."""
  obj = obj_raiz.cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)
  verifica_objeto(rotulo, obj, id_obj, atrs, None)
  return obj

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_raiz.cria}:\n")
obj1_atrs = { 'coisa': 100, 'treco': 101, 'lhufas': "cem" }
obj1_ind = 1
obj1_id = ("X-%08d" % obj1_ind)
obj1 = testa_cria_objeto("obj1", obj1_id, obj1_atrs)

obj2_atrs = { 'coisa': 200, 'treco': 201, 'lhufas': "duzentos" }
obj2_ind = 2
obj2_id = ("X-%08d" % obj2_ind)
obj2 = testa_cria_objeto("obj2", obj2_id, obj2_atrs)

obj3_atrs = { 'coisa': 300, 'treco': 301, 'lhufas': "trezentos" }
obj3_ind = 3
obj3_id = ("X-%08d" % obj3_ind)
obj3 = testa_cria_objeto("obj3", obj3_id, obj3_atrs)

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_raiz.muda_atributos}:\n")

obj1_mods = {
  'coisa': 109,
  'lhufas': "cento e nove"
}
obj_raiz.muda_atributos(obj1, obj1_mods, cache, nome_tb, letra_tb, colunas, def_obj_mem)
obj1_atrs_m = obj1_atrs
for k, v in obj1_mods.items():
  obj1_atrs_m[k] = v
verifica_objeto("obj1_d", obj1, obj1_id, obj1_atrs_m, None)

obj_raiz.muda_atributos(obj2, obj2_atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem) # Não deveria mudar os atributos
verifica_objeto("obj2", obj2, obj2_id, obj2_atrs, ('coisa',))

obj2_atrs_m = obj3_atrs.copy()
obj_raiz.muda_atributos(obj2, obj2_atrs_m, cache, nome_tb, letra_tb, colunas, def_obj_mem) # Deveria assumir os valores do obj3
verifica_objeto("obj2_m", obj2, obj2_id, obj2_atrs_m, None)

# ----------------------------------------------------------------------

# Adicione este import ao início do seu código de teste
from obj_raiz import ultimo_identificador

# ...

# Adicione este bloco de código no final do seu script de teste

# ----------------------------------------------------------------------
sys.stderr.write("  testando {obj_raiz.ultimo_identificador}:\n")

# Defina o nome da tabela e a letra do prefixo
nome_tb = "objtestes"
letra_tb = "X"

# Chamada da função ultimo_identificador
ultimo_id = ultimo_identificador(nome_tb, letra_tb)

# Verificação do resultado
if ultimo_id == "X-00000003":  # O identificador esperado com base no exemplo fornecido
    sys.stderr.write("Teste passou: o último identificador foi obtido corretamente.\n")
else:
    erro_prog("Teste falhou: o último identificador não corresponde ao esperado.")

# ----------------------------------------------------------------------

# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminados normalmente.\n")
else:
  erro_prog("Teste falhou")