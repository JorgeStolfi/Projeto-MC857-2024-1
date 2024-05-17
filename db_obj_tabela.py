import db_obj_tabela_IMP

# Funções para manipular tabelas da base de dados.

# Cada tabela SQL tem uma columa de tipo inteiro, 'indice' que é a chave primária
# Esta coluna é incrementada automaticamente pela biblioteca SQL 
# sempre que um objeto é acrescentado à tabela.  A primeira entrada
# em cada tabela tem índice 1.

class Classe(db_obj_tabela_IMP.Classe_IMP):
  """
  Um objeto desta classe descreve uma das tabelas da base de dados.
  
  Cada objeto desta classe possui os seguintes campos privados:
  
    {.nome}          {str}  Nome da tabela ("usuarios", "videos", etc.)
    {.letra}         {str}  Prefixo dos identificadores ("U", "V", etc.)
    {.classe}        {type} Subclasse dos objetos armazenados na tabela.
    {.colunas}       {list} Lista de tuplas descrevendo as colunas da tabela.
    {.cache}         {dict} Cache de objetos lidos da tabela.
    {.debug}         {bool} Se {True}, imprime diagnósticos das operações da tabela.
    
  O atributo {.colunas} é uma lista de listas que descreve as colunas da tabela.
  Vide a documentação de {cria_tabela} abaixo.
  
  O atributo {.classe} deve ser um tipo de subclasse de {obj_raiz.Classe},
  como {obj_usuario.Classe}, {obj_video.Classe}, etc.
  
  A classe {db_obj_tabela.Classe} NÃO é uma subclasse de {obj_raiz.Classe}.
  
  CONVERSÕES MEMÓRIA <-> DISCO
        
  Certos valores de atributos na memória exigem conversão para poderem ser
  armazenados ou recueperados da base em disco.  Por exemplo, um atributo
  que tem tipo {bool} na memória é gravado na base como um valor de tipo SQL
  'INTEGER', que é 0 se {False}, 1 se {True}.  Se o valor de um atributo na
  memória é um objeto {obj} (por exemplo, o atributo 'dono' de uma sessão, que é
  um {obj_usuario.Classe}), a coluna correspondente na base de dados terá tipo 
  SQL 'INTEGER', e o valor será o índice do objeto {obj} na sua 
  respectiva tabela.
  
  FUNCIONAMENTO DO CACHE
  
  O atributo {.cache} é um dict que mapeia identificadores para objetos
  do tipo {classe} que espelham na memória algumas das linhas da tabela.
  Sua função é evitar leituras desnecessárias da tabela, e garantir que
  não há duas ou mais cópias de cada objeto na memória. O cache é
  gerenciado automaticamente pelas funções {acrescenta_objeto}, {atualiza_objeto},
  {obtem_objeto}, e {busca_por_indice} abaixo.
  
  Cada objeto no cache é uma cópia fiel de uma linha da tabela, exceto
  que os valores são convertidos de tipos compatíveis com SQL para tipos
  Python na memória.
  
  A função {obtem_objeto} de da subclasse {classe} primeiro
  procura o objeto no {.cache} da tabela correspondente. Se encontrar,
  devolve esse objeto. Se não encontrar, lê linha da tabela, cria o
  objeto na memória, e acrescenta ao cache.
  
  A função {atualiza_objeto} da subclasse {classe} altera o objeto na
  memória e imediatamente modifica a linha correspondente da tabela.
  """
  pass

# Nas funções abaixo,
# 
#   {atrs_SQL} é um dicionário Python com os atributos do objeto, menos o
#     identificador, tal como representados na base de dados SQL.
#
#   {def_obj} é uma função que é chamada pelas funções abaixo para
#     construir ou modificar objetos na memória, dados seus atributos na
#     base de dados. Ela recebe parâmetros {(obj,ident,atrs_SQL)} onde
#     {obj} é {None} ou um objeto da classe associada à tabela
#     ({obj_usuario.Classe}, {obj_sessao.Classe}, etc.); {ident} é um identificador de
#     objetos dessa classe ("U-{NNNNNNNN}", "P-{NNNNNNNN}", etc.); e
#     {atrs_SQL} é um dicionário que associa nomes de colunas a seus
#     valores.
#
#     Se {obj} for {None}, a função {def_obj} deve criar um novo objeto
#     da classe correta, com identificador {ident} e atributos
#     {atrs_SQL}. Neste caso, {atrs_SQL} deve ter todas as colunas da
#     tabela. 
#
#     Se {obj} não é {None}, {def_obj} deve alterar os campos do
#     objeto {obj} dado. Neste caso, {atrs_SQL} pode ter apenas um
#     subconjuto das colunas da tabela; campos ausentes não serão
#     modificados.
#     
#     Nos dois casos, a função {def_obj} terá que converter
#     os valores em {atrs_SQL} do formato SQL para o formato na memória
#     como especificado em {tab.colunas}, e devolver o objeto criado ou modificado.
# 
#     A função {def_obj} é chamada quando a entrada do objeto {obj}
#     no cache está inconsistente com sua linha na base de dados.
#     Portanto, a função {def_obj} não deve tentar fazer buscas na 
#     tabela {tab}, nem acessar essa linha dessa tabela.
#     Ela pode porém chamar {obtem_objeto} para 
#     converter campos de {atrs_SQL} que são identificadores 
#     para objetos.
#
# Em caso de erro, as funções abaixo abortam com mensagem de erro.

# Implementação da interface:
import db_obj_tabela_IMP

def cria_tabela(nome, letra, classe, colunas, limpa):
  """
  Cria a tabela {nome} dentro da base de dados, com as colunas
  descritas em {colunas}.  Também cria um objeto {tab} de tipo
  {db_obj_tabela.Classe} onde os argumentos acima são armazenados.

  Esta função deve ser chamada apenas uma vez para o cada {nome}.
  Se a tabela {nome} já existe na base de dados em disco, 
  preserva as entradas da mesma; a menos que {limpa} seja
  {True}, caso em que apaga todas as entradas.
  
  O parâmetro {colunas} é uma seqüência de tuplas. Cada tupla 
  descreve uma coluna da tabela (exceto o índice) e o atributo
  correspondente dos objetos do tipo {classe}.
  Cada tupla {colunas[k]} tem os seguintes elementos: 
   
    [0] A chave do atributo (um string, por exemplo 'nome' ou 'telefone'),
   
    [1] O tipo Python do atributo (por exemplo, {type(int)})
   
    [2] O tipo SQL usado para armazenar o atributo na base
        (por exemplo, 'INTEGER' ou 'TEXT').
       
    [3] Um booleano que diz se a coluna pode ser {NULL} na 
      tabela SQL e {None} no objeto na memória.
      
  Se o tipo de um atributo na memória é lista, tupla, ou dicionário,
  esse atributo não pode ser armazenado numa coluna da base SQL.
  Nesse caso o item [2] da descrição acima deve ser {None}, e o 
  item [3] é irrelevante.

  Esta função deveria ser chamada apenas uma vez em cada 
  inicialização do servidor, depois de chamar {db_base_sql.conecta}.
  """
  return db_obj_tabela_IMP.cria_tabela(nome, letra, classe, colunas, limpa)

def acrescenta_objeto(tab, def_obj, atrs_SQL):
  """Acrescenta mais um objeto {obj} com atributos {atrs_SQL} na tabela {nome} 
  da base {bas}, e também no seu {tab.cache}. Cada valor de {atrs_SQL} 
  deve ser consistente com os tipo SQL especificado por {tab.colunas}. 
  Devolve o objeto criado {obj}.
  
  O identificador {id_obj} do objeto será "{let}-{ind}", onde {ind} é o
  índice da linha correspondente na tabela, formatado em 8 dígitos. 
  
  A função chamará {obj=def_obj(None,id_obj,atrs_SQL)} para criar o objeto
  {obj} na memória, depois de acrescentar a linha no banco de dados mas
  antes de atualizar o cache."""
  return db_obj_tabela_IMP.acrescenta_objeto(tab, def_obj, atrs_SQL)

def atualiza_objeto(tab, def_obj, ident, mods_SQL):
  """Procura na tabela em disco {tab.nome} e no seu {cache}
  um objeto {obj} com o identificador {ident}, que deve ter a forma 
  "{let}-{ind}" onde {ind} é o índice na tabela.  O objeto 
  deve existir.  Se o objeto não estiver no {cache}, cria o mesmo
  com {obj=def_obj(None,ident,atrs_SQL)} onde {atrs_SQL} são os campos 
  atuais da linha da tabela.
  
  Em qualquer caso, para cada entada {chv:val_novo} no dicionário
  {mods_SQL}, esta função substitui o valor corrente da coluna {chv}
  dessa linha por {val_novo}. As chaves de {mods_SQL} devem ser um
  subconjuto dos nomes das colunas da tabela, como definido em {colunas}.
  Em seguida modifica os campos do objeto {obj} na memória chamando
  {def_obj(obj,ident,mods_SQL)}.  
  
  A função devolve o próprio objeto {obj}."""
  return db_obj_tabela_IMP.atualiza_objeto(tab, def_obj, ident, mods_SQL)

def obtem_objeto(tab, def_obj, ident):
  """Procura na tabela {tab} um objeto com o identificador {ident}, que deve ter a forma 
  "{let}-{ind}" onde {ind} é o índice na tabela. 
  
  Mais precisamente, se já existir um objeto {obj} com identificador {ident}
  no cache da tabela, pega esse objeto.  Caso contrário
  extrai da tabela em disco {tab.nome} a linha com índice {ind},
  cria um objeto {obj} chamando {def_obj(None,ident,atrs_SQL)} onde {atrs_SQL} é
  o conteúdo dessa linha, e armazena esse objeto {obj} no cache.  Nos dois casos, devolve o 
  objeto {obj}.  Se não existir a linha {ind} na tabela em disco, devolve {None}."""
  return db_obj_tabela_IMP.obtem_objeto(tab, def_obj, ident)

def busca_por_indice(tab, def_obj, ind):
  """Mesmo que {obtem_objeto}, mas quer o indice inteiro {ind} da linha da tabela,
  em vez do identificador do objeto."""
  return db_obj_tabela_IMP.busca_por_indice(tab, def_obj, ind)

def busca_por_campo(tab, chave, valor, res_cols):
  """
  Procura na tabela {tab} objetos que tem o valor {val}
  na coluna de nome {chave}.  Equivalente a 
  {busca_por_campos(tab, { chave: valor }, res_cols)}.
  """
  return db_obj_tabela_IMP.busca_por_campo(tab, chave, valor, res_cols)

def busca_por_campos(tab, args, res_cols):
  """
  Procura na tabela {tab} linhas com certos valores 
  em certas colunas, especificados pelo dicionário {args}.  
  
  Basicamente, para cada par {ch,val} em {args}, exige que a coluna {ch} da tabela
  tenha valor {val}.  O valor {val} pode ser {str}, {int}, ou {float}. 
  
  Entretanto, se {val} é um string que começa com o caracter "~",
  supõe que o restante de {val} é um padrão SQL para uso com o operador "LIKE".
  Nesse caso, cada caractere '_' em {val} casa um caractere arbitrário 
  no dado da tabela, e cada caractere '%' casa 0 ou mais
  caracteres arbitrários. Além diso, a distinção de letras maiúsculas e
  minúsculas será ignorada. Por exemplo, a busca com {val} "~%siLVa%" casaria com
  entradas na tabela cujo valor for "João da Silva" ou "Donasilvana".
  O padrão {val} "~jo__ %" casaria com "José da Silva",
  "João Nabuco", mas não com "Maria José Costa".  O padrão {val} "~%jo%e%"
  casaria com "João Jorge Silva", "Josefina Costa",
  "Juca Feijoeiro", e "Josias Abreu".
  
  Por outro lado, se {val} for uma lista ou tupla de dois elementos
  {( val_min, val_max )}, exige que o valor na coluna {ch} da tabela
  esteja entre {val_min} e {val_max}. Os dois valores podem ser {str},
  {int}, ou {float}.
  
  Finalmente, se {val} for um objeto derivado de {obj_raiz.Classe},
  como {obj_usuario.Classe} ou {obj_video.Classe}, exige que 
  o campo na coluna {ch} da tabela seja o identificador desse obejto.
  """
  return db_obj_tabela_IMP.busca_por_campos(tab, args, res_cols)

def muda_diagnosticos(tab, val):
  """Liga (se {val} é {True}) ou desliga (se {val} é {False}) os 
  diagnósticos na tabela {tab}.  Retorna {None}."""
  return db_obj_tabela_IMP.muda_diagnosticos(tab, val)

def num_entradas(tab):
  """Retorna o número {N} de objetos presentes na tabla {tab.nome}.
  Os índices dos objetos variam de 1 a {N}."""
  return db_obj_tabela_IMP.num_entradas(tab)
