# Implementação do módulo {usuario} e da classe {obj_usuario.Classe}.

import db_base_sql
import util_identificador
import db_obj_tabela
import obj_raiz
from util_erros import erro_prog, aviso_prog
import sys

# Definição interna da classe {db_obj_tabela.Classe}:

tabelas_criadas = set()

class Classe_IMP:

  def __init__(self, nome, letra, colunas, classe):
    self.nome = nome
    self.letra = letra
    self.colunas = colunas
    self.classe = classe
    self.cache = {}
    self.debug = False

def cria_tabela(nome, letra, classe, colunas, limpa):
  if nome in tabelas_criadas:
    erro_prog(f"tabela {nome} já foi criada nesta execução")
  tab = db_obj_tabela.Classe(nome, letra, colunas, classe)
  existe = existe_tabela_SQL(tab.nome)
  if existe:
    if limpa:
      sys.stderr.write(f"  limpando a tabela {nome}\n")
      limpa_tabela_SQL(tab.nome)
      existe = False
    else:
      ne = num_entradas(tab)
      sys.stderr.write(f"  tabela {tab.nome} já existe com {ne} entradas, mantendo\n")
  if not existe:
    sys.stderr.write(f"  criando a tabela {tab.nome}\n")
    cria_tabela_SQL(tab.nome, tab.colunas)
  # Lembra que criou um {obj_db_tabela.Classe} para este {nome}:
  tabelas_criadas.add(tab.nome)
  return tab

def muda_diagnosticos(tab, val):
  tab.debug = val
  return

def acrescenta_objeto(tab, def_obj, atrs_SQL):
  # Descobre o indice da última entrada na tabela:
  num_ents = num_entradas(tab)
  # Tenta criar o objeto:
  ind = num_ents + 1 # Indice esperado do objeto na tabela.
  ident = util_identificador.de_indice(tab.letra, ind)
  obj = def_obj(None, ident, atrs_SQL)
  assert obj != None and isinstance(obj, tab.classe)
  # Insere na base de dados e obtém o índice na mesma:
  ind_insert = db_base_sql.executa_comando_INSERT(tab.nome, atrs_SQL)
  if (not type(ind_insert) is int) or (ind_insert != ind):
    erro_prog("indice de inserção inválido " + str(ind))
  tab.cache[ident] = obj
  return obj

def atualiza_objeto(tab, def_obj, ident, mods_SQL):
  # Obtém o objeto com esse identificador e garante que está em {cache}:
  obj = obtem_objeto(tab, def_obj, ident)
  if obj == None:
    # Objeto não existe:
    erro_prog("identificador '" + ident + "' nao encontrado")
  else:
    assert isinstance(obj, tab.classe)
  # Atualiza os atributos do objeto na memória:
  res = def_obj(obj, ident, mods_SQL)
  assert res == obj
  # Atualiza a base de dados:
  ind = util_identificador.para_indice(tab.letra, ident)
  cond = "indice = " + str(ind)
  res = db_base_sql.executa_comando_UPDATE(tab.nome, cond, mods_SQL)
  if res != None:
    erro_prog("UPDATE da tabela '" + tab.nome + "' falhou")
  return obj

def obtem_objeto(tab, def_obj, ident):
  if ident in tab.cache:
    obj = tab.cache[ident]
    assert obj != None
  else:
    ind = util_identificador.para_indice(tab.letra, ident)
    if tab.debug: sys.stderr.write("obtem_objeto %s -> %s\n" % (fname, str(ident), str(ind)))
    obj = obtem_objeto_e_indice(tab, def_obj, ident, ind)
  return obj
    
def busca_por_indice(tab, def_obj, ind):
  ident = util_identificador.de_indice(tab.letra, ind)
  if ident in tab.cache:
    obj = tab.cache[ident]
    assert obj != None
  else:
    obj = obtem_objeto_e_indice(tab, def_obj, ident, ind)
  return obj
    
def obtem_objeto_e_indice(tab, def_obj, ident, ind):
  """Função interna: mesmo que {busca_por identificador}, mas exige o índice inteiro {ind}
  da linha da tabela, além do identificador {ident}."""
  cond = "indice = " + str(ind)
  col_nomes = extrai_nomes_de_cols_SQL(tab.colunas)
  res = db_base_sql.executa_comando_SELECT(tab.nome, cond, col_nomes)
  if tab.debug: sys.stderr.write("  > obtem_objeto_e_indice: res = " + str(res) + "\n")
  if res == None:
    obj = None
  elif not (type(res) is list or type(res) is tuple): 
    erro_prog("SELECT com índice em '" + tab.nome + "' resultado = " + str(res) + "não é nem {None} nem lista")
  elif len(res) == 0:
    obj = None
  elif len(res) > 1:
    erro_prog("SELECT com índice em '" + tab.nome + "' resultado = " + str(res) + " não é único")
  else:
    col_vals = res[0]
    if not (type(col_vals) is list or type(col_vals) is tuple): 
      erro_prog("SELECT com índice em '" + tab.nome + "' resultado = " + str(res) + " não é lista de listas")
    assert len(col_vals) == len(col_nomes)
    atrs_SQL = dict(zip(col_nomes, col_vals))
    obj = def_obj(None, ident, atrs_SQL)
    assert obj != None and isinstance(obj, tab.classe)
    tab.cache[ident] = obj
  return obj

def busca_por_campo(tab, chave, valor, res_cols):
  # Converte {valor} para string na linguagem SQL:
  if tab.debug: sys.stderr.write(f"  > db_obj_tabela.busca_por_campo_IMP: chave = {chave} valor = {str(valor)}\n");
  
  args = { chave: valor, }
  return busca_por_campos(tab, args, res_cols)

def busca_por_campos(tab, args, res_cols):
  # Supõe que o cache é um subconjuto da base em disco, então procura só na última.

  # !!! Verificar a lógica de {res_cols} etc. !!!
  # !!! Melhorar comportamento em caso de erro. !!!

  # Converte {args} para uma condição {cond} na liguagem SQL:
  cond = ""
  sep = ""
  for chave, val in args.items():
    # !!! Deveria validar o campo {chave,val} contra colunas da tabela {tab} !!!
    if val == None:
      termo = busca_por_campos_termo_nulo(chave)
    else:
      # Se {val} for um objeto, converte para identificador:
      if isinstance(val, obj_raiz.Classe):
        val = obj_raiz.obtem_identificador(val)
        assert val != None and isinstance(val, str)
 
      # Descobre tipo da busca:
      if type(val) is str and len(val) >= 2 and val[0] == "~":
        # Busca aproximada.
        val = val[1:]  # Remove o '~'.
        termo = busca_por_campos_termo_semelhanca(chave, val)
      elif (isinstance(val, list) or isinstance(val, tuple)) and len(val) == 2: 
        # Busca por intervalo.
        val_min = val[0]
        val_max = val[1]
        for val_end in val_min, val_max:
          if not (isinstance(val_end, str) or isinstance(val_end, int) or isinstance(val_end, float)):
            erro_prog(f"valor extremo {str(val_end)} tem tipo inválido")
        termo = busca_por_campos_termo_intervalo(chave, val_min, val_max)
      elif isinstance(val, str) or isinstance(val, int) or isinstance(val, float): 
        # Busca por valor exato:
        if isinstance(val, str) and len(val) == 0:
          erro_prog(f"busca por cadeia vazia")
        termo = busca_por_campos_termo_identidade(chave, val)

    cond += (sep + termo)
    sep = " AND "

  if res_cols == None:
    # Por default, devolve lista de identificadores:
    colunas = ['indice']
  else:
    colunas = res_cols
    
  # Executa a busca:
  res = db_base_sql.executa_comando_SELECT(tab.nome, cond, colunas)
  
  # Finaliza o resultado:
  if res == None:
    # Não achou nada:
    res = []
  elif isinstance(res, str):
    # {res} deve ser uma mensagem de erro:
    erro_prog("SELECT falhou " + str(res))
  else:
    # {res} deve ser uma lista de índices, ou de tuplas de valores das colunas pedidas:
    if res_cols == None:
      # Converte lista de índices para lista de identificadores:
      res = util_identificador.de_lista_de_indices(tab.letra, res)
  return res

def num_entradas(tab): 
  num_ents = db_base_sql.num_entradas(tab.nome, 'indice')
  if not type(num_ents) is int:
    erro_prog("db_base_sql.num_entradas: result = '" + str(num_ents) + "'")
  return num_ents
 
# FUNÇÕES INTERNAS

def existe_tabela_SQL(nome):
  res = db_base_sql.executa_comando_TABLE_EXISTS(nome)
  if not type(res) is bool:
    erro_prog("db_base_sql.executa_comando_TABLE_EXISTS result = '" + str(res) + "'")
  return res
    
def cria_tabela_SQL(nome, colunas):
  cols_SQL = converte_colunas_para_cols_SQL(colunas)
  res = db_base_sql.executa_comando_CREATE_TABLE(nome, cols_SQL);
  if res != None:
    erro_prog(f"CREATE_TABLE falhou: {res}")
  return

def limpa_tabela_SQL(nome):
  res = db_base_sql.executa_comando_DROP_TABLE(nome);
  if res != None:
    assert type(res) is str
    erro_prog("DROP_TABLE de " + nome + " falhou, res = '" + str(res) + "' falhou")
  return

def converte_colunas_para_cols_SQL(colunas):
  """Constrói a descrição SQL das colunas de uma tabela, 
  dada a lista de propriedades {colunas} como fornecida
  a {cria_tabela_SQL}.  Omite colunas com tipo SQL {None}."""
  cols_SQL = "indice integer NOT NULL PRIMARY KEY"
  for cp in colunas:
    chave = cp[0]
    tipo_SQL = cp[2]
    if tipo_SQL != None:
      # O campo é uma coluna da tabela.
      nulo_ok = cp[3] # O valor da coluna pode ser NULL?
      cols_SQL += \
        ", " + chave + " " + tipo_SQL + (' NOT NULL' if not nulo_ok else '')
  return cols_SQL

def extrai_nomes_de_cols_SQL(colunas):
  """Extrai a lista dos nomes das colunas de uma tabela, 
  dada a lista de propriedades {colunas} como fornecida
  a {cria_tabela_SQL}.  Omite colunas com tipo SQL {None}."""
  nomes = []
  for cp in colunas:
    chave = cp[0]
    tipo_SQL = cp[2]
    if tipo_SQL != None:
      # O campo é uma coluna da tabela.
      nomes.append(chave)
  return nomes
 
def busca_por_campos_termo_nulo(chave):
  """Devolve o termo de uma condição SQL que exige que o campo da coluna
  {chave} da tabela seja nulo; isto é, "{chave} IS NULL". """
  termo = f"{chave} IS NULL"
  return termo

def busca_por_campos_termo_identidade(chave, val):
  """Devolve o termo de uma condição SQL que exige que o campo da coluna
  {chave} da tabela seja exatamente {val}; isto é, "{chave} = {val-san}"
  onde {val_san} é {val}
  oportunamente sanitizado e convertido."""
  val_sql = db_base_sql.codifica_valor(val)
  termo = chave + " = " + val_sql
  return termo

def busca_por_campos_termo_semelhanca(chave, val):
  """Devolve o termo de uma condição SQL que exige que o campo da coluna
  {chave} da tabela case o padrão {val}, ignorando maiúsculas/minúsculas. 
  Ou seja, "{chave} LIKE '{val_san}' onde {val_san} é {val}
  oportunamente sanitizado e convertido."""
  
  assert isinstance(val, str), "valor de tipo inválido"
  min_compr = 3 # Comprimento mínimo para busca parcial.
  if len(val) < min_compr:
    erro_prog(f"cadeia '{val}' muito curta para busca parcial (minimo {min_compr} caracteres)")
  chave_sql = chave + ")"
  val_sql = db_base_sql.codifica_valor(val.lower())
  assert len(val_sql) >= 2 and val_sql[0] == "'" and val_sql[-1] == "'"
  termo = "LOWER(" + chave + ") LIKE " + val_sql
  return termo

def busca_por_campos_termo_intervalo(chave, val_min, val_max):
  """Devolve o termo de uma condição SQL que exige que o campo da coluna
  {chave} da tabela esteja entre {val_min} e {val_max}, ambos inclusive. 
  Ou seja, " {chave} BETWEEN {val_min_sql} AND {val_max_sql}
  onde {va_min_sql} e {val_max_sql} são {val_min} e {val_max} 
  oportunamente sanitizados e convertido."""
  
  if isinstance(val_min, str) and isinstance(val_max, str):
    # Both strings.
    pass
  elif (isinstance(val_min, int) or isinstance(val_min, float)) and  (isinstance(val_max, int) or isinstance(val_max, float)):
    # Both numeric.
    pass
  else:
    erro_prog(f"limites {str(val_min)} e {str(val_max)} de tipos inválidos ou incompatíveis")
  
  val_min_sql = db_base_sql.codifica_valor(val_min)
  val_max_sql = db_base_sql.codifica_valor(val_max)

  termo = f"( {chave} BETWEEN {val_min_sql} AND {val_max_sql} )"
  return termo
