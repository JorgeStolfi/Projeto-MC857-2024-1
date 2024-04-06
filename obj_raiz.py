# Este módulo define a classe geral de objetos {Objeto}, 
# superclasse de objetos como {obj_usuario.Classe}, {obj_sessao.Classe}, etc.

# Implementação deste módulo e da classe {Objeto}:
import obj_raiz_IMP

class Classe(obj_raiz_IMP.Classe_IMP):
  """Um objeto genérico. Possui os seguintes campos privados:
  
    {id}     o identificador do objeto: uma string da forma "{X}-{NNNNNNNN}" onde
             {X} é uma letra que identifica o tipo do objeto
             ('U' para {obj_usuario.Classe}, 'S' para {obj_sessao.Classe}, etc)
             e {NNNNNNNN} é o índice na tabela correspondente
             da base de dados, formatado em 8 algarismos
                      
    {atrs}   um dicionário Python que contém os atributos 
             do objeto, específicos para cada classe.
  """
  pass


def cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Cria um novo objeto da classe {Objeto} com atributos {atrs}
  e acrescenta-o à tabela {nome_tb}, que deve ter as {colunas} especificadas.
  O identificador {id} será "{L}-{NNNNNNNN}" onde {L} é {letra_tb}
  e {NNNNNNNN} é o índice da linha na tabela, formatada em 8 dígitos decimais.
  Também acrescenta o objeto no {cache} na memória.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return obj_raiz_IMP.cria(atrs, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def muda_atributos(obj, mods, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Modifica alguns atributos do objeto {obj} da classe {Objeto},
  registrando as alterações na tabela especificada da base de dados.

  O parâmetro {mods} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do objeto (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {mods}.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  obj_raiz_IMP.muda_atributos(obj, mods, cache, nome_tb, letra_tb, colunas, def_obj_mem)

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

def busca_por_identificador(id_obj, cache, nome_tb, letra_tb, colunas, def_obj_mem):
  """Localiza um objeto com identificador {id_obj} (uma string da forma
  "{X}-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {Objeto}.
  Se {id_obj} é {None} ou tal objeto não existe, devolve {None}."""
  return obj_raiz_IMP.busca_por_identificador(id_obj, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def busca_por_campo(chave, val, unico, cache, nome_tb, letra_tb, colunas):
  """Procura objetos cujo atributo {chave} tem valor {val}. 
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto (NÃO o objeto, NÃO uma lista) se 
  encontrar apenas um. Em qualquer outro caso, aborta o programa com erro."""
  return obj_raiz_IMP.busca_por_campo(chave, val, unico, cache, nome_tb, letra_tb, colunas)

def busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas):
  """Procura objetos com atributos {args}, na memória ou na base de dados.
  
  Especificamente, para todo par {ch: val} em {args}, exige que o valor
  do atributo {ch} do objeto seja {val}. 
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro."""
  return obj_raiz_IMP.busca_por_campos(args, unico, cache, nome_tb, letra_tb, colunas)

def busca_por_semelhanca(nome_tb, let, chaves, valores):
  """Procura objetos cujos valores {chaves} são semelhantes a certos valores {valores}.
  A busca funciona com parte dos valores e não faz distinção de letras maiúsculas e minúsculas"""
  return obj_raiz_IMP.busca_por_semelhanca(nome_tb, let, chaves, valores)
  
def ultimo_identificador(nome_tb, letra_tb):
  """Retorna o identificador do último objeto na tabela {nome_tb},
  no formato "{letra_tb}-{NNNNNNNN}" onde {NNNNNNNN} é o 
  número de objetos atualemente armazenados nessa tabela.
  Em particular, se a tabela estiver vazia, retorna "V-00000000"."""
  return obj_raiz_IMP.ultimo_identificador(nome_tb, letra_tb)

# FUNÇÕES PARA DEPURAÇÃO

def verifica_criacao(obj, tipo, id_obj, atrs, ignore, cache, nome_tb, letra_tb, colunas, def_obj_mem):
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
  return obj_raiz_IMP.verifica_criacao(obj, tipo, id_obj, atrs, ignore, cache, nome_tb, letra_tb, colunas, def_obj_mem)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  obj_raiz_IMP.liga_diagnosticos(val)

