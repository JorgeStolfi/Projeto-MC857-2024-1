# Este módulo oferece funções para converter valores 
# entre o formato de memória ({mem}), usado em variáveis e campos
# de objetos Python, e o formato usado na base de dados SQL.

# Implementação desta interface:
import db_conversao_sql_IMP

def valor_mem_para_valor_SQL(nome, val_mem, tipo_mem, tipo_SQL, nulo_ok):
  """
  Converte um valor de atributo {val_mem} de tipo Python {tipo_mem}
  para o tipo {tipo_SQL} usado na base de dados.
  
  Em particular, 
  
    Se {tipo_mem} é {bool}, o {tipo_SQL} deve ser 'INTEGER'; e o
    resultado é 0 se {val_mem=False}) e 1 {se val_mem=True}.
    
    Se {tipo_mem} é uma subclasse de {obj_raiz.Classe}, o {tipo_SQL}
    deve ser 'TEXT'; e o objeto {val_mem} é substituído pelo seu
    identificador "{L}-{NNNNNNNN}", obtido com
    {obj_raiz.obtem_identificador(val_mem)}.
  
  Se o parametro {nulo_ok} for {True}, o valor {val_mem} pode ser {None},
  e nesse caso o resultado será {None}.  Se {nulo_ok} for {False}, o
  valor {val_mem} não pode ser {None}.
    
  O parâmetro {nome} é usado apenas para formar mensagens de erro.
  Esta função aborta com erro se os dados forem inválidos;
  em particular, se o tipo de {val_mem} for uma lista, tupla, ou dicionário.
  """
  return db_conversao_sql_IMP.valor_mem_para_valor_SQL(nome, val_mem, tipo_mem, tipo_SQL, nulo_ok)
 
def valor_SQL_para_valor_mem(nome, val_SQL, tipo_SQL, tipo_mem, nulo_ok, identificador_para_objeto):
  """
  Converte um valor de atributo {val_SQL} do tipo {tipo_SQL} usado na
  base de dados para um valor Python de tipo {tipo_mem}, como ficaria na
  memória.
  
  Em particular, 
  
    Se {tipo_mem} é {bool}, o {tipo_SQL} deve ser 'INTEGER'; e o valor
    inteiro {val_SQL} é convertido para booleano usando a convenção
    0={False}, 1={True}.
    
    Se {tipo_mem} é uma subclasse de {obj_raiz.Classe}, o {tipo_SQL}
    deve ser 'TEXT', e seu valor deve ser o identificador
    "{L}-{NNNNNNNN}" de um objeto dessa classe, que será devolvido.
    Neste último caso, o objeto será obtido pela função
    {obj_raiz.identificador_para_objeto(val_SQL)}.
  
  Se o parametro {nulo_ok} for {True}, o valor {val_mem} pode ser
  {None}, e nesse caso o resultado será {None}. Se {nulo_ok} for
  {False}, o valor {val_mem} não pode ser {None}.
    
  O parâmetro {nome} é usado apenas para formar mensagens de erro. Esta
  função aborta com erro se os dados forem inválidos; em particular, se
  o {tipo_mem} for lista, tupla, ou dicionário.
  """
  return db_conversao_sql_IMP.valor_SQL_para_valor_mem(nome, val_SQL, tipo_SQL, tipo_mem, nulo_ok, identificador_para_objeto)
  
# CONVERSÂO DE DICIONÁRIOS
# 
# As funções abaixo fazem a conversão entre um dicionário
# Python que representa atributos de um objeto na memória
# e outro dicionário que representa o conteúdo de uma 
# linha da tabela SQL.
# 
# Nestas funções, o parâmetro {cols} deve ser uma descrição das 
# colunas da tabela, menos a coluna de índice de linha.
# Vide {db_tabela_generica.cria_tabela}. 
  
def dict_mem_para_dict_SQL(dic_mem, cols, falta_ok):
  """
  Supõe que {dic_mem} é um dicionário Python cujos valores são valores
  da linguagem Python (por exemplo, {float} ou {bool}) e/ou objetos
  definidos pelo software do site (como {obj_usuario.Classe}) Converte
  esses valores para representações correspondentes na base de dados
  SQL, usando {valor_mem_para_valor_SQL} e os tipos SQL especificados 
  na lista {cols}. Devolve um dicionário com esses valores, e as mesmas chaves.
  
  Por exemplo, se {dic_mem} for 
  
  Se {falta_ok} for {True}, os nomes dos campos em {dic_mem} devem ser
  um subconjunto dos nomes de columas especificados em {cols}. O
  dicionário retornado terá apenas esses mesmos campos.
  
  Se {falta_ok} for {False}, todos os campos de {cols} devem estar
  presentes em {dic_mem} (ao menos com valor {None}).
  
  A lista de colunas {cols} não deve ter atributos cujo {tipo_mem} for
  lista, tupla, ou dicionário.
  
  A função aborta em caso de erro, por exemplo atributos não listados em
  {cols}, ou com valor que náo é do {tipo_mem} correspondente.
  """
  return db_conversao_sql_IMP.dict_mem_para_dict_SQL(dic_mem, cols, falta_ok)
  
def dict_SQL_para_dict_mem(dic_SQL, cols, falta_ok, identificador_para_objeto):
  """
  Supõe que {dic_SQL} é um dicionário Python com nomes e valores
  extraídos de uma linha de uma tabela da base de dados. Converte os
  mesmos para nomes e valores usando {valor_SQL_para_valor_mem}.
  
  Os nomes dos campos em {dic_SQL} devem ser um subconjunto dos campos
  definidos em {cols}.  Se {falta_ok} for {False}, todos os campos de {cols}
  devem estar presentes em {dic_mem} (ao menos com valor {None}).
  
  A lista {cols} não deve ter atributos cujo {tipo_mem} for lista, tupla, 
  ou dicionário.
  
  Se houver violações de limites de valores, ou valores forem indevidamente omitidos,
  a função aborta com erro.
  """
  return db_conversao_sql_IMP.dict_SQL_para_dict_mem(dic_SQL, cols, falta_ok, identificador_para_objeto)
  
