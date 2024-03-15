# Imlementação do módulo {db_tabela_generica}.

import db_base_sql
import util_identificador
from util_testes import erro_prog, mostra

import sys # Para depuração.

# FUNÇÕES INTERNAS

tbg_debug = False

def constroi_colunas_SQL(cols):
  """Constrói a descrição SQL das colunas de uma tabela, 
  dada a lista de propriedades {cols} como fornecida
  a {cria_tabela}.  Omite colunas com tipo SQL {None}."""
  colunas = "indice integer NOT NULL PRIMARY KEY"
  for cp in cols:
    chave = cp[0]
    tipo_SQL = cp[2]
    if tipo_SQL != None:
      # O campo é uma coluna da tabela.
      nulo_ok = cp[3] # O valor da coluna pode ser NULL?
      colunas = colunas + ", " + chave + " " + tipo_SQL + (' NOT NULL' if not nulo_ok else '')
  return colunas

def extrai_nomes_de_colunas_SQL(cols):
  """Extrai a lista dos nomes das colunas de uma tabela, 
  dada a lista de propriedades {cols} como fornecida
  a {cria_tabela}.  Omite colunas com tipo SQL {None}."""
  nomes = [].copy()
  for cp in cols:
    chave = cp[0]
    tipo_SQL = cp[2]
    if tipo_SQL != None:
      # O campo é uma coluna da tabela.
      nomes.append(chave)
  return nomes

# IMPLEMENTAÇÕES

def cria_tabela(nome_tb, cols):
  colunas = constroi_colunas_SQL(cols)
  res = db_base_sql.executa_comando_CREATE_TABLE(nome_tb, colunas);
  if res != None:
    sys.stderr.write("  CREATE TABLE = \"%s\"\n" % str(res))
    assert type(res) is str
    erro_prog("CREATE_TABLE falhou " + str(res))
  return

def acrescenta(nome_tb, cache, let, cols, def_obj, atrs_SQL):
  # Descobre o indice da última entrada na tabela:
  num_ents = db_base_sql.num_entradas(nome_tb, 'indice')
  if not type(num_ents) is int:
    erro_prog("db_base_sql.num_entradas: result = '" + str(num_ents) + "'")
  # Tenta criar o objeto:
  ind = num_ents + 1 # Indice esperado do objeto na tabela.
  ident = util_identificador.de_indice(let, ind)
  obj = def_obj(None, ident, atrs_SQL)
  # Insere na base de dados e obtém o índice na mesma:
  ind_insert = db_base_sql.executa_comando_INSERT(nome_tb, atrs_SQL)
  if (not type(ind_insert) is int) or (ind_insert != ind):
    erro_prog("indice de inserção inválido " + str(ind))
  cache[ident] = obj
  return obj

def atualiza(nome_tb, cache, let, cols, def_obj, ident, mods_SQL):
  # Obtém o objeto com esse identificador e garante que está em {cache}:
  obj = busca_por_identificador(nome_tb, cache, let, cols, def_obj, ident)
  if obj == None:
    # Objeto não existe:
    erro_prog("identificador '" + ident + "' nao encontrado")
  # Atualiza os atributos do objeto na memória:
  res = def_obj(obj, ident, mods_SQL)
  assert res == obj
  # Atualiza a base de dados:
  ind = util_identificador.para_indice(let, ident)
  cond = "indice = " + str(ind)
  res = db_base_sql.executa_comando_UPDATE(nome_tb, cond, mods_SQL)
  if res != None:
    erro_prog("UPDATE da tabela '" + nome_tb + "' falhou")
  return obj

def busca_por_identificador(nome_tb, cache, let, cols, def_obj, ident):
  if ident in cache:
    return cache[ident]
  else:
    ind = util_identificador.para_indice(let, ident)
    return busca_por_identificador_e_indice(nome_tb, cache, let, cols, def_obj, ident, ind)
    
def busca_por_indice(nome_tb, cache, let, cols, def_obj, ind):
  ident = util_identificador.de_indice(let, ind)
  if ident in cache:
    return cache[ident]
  else:
    return busca_por_identificador_e_indice(nome_tb, cache, let, cols, def_obj, ident, ind)
    
def busca_por_identificador_e_indice(nome_tb, cache, let, cols, def_obj, ident, ind):
  """Função interna: mesmo que {busca_por identificador}, mas exige o índice inteiro {ind}
  da linha da tabela, além do identificador {ident}."""
  cond = "indice = " + str(ind)
  col_nomes = extrai_nomes_de_colunas_SQL(cols)
  res = db_base_sql.executa_comando_SELECT(nome_tb, cond, col_nomes)
  if tbg_debug: sys.stderr.write("  > busca_por_identificador_e_indice: res = " + str(res) + "\n")
  if res == None:
    return None
  res = list(res)
  if len(res) == 0:
    return None
  elif len(res) > 1:
    erro_prog("SELECT com índice em '" + nome_tb + "' não é único, res = " + str(res))
  col_vals = list(res[0])
  assert len(col_vals) == len(col_nomes)
  atrs_SQL = dict(zip(col_nomes, col_vals))
  obj = def_obj(None, ident, atrs_SQL)
  cache[ident] = obj
  return obj

def busca_por_campo(nome_tb, let, cols, chave, valor, res_cols):
  # Converte {valor} para string na linguagem SQL:
  if tbg_debug: sys.stderr.write(f"  > db_tabela_generica.busca_por_campo_IMP: chave = {chave} valor = {str(valor)}\n");
  valor = db_base_sql.codifica_valor(valor)

  # Supõe que o cache é um subconjuto da base em disco, então procura só na última:
  cond = chave + " = " + valor
  if res_cols == None:
    cols = ['indice']
  else:
    cols = res_cols
  res = db_base_sql.executa_comando_SELECT(nome_tb, cond, cols)
  if res == None:
    res = [].copy()
  elif type(res) is str:
    erro_prog("SELECT falhou " + str(res))
  else:
    if res_cols == None:
      # Converte lista de índices para lista de identificadores:
      res = util_identificador.de_lista_de_indices(let, res)
  return res

def busca_por_campos(nome_tb, let, cols, args, res_cols):
  # Supõe que o cache é um subconjuto da base em disco, então procura só na última.
  # Converte {args} para condição na linguagem SQL:
  cond = ""
  sep = ""
  for ch,val in args.items():
    compador = " = " if val is not None else " IS "
    val_sql = db_base_sql.codifica_valor(val)
    cond = cond + sep + ch + compador + val_sql
    sep = " AND "
  if res_cols == None:
    cols = ['indice']
  else:
    cols = res_cols
  res = db_base_sql.executa_comando_SELECT(nome_tb, cond, cols)
  if res == None:
    res = [].copy()
  elif type(res) is str:
    erro_prog("SELECT falhou " + str(res))
  else:
    if res_cols == None:
      # Converte lista de índices para lista de identificadores:
      res = util_identificador.de_lista_de_indices(let, res)
  return res

def busca_por_semelhanca(nome_tb, let, cols, chaves, valores):
  cond = ""
  for key in chaves:
    for value in valores:
      cond += (key + " LIKE '%" + value + "%' OR ")
  cond = cond[:-4]
  res = db_base_sql.executa_comando_SELECT(nome_tb, cond, ['indice'])
  if res != None and type(res) is str:
    erro_prog("SELECT falhou " + str(res))
  if tgb_debug: sys.stderr.write("  > busca_por_semelhanca: res = " + str(res) + "\n")
  res = util_identificador.de_lista_de_indices(let, res)
  return res

def limpa_tabela(nome_tb, cols):
  res = db_base_sql.executa_comando_DROP_TABLE(nome_tb);
  if res != None:
    assert type(res) is str
    erro_prog("DROP_TABLE de " + nome_tb + " falhou, res = '" + str(res) + "' falhou")
  cria_tabela(nome_tb, cols)
  return
  
