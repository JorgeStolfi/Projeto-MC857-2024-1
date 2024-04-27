import obj_comentario_IMP

class Classe(obj_comentario_IMP.Classe_IMP):
  """
  Um objeto desta classe representa um comentário associado a um video
  e armazena seus atributos na memória, espelhando a linha
  correspondente da tabela "comentarios" da base de dados do sistema. É
  uma subclasse de {obj_raiz.Classe}.  Um objeto desta classe é criado
  quando alguém posta um comentário a um vídeo, ou uma resposta
  a um comentário anterior. 
  
  O identificador de um comentário (vide {obtem_indentificador} é uma
  string da forma "C-{NNNNNNNN}" onde {NNNNNNNN} é o índice na tabela de
  comentários, formatado em 8 algarismos.

  Por enquanto, o dicionário de atributos de um objeto desta classe
  (vide {obtem_atributos} abaixo) contém os seguintes campos:

    'video'          {obj_video.Classe}      Vídeo ao qual o comentário se refere.
    'autor'          {obj_usuario.Classe}    Usuário que postou o comentário.
    'data'           {str}                   Data de postagem.
    'pai'            {obj_comentario.Classe} Comentário do qual este é resposta.
    'texto'          {str}                   Texto do comentário.

  Outros atributos (como censura, escore, histórico de edições, etc.)
  poderão ser acrescentados no futuro.
  
  A data de postagem deve estar no formato ISO, "yyyy-mm-dd HH:MM:SS UTC".
  Por enquanto todas as datas são referentes ao fuso universal "UTC".
   
  Nenhum destes atributos pode ser {None}, exceto 'pai'.
  
  Se o campo 'pai' não é {None}, o comentário em questão é uma
  resposta ao comentário cujo identificador é o valor de 'pai'.
  O campo 'data' deve serr estritamente maior (posterior) à data
  do 'pai', e os dois devem se referir ao mesmo vídeo. 
  
  Cada comentário tem um unico autor (usuário), um único vídeo,
  e um único comentário-pai; mas cada um destes objetos 
  pode ter vários comentários.
  
  Em todas as funções abaixo, o parâmetro {com} deve ser {None}
  ou um objeto desta classe.
  
  REPRESENTAÇÃO NA BASE DE DADOS

  Cada comentário no sistema é representado por uma linha na tabela
  "comentarios" da base SQL em disco. Apenas algumas dessas linhas são
  representadas também na memória por objetos da classe
  {obj_comentario.Classe}.

  Cada linha da tabela tem um índice inteiro (chave primária) distinto,
  que é atribuído quando a linha é criada. O índice é o identificador
  menos o prefixo "C-", convertido para inteiro. Além disso, cada linha tem
  uma coluna da tabela (um campo) para cada um dos atributos do comentário
  (menos o identificador).
  """
  pass

def inicializa_modulo(limpa):
  """Inicializa o modulo, criando a tabela "comentarios" na base de dados.
  Não retorna nenhum valor. Deve ser chamada apenas uma vez no ínicio da
  execução do servidor, depois de chamar {db_base_sql.conecta}. 
  Se o parâmetro booleano {limpa} for {True}, apaga todas as linhas da tabela
  SQL, resetando o contador em 0."""
  obj_comentario_IMP.inicializa_modulo(limpa)

def cria(atrs):
  """
  Cria um novo objeto da classe {obj_comentario.Classe}, com os
  atributos especificados pelo dicionário Python {atrs}, acrescentando-o
  à tabéla de comentários da base de dados. Atribui um identificador
  único ao comentário, derivado do seu índice na tabela.
  
  O dicionário {atrs} deve ter os atributod da {Classe} especificados
  acima, menos o campo 'data', que será a data corrente no momento da
  chamada desta função. O identificador do novo objeto será derivado do
  seu índice na tabela.
  
  Em caso de sucesso, retorna o objeto criado.  Caso contrário, 
  levanta a exceção {ErroAtrib} com uma lista de mensagens
  de erro.
  """
  return obj_comentario_IMP.cria(atrs)

def muda_atributos(com, atrs_mod):
  """
  Modifica alguns atributos do objeto {com} da classe
  {obj_comentario.Classe}, registrando as alterações na base de dados.
  Dá erro se {com} é {None}.


  O parâmetro {atrs_mod} deve ser um dicionário cujas chaves são um
  subconjunto das chaves dos atributos do comentário (excluindo o identificador).
  Os valores atuais desses atributos são substituídos pelos valores
  correspondentes em {atrs_mod}.  Os valores devem estar no formato de
  atributos na memória.
  
  Em caso de sucesso, não devolve nenhum resultado. Caso contrário,
  levanta a exceção {ErroAtrib} com uma lista de mensagens de erro.
  """
  obj_comentario_IMP.muda_atributos(com, atrs_mod)

def obtem_identificador(com):
  """Devolve o identificador 'C-{NNNNNNNN}' do comentario. Dá erro se {com} é {None}."""
  return obj_comentario_IMP.obtem_identificador(com)

def obtem_atributos(com):
  """Retorna um dicionário Python que é uma cópia dos atributos do comentário,
  exceto identificador. Dá erro se {com} é {None}."""
  return obj_comentario_IMP.obtem_atributos(com)

def obtem_atributo(com, chave):
  """Retorna o atributo do comentário {com} com a {chave} dada. 
  Equivale a {obtem_atributos(com)[chave]}. Dá erro se {com} é {None}."""
  return obj_comentario_IMP.obtem_atributo(com, chave)

def busca_por_identificador(id_com):
  """Localiza um comentario com identificador {id_com} (uma string da forma
  "C-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_comentario.Classe}.
  Se {id_com} é {None} ou tal comentário não existe, devolve {None}."""
  return obj_comentario_IMP.busca_por_identificador(id_com)

def busca_por_video(id_vid):
  """Localiza comentários associados ao video com identificador {id_vid}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o usuário não postou nenhum comentário."""
  return obj_comentario_IMP.busca_por_video(id_vid)

def busca_por_autor(id_usr):
  """Localiza comentários postados pelo usuário com identifiador {id_usr}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o usuário não postou nenhum comentário."""
  return obj_comentario_IMP.busca_por_autor(id_usr)

def busca_por_pai(id_pai):
  """Localiza comentários que são respostas ao comentário com identificador {id_pai}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o comentário não tem respostas."""
  return obj_comentario_IMP.busca_por_pai(id_pai)

def busca_por_texto(texto):
  """Localiza comentários que contém a string {texto} no campo de texto
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se nenhum comentário contém o texto."""
  return obj_comentario_IMP.busca_por_texto(texto)

def busca_por_data(data):
  """Localiza comentários postados com uma data aproximada de data {data} 
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se nenhum comentário foi postado na data."""
  return obj_comentario_IMP.busca_por_data(data)

def ultimo_identificador():
  """Devolve o identificador do último comentário inserido na tabela.
  Se ainda não houver nenhum comentário, devolve "C-00000000"."""
  return obj_comentario_IMP.ultimo_identificador()

# FUNÇÕES PARA DEPURAÇÃO

def verifica_criacao(com, id_com, atrs):
  """Faz testes de consistência básicos de um objeto {com} de classe 
  {obj_comentario.Classe}.  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(com)} devolve
  o identificador esperado {id_com}, {obtem_atributos(com)} devolve 
  os atributos esperados {atrs}, e {busca_por_identificador(id_com)}
  devolve o próprio {com}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_comentario_IMP.verifica_criacao(com, id_com, atrs)

def cria_testes(verb):
  """Limpa a tabela de comentários com {inicializa(True)}, e cria pelo menos três comentários
  para fins de teste, incluindo-os na tabela.  Não devolve nenhum resultado.
  
  Deve ser chamada apenas uma vez no ínicio da execução do programa, 
  depois de chamar {db_base_sql.conecta}.
  
  Se {verb} for {True}, escreve uma linha em {sys.stderr}
  para cada objeto criado.""" 
  obj_comentario_IMP.cria_testes(verb)

def liga_diagnosticos(val):
  """Habilita (se {val=True}) ou desabilita (se {val=False}) a
  impressão em {sys.stderr} de mensagens de diagnóstico pelas 
  funções deste módulo."""
  obj_comentario_IMP.liga_diagnosticos(val)
