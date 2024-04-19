# Este módulo define a classe geral de objetos {obj_raiz.Classe}, 
# superclasse de objetos como {obj_usuario.Classe}, {obj_sessao.Classe}, etc.

# Implementação deste módulo e da classe {obj_raiz.Classe}:
import obj_raiz_IMP

class Classe(obj_raiz_IMP.Classe_IMP):
  """
  Um objeto que representa uma entidade genérica do sistems
  (usuário, sessão, vídeo, comentário, etc.) genérico. 
  Cada tipo de entidade tem uma subclasse própria desta classe,
  como {obj_usuario.Classe} ou {obj_video.Classe}.
  
  Uma instância de {obj_raiz.Classe} ou de suas subclasses
  possui os seguintes campos privados:
  
    {.id}    o identificador do objeto: uma string da forma "{X}-{NNNNNNNN}" onde
             {X} é uma letra que identifica o tipo do objeto
             ('U' para {obj_usuario.Classe}, 'S' para {obj_sessao.Classe}, etc)
             e {NNNNNNNN} é o índice na tabela correspondente
             da base de dados, formatado em 8 algarismos
                      
    {.atrs}  um dicionário Python que contém os demais atributos 
             do objeto, específicos para cada subclasse.

  REPRESENTAÇÃO NA BASE DE DADOS

  Cada instância de {obj_raiz.Classe} é o espelho na memória de uma
  linha em uma das tabelas da base SQL em disco. Apenas algumas dessas
  linhas estarão representadas também na memória por objetos da
  subclasse correspondente.
  
  O parâmetro {tabela} nas funções abaixo é um objeto de tipo
  {db_obj_tabela.Classe} que contém informações sobre a tabela 
  em disco, como o nome, a especificação das colunas, a letra
  prefixo dos identificadores, e o cache de linhas lidas na memória. 

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo da subclasse ("U"-, "V-", etc.), convertido para
  inteiro. Além disso, cada linha tem uma coluna da tabela (um campo)
  para cada um dos atributos que ocorre no dicionário {.atrs} da
  subclasse. (menos o identificador).  
  
  Para alguns campos, haverá uma conversão automática entre valor do campo
  na memória e o valor armazenado na tabela. Por exmplo, um campo {bool}
  na memória é gravado como 'NUMERIC' na tabela, com valores 0 ou 1.
  Campos de um objeto cujo valor é outro objeto são substituídos por 
  seus identificadores.
  """
  pass

def cria(atrs, tabela, def_obj_mem):
  """
  Cria um novo objeto da classe {obj_raiz.Classe} com atributos {atrs}
  e acrescenta-o à tabela SQL representada pelo objeto {tabela}.
  
  O atributo {tabela.classe} deve ser uma subclasse de
  {obj_raiz.Classe}. O atributo {tabela.colunas} deve ser compatível com
  o atributo {.atrs} de objetos dessa classe. O identificador {id} do
  objeto criado será "{L}-{NNNNNNNN}" onde {L} é {tabela.letra} e
  {NNNNNNNN} é o índice da linha na tabela, formatada em 8 dígitos
  decimais. 
  
  A função também armazena o objeto criado no cache de {tabela}.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro.
  """
  return obj_raiz_IMP.cria(atrs, tabela, def_obj_mem)

def muda_atributos(obj, mods, tabela, def_obj_mem):
  """Modifica alguns atributos do objeto {obj} da classe {obj_raiz.Classe},
  registrando as alterações na tabela especificada da base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do objeto (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  obj_raiz_IMP.muda_atributos(obj, mods, tabela, def_obj_mem)

def obtem_identificador(obj):
  """Devolve o identificador '{L}-{NNNNNNNN}' do objeto."""
  return obj_raiz_IMP.obtem_identificador(obj)

def obtem_atributos(obj):
  """Retorna um dicionário Python que é uma cópia dos atributos do objeto,
  exceto identificador."""
  return obj_raiz_IMP.obtem_atributos(obj)

def obtem_atributo(obj, chave):
  """Retorna o valor do atributo de {obj} com a chave {chave}.
  Não serve para obter o identificador."""
  return obj_raiz_IMP.obtem_atributo(obj, chave)

def busca_por_identificador(id_obj, tabela, def_obj_mem):
  """Localiza um objeto com identificador {id_obj} (uma string da forma
  "{X}-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_raiz.Classe}.
  Se {id_obj} é {None} ou tal objeto não existe, devolve {None}."""
  return obj_raiz_IMP.busca_por_identificador(id_obj, tabela, def_obj_mem)

def busca_por_campo(chave, val, unico, tabela):
  """Procura objetos cujo atributo {chave} tem valor {val}. 
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto (NÃO o objeto, NÃO uma lista) se 
  encontrar apenas um. Em qualquer outro caso, aborta o programa com erro."""
  return obj_raiz_IMP.busca_por_campo(chave, val, unico, tabela)

def busca_por_campos(args, unico, tabela):
  """Procura objetos com atributos {args}, na memória ou na base de dados.
  
  Especificamente, para todo par {ch: val} em {args}, exige que o valor
  do atributo {ch} do objeto seja {val}. 
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro."""
  return obj_raiz_IMP.busca_por_campos(args, unico, tabela)

def busca_por_semelhanca(args, unico, tabela):
  """Similar a {busca_por_campos}, mas aceita valores na tabela semelhantes 
  aos valores em {args}, em vez de iguais a eles.  Vide
  {db_obj_tabela.busca_por_semelhanca}."""
  # !!! Deveria ter especificação exato/aproximado para cada campo. !!!
  # !!! Corrigir clientes !!!
  return obj_raiz_IMP.busca_por_semelhanca(args, unico, tabela)
  
def ultimo_identificador(tabela):
  """Retorna o identificador do último objeto na tabela {tabela},
  no formato "{letra_tb}-{NNNNNNNN}" onde {NNNNNNNN} é o 
  número de objetos atualmente armazenados nessa tabela.
  Em particular, se a tabela estiver vazia, retorna "V-00000000"."""
  return obj_raiz_IMP.ultimo_identificador(tabela)

# FUNÇÕES PARA DEPURAÇÃO

def verifica_criacao(obj, tipo, id_obj, atrs, ignore, tabela, def_obj_mem):
  """Faz testes de consistência básicos de um objeto {obj} de classe {tipo}, 
  que deve ser uma sublcasse de {Classe}.  Tipicamente usada para 
  testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(obj)} devolve
  o identificador esperado {id_obj}, {obtem_atributos(obj)} devolve 
  os atributos esperados {atrs}, e {busca_por_identificador(id_obj)}
  devolve o próprio {obj}.  
  
  O parâmetro {ignore} deve ser {None}, ou uma lista de chaves
  de campos que não estão em {atrs} mas podem estar presentes no 
  objeto {obj}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_raiz_IMP.verifica_criacao(obj, tipo, id_obj, atrs, ignore, tabela, def_obj_mem)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  obj_raiz_IMP.liga_diagnosticos(val)

