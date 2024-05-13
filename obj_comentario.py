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

def obtem_autor(com):
  """Retorna o atributo 'autor' do comentário {com}. 
  Equivale a {obtem_atributos(com)['autor']}. Dá erro se {com} é {None}."""
  return obj_comentario_IMP.obtem_autor(com)

def obtem_objeto(com_id):
  """Localiza um comentario com identificador {com_id} (uma string da forma
  "C-{NNNNNNNN}"), e devolve o mesmo na forma de um objeto da classe {obj_comentario.Classe}.
  Se {com_id} é {None} ou tal comentário não existe, devolve {None}."""
  return obj_comentario_IMP.obtem_objeto(com_id)

def busca_por_video(vid_id, sem_pai):
  """
  Se {sem_pai} é {False}, localiza todos os comentários associados ao
  video com identificador {vid_id} e devolve o uma lista com os
  identificadores desses comentários (não os objetos).
  
  Se o booleano {sem_pai} for {True}, retorna apenas os identificadores
  dos comentários desse vídeo que tem 'pai' {None} (ou seja, são
  respostas diretas ao vídeo).
  
  O resultado será {None} se não há comentários com essas condições.
  """
  return obj_comentario_IMP.busca_por_video(vid_id, sem_pai)

def busca_por_pai(pai_id):
  """Localiza comentários que são respostas ao comentário com identificador {pai_id}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o comentário não tem respostas."""
  return obj_comentario_IMP.busca_por_pai(pai_id)

def busca_por_autor(usr_id):
  """Localiza comentários postados pelo usuário com identifiador {usr_id}
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se o usuário não postou nenhum comentário."""
  return obj_comentario_IMP.busca_por_autor(usr_id)

def busca_por_texto(texto):
  """Localiza comentários que contém a string {texto} no campo de texto
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se nenhum comentário contém o texto."""
  return obj_comentario_IMP.busca_por_texto(texto)

def busca_por_data(data_ini, data_ter):
  """Localiza comentários postados em um intervalo entre os dois anos, inclusive 
  e devolve o uma lista com os identificadores desses comentários (não os objetos);
  ou {None} se nenhum comentário foi postado no intervalo de data."""
  return obj_comentario_IMP.busca_por_data(data_ini, data_ter)

def busca_por_campos(args):
  """
  Permite buscar por múltiplos campos de um comentário, onde o argumento {args}
  representa um dicionário no formato {chave, valor}
  """
  return obj_comentario_IMP.busca_por_campos(args)

def obtem_conversa(raizes, max_coms, max_nivel):
  """
  "Determina toda a floresta de comentarios de um vídeo ou a árvore de respostas
  de um comentário que está pendurada nas {raizes} dadas.
  
  O parâmetro {raizes} deve ser uma lista, possivelmente vazia,
  de identificadores de comentários.
  
  O resultado da função uma floresta de comentários: uma lista,
  possivelmente vazia, cada elemento da qual é uma árvore de
  comentários. Uma árvore de comentários {arv} é uma lista cujo primeiro
  elemento {arv[0]} é um identificador de comentário (a raiz), sendo o
  restante dessa lista {arv[1:]} uma floresta cujas raízes são respostas
  ao comentário {raiz}.
  
  As raízes das árvores da floresta {flor} devolvida pela função são os comentários
  cujos identificadores estão na lista {raizes}.
  """
  return obj_comentario_IMP.obtem_conversa(raizes, max_coms, max_nivel)

def ultimo_identificador():
  """Devolve o identificador do último comentário inserido na tabela.
  Se ainda não houver nenhum comentário, devolve "C-00000000"."""
  return obj_comentario_IMP.ultimo_identificador()

# FUNÇÕES PARA DEPURAÇÃO

def verifica_criacao(com, com_id, atrs):
  """Faz testes de consistência básicos de um objeto {com} de classe 
  {obj_comentario.Classe}.  Tipicamente usada para testar a função {cria}
  
  Especificamente, testa se {obtem_identificador(com)} devolve
  o identificador esperado {com_id}, {obtem_atributos(com)} devolve 
  os atributos esperados {atrs}, e {obtem_objeto(com_id)}
  devolve o próprio {com}.
  
  Devolve {True} se os testes deram certo, {False} caso contrário. Também
  imprme diagnósticos em {sys.stderr}."""
  return obj_comentario_IMP.verifica_criacao(com, com_id, atrs)

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
