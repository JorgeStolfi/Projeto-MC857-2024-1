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

def obtem_objeto(id_obj, tabela, def_obj_mem):
  """Localiza um objeto com identificador {id_obj} (uma string da forma
  "{X}-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_raiz.Classe}.
  Se {id_obj} é {None} ou tal objeto não existe, devolve {None}."""
  return obj_raiz_IMP.obtem_objeto(id_obj, tabela, def_obj_mem)

def busca_por_campo(chave, val, unico, tabela):
  """Procura objetos cujo atributo {chave} tem valor {val}.  
  Equivale a {busca_por_campos({chave: val}, unico, tabela)}
  Veja essa função para os casos especiais em que {val}
  começa com "~" ou é um par {(vmin,vmax)}.
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto (NÃO o objeto, NÃO uma lista) se 
  encontrar apenas um. Em qualquer outro caso, aborta o programa com erro."""
  return obj_raiz_IMP.busca_por_campo(chave, val, unico, tabela)

def busca_por_campos(args, unico, tabela):
  """
  Semelhante a {busca_por_campo}, mas procura linhas com certos valores 
  em certos campos, especificados pelo dicionário {args}.
  
  Basicamente, para cada par {ch,val} em {args}, exige que a coluna {ch} da tabela
  tenha valor {val}.  
  
  Entretanto, se {val} começa com '~', exige apenas que o valor na
  coluna {ch} seja apenas similar ao valor especificado em {val} (menos
  o caracter '~'), segundo as regras do operador SQL "LIKE". Esse
  operador ignora as distinções minúscula/maiúscula, e entende os
  caracteres '_' e '%' em {val} como significando "qualquer caracter" e
  "qualquer cadeia de zero ou mais caracteres", respectivamente. Por
  exemplo, se {val} for "~% peiXE%", vai aceitar linhas da tabela cuja
  coluna {ch} é "Temos Peixes", "Nossa peixeira" mas não "Peixes à
  venda" nem "O Peixésimo".
  
  Se {val} for uma lista de dois elementos {(vmin, vmax)}, esta função
  exige que o valor na coluna {ch} da tabela esteja entre {vmin} e
  {vmax}, inclusive. Veja as regras em {db_obj_tabela.busca_por_campos}.
 
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro.
  """
  return obj_raiz_IMP.busca_por_campos(args, unico, tabela)
  
def converte_campo_em_padrao(args, chave):
  """
  Se {args} tem um campo {chave: val}, e {val} é um string 
  que não começa com "~", devolve uma cópia de {args} 
  onde esse campo foi substituído por {chave: "~%" + val + "%"}.
  Senão devolve {args} sem alteração.
  
  Esta função pode ser usada para forçar que uma busca pelo campo
  {chave} use forçosamente o operador SQL "LIKE", mesmo que o valor
  {val} não tenha o prefixo "~".
  """
  return obj_raiz_IMP.converte_campo_em_padrao(args, chave)

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
  os atributos esperados {atrs}, e {obtem_objeto(id_obj)}
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

