# Este módulo define as tabelas da base de dados da loja e as 
# classes de objetos que representam linhas dessas tabelas na memória.

# Implementação desta interface:
import db_tabelas_do_sistema_IMP

def inicializa_todas(limpa):
  """Inicializa as tabelas da base de dados para os objetos
  das classes {obj_usuario.Classe} e {obj_sessao.Classe},
  criando-as se necessário, e criando os caches 
  de objetos na memória.   Nao retorna nenhum resultado.
  
  Se parâmetro booleano {limpa} for {True}, também apaga todas as
  entradas das tabelas no disco e reinicializa os contadores de linhas
  para 0.
  
  Esta função deve ser chamada apenas uma vez em cada execução do
  servidor, depois de executar {basesql.conecta(...)}."""
  db_tabelas_do_sistema_IMP.inicializa_todas(limpa)

def identificador_para_objeto(id_obj):
  """Converte um identificador de objeto {id_obj} ("U-{NNNNNNNN}", "S-{NNNNNNNN}" etc.)
  para o objeto correspondente, com {{modulo}.busca_por_identificador}
  onde {modulo} é o módulo indicado pela letra ({usuario}, {sessao}, etc.)."""
  return db_tabelas_do_sistema_IMP.identificador_para_objeto(id_obj)

def cria_todos_os_testes(verb):
  """Limpa todas as tabelas com {inicializa_todas(True)}, e cria três 
  objetos de cada classe, incluindo-os nas respectivas tabelas.  
  Se {verb} for {True}, escreve uma linha em {sys.stderr} para
  cada objeto criado. Não devolve nenhum resultado.""" 
  db_tabelas_do_sistema_IMP.cria_todos_os_testes(False)
