import obj_usuario_IMP

class Classe(obj_usuario_IMP.Classe_IMP):
  """
  Um objeto desta classe representa um usuário do sistema
  (administrador ou comum) e armazena seus atributos na memória,
  espelhando a linha correspondente da tabela "usuarios" da base de
  dados do sistema. É uma subclasse de {obj_raiz.Classe}.
  
  O identificador de um usuário (vide {obtem_indentificador} abaixo) é
  uma string da forma "U-{NNNNNNNN}" onde {NNNNNNNN} é o índice na
  tabela de usuários, formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  (vide {obtem_atributos} abaixo) contém os seguintes campos:

    'nome'           {str}     Nome completo do usuário.
    'email'          {str}     Email para identificacao no login.
    'senha'          {str}     Senha do usuário.
    'administrador'  {bool}    {True} sse o usuário é administrador. 
   
  Outros atributos (CPF, vídeos, preferências, etc.) poderão ser
  acrescentados no futuro. 
  
  Nenhum destes atributos pode ser {None}.
  
  A qualquer momento, não pode haver dois usuários no sistema com mesmo email.
  
  Em todas as funções abaixo, o parâmetro {usr} deve ser {None}
  ou um objeto desta classe.
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada usuário do sistema -- comum ou administrador, ativo ou bloqueado
  -- é representado por uma linha na tabela "usuarios" da base SQL em
  disco. Apenas algumas dessas linhas são representadas também na memória por objetos
  da classe {obj_usuario.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo "U-", convertido para inteiro.  Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do usuário
  (menos o identificador).
  """
  pass

def inicializa_modulo(limpa):
  """Inicializa o modulo, criando a tabela de usuários na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {db_base_sql.conecta}. 
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  obj_usuario_IMP.inicializa_modulo(limpa)

def cria(atrs):
  """Cria um novo objeto da classe {obj_usuario.Classe}, com os atributos especificados
  pelo dicionário Python {atrs}, acrescentando-o à tabéla de usuários da base de dados.
  
  O identificador do novo objeto será derivado do seu índice na tabela.
  
  Não pode haver outro usuário com mesmo email.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro."""
  return obj_usuario_IMP.cria(atrs)

def muda_atributos(usr, atrs_mod_mem):
  """Modifica alguns atributos do objeto {usr} da classe {obj_usuario.Classe},
  registrando as alterações na base de dados. Dá erro se {usr} é {None}.

  O parâmetro {atrs_mod} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do usuário (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {atrs_mod}.  Os valores devem estar no formato de
  atributos na memória.
  
  A função falha se o campo 'email' for alterado para um endereço
  igual ao atualmente registrado para um usuário diferente de {usr}.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro."""
  obj_usuario_IMP.muda_atributos(usr, atrs_mod_mem)

def obtem_identificador(usr):
  """Devolve o identificador 'U-{NNNNNNNN}' do usuario.
  Dá erro se {usr} é {None}."""
  return obj_usuario_IMP.obtem_identificador(usr)

def obtem_atributos(usr):
  """Retorna um dicionário Python que é uma cópia dos atributos do usuário,
  exceto identificador. Dá erro se {usr} é {None}."""
  return obj_usuario_IMP.obtem_atributos(usr)

def obtem_atributo(usr, chave):
  """Retorna o atributo do usuário {usr} com a {chave} dada. 
  Equivale a {obtem_atributos(usr)[chave]}"""
  return obj_usuario_IMP.obtem_atributo(usr, chave)

def busca_por_identificador(id_usr):
  """Localiza um usuario com identificador {id_usr} (uma string da forma
  "U-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_usuario.Classe}.
  Se {id_usr} é {None} ou tal usuário não existe, devolve {None}."""
  return obj_usuario_IMP.busca_por_identificador(id_usr)

def busca_por_email(em):
  """Localiza um usuário cujo endereço de email é {em} (um string da forma
  "{nome}@{host}") e devolve o identificador do mesmo (não o objeto);
  ou {None} se não existir tal usuário."""
  return obj_usuario_IMP.busca_por_email(em)

def busca_por_nome(nome):
  """Localiza usuarios usuário cujo nome é {nome} e devolve o uma lista
  com os identificadores dos mesmos (não os objetos);
  ou {None} se não existir nenhum usuário."""
  return obj_usuario_IMP.busca_por_nome(nome)

def busca_por_campos(args, unico):
  """Procura usuarios com atributos {args}, na memória ou na base de dados.
  
  Especificamente, para todo par {ch: val} em {args}, exige que o valor
  do atributo {ch} do objeto seja {val}. 
  
  Se {unico} for {False}, devolve uma lista, possivelmente vazia,
  com os identificadores dos objetos encontrados (NÃO os objetos).
  
  Se {unico} for {True}, devolve {None} se não encontrar nenhum objeto,
  ou o identificador de um objeto encontrado (NÃO o objeto, NÃO uma lista)  
  se houver apenas um.  Em qualquer outro case, termina o programa com erro."""
  return obj_usuario_IMP.busca_por_campos(args, unico)

def busca_por_semelhanca(args, unico):
  """Similar a {busca_por_campos}, mas aceita valores na base de dados 
  que são semelhantes aos valores em {args}, em vez de iguais a eles.  Vide
  {db_tabela_generica.busca_por_semelhanca}."""
  # !!! Deveria ter especificação exato/aproximado para cada campo. !!!
  return obj_usuario_IMP.busca_por_semelhanca(args, unico)

def ultimo_identificador():
  """Devolve o identificador do último usuário inserido na tabela.
  Se ainda não houver nenhum usuário, devolve "U-00000000"."""
  return obj_usuario_IMP.ultimo_identificador()

# UTILIDADES

def confere_e_elimina_conf_senha(args):
  """Se o campo 'senha' está em {args}, exige o campo
  'conf_senha' com mesmo valor.  Em caso de erro, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro.  Senão, remove o campo 'conf_senha' de {atrs}
  e retorna sem resultado.
  
  Esta função é útil para processar comandos de 
  cadastrar novo usuário ou alterar dados de usuário."""
  return obj_usuario_IMP.confere_e_elimina_conf_senha(args)

# FUNÇÕES PARA DEPURAÇÃO

def verifica_criacao(usr, id_usr, atrs):
  """Faz testes de consistência básicos de um objeto {usr} de classe 
  {obj_usuario.Classe}.  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(usr)} devolve
  o identificador esperado {id_usr}, {obtem_atributos(usr)} devolve 
  os atributos esperados {atrs}, e {busca_por_identificador(id_usr)}
  devolve o próprio {usr}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_usuario_IMP.verifica_criacao(usr, id_usr, atrs)

def cria_testes(verb):
  """Limpa a tabela de usuários com {inicializa(True)}, e cria pelo menos três usuários
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {db_base_sql.conecta}.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado.""" 
  obj_usuario_IMP.cria_testes(verb)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  obj_usuario_IMP.liga_diagnosticos(val)
