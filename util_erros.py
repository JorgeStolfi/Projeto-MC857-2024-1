# Funções úteis para testes.

import util_erros_IMP

class ErroAtrib(Exception):
  # Usada por algumas funções para sinalizar parâmetros indevidos.
  pass

# MENSAGENS DE DIAGNÓSTICO

def erro_prog(mens):
  """Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o
  arquivo e linha da chamada e a palavra " ** erro fatal: ", e aborta a
  execução com {assert False}, que levanta a exceção {AssertionError}.
  
  Esta função causa uma mensagem de diagnóstico no shell onde roda o
  {servidor.py}, possivelmente terminando sua execução. O browser do
  usuário geralmente vai mostrar um erro de HTTP, como "404 - página não
  encontrada".
  
  Portanto, esta função deve ser chamada apenas para informar erros 
  de programação. Erros nos dados fornecidos pelo usuário (comum ou
  administrador) devem ser enviados ao browser do usuário na forma de
  uma página HTML com a mensagem de erro 
  (vide {html_pag_mensagem_de_erro.gera}).
  """
  util_erros_IMP.erro_prog(mens)

def aviso_prog(mens, grave):
  """
  Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o
  arquivo e linha da chamada. Se {grave} for {True}, insere também a
  palavra " ** erro: ", senão insere palavra " !! aviso: ". Não aborta a
  execução e não retorna nada.
  
  Esta função deve ser chamada apenas para depuração do programa. Avisos
  destinados ao usuário (comum ou administrador) devem ser enviados ao
  browser na forma de uma página HTML com a mensagem de erro (vide
  {html_pag_mensagem_de_erro.gera})."""
  util_erros_IMP.aviso_prog(mens, grave)

def mostra(ind,mens):
  """ Escreve a mensagem {mens} na saída {sys.stderr}, indentada de {ind}
  colunas. Útil para imprimir variáveis internas no diagnóstico de
  programas."""
  util_erros_IMP.mostra(ind,mens)
