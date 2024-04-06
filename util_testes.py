# Funções úteis para testes.

import util_testes_IMP

class ErroAtrib(Exception):
  # Usada por algumas funções para sinalizar parâmetros indevidos.
  pass

# MENSAGENS DE DIAGNÓSTICO

def erro_prog(mens):
  """
  Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o
  arquivo e linha da chamada e a palavra " ** erro: ", e aborta a
  execução com {assert False}, que levanta a exceção {AssertionFailure}.
  
  Esta função causa uma mensagem de diagnóstico no shell onde roda o
  {servidor.py}, possivelmente terminando sua execução. O browser do
  usuário geralmente vai mostrar um erro de HTTP, como "404 - página não
  encontrada".
  
  Portanto, esta função deve ser chamada apenas para informar erros no
  programa. Erros nos dados fornecidos pelo usuário (comum ou
  administrador) devem ser enviados ao browser do usuário na forma de
  uma página HTML com a mensagem de erro (vide
  {html_pag_mensagem_de_erro.gera}).
  """
  util_testes_IMP.erro_prog(mens)

def aviso_prog(mens, grave):
  """
  Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o
  arquivo e linha da chamada. Se {grave} for {True}, insere também a
  palavra " ** erro: ", senão insere palavra " !! aviso: ". Não aborta a
  execução e não retorna nada.
  
  Esta função deve ser chamada apenas para depuração do programa. Avisos
  destinados ao usuário (comum ou administrador) devem ser enviados ao
  browser na forma de uma página HTML com a mensagem de erro (vide
  {html_pag_mensagem_de_erro.gera}).
  """
  util_testes_IMP.aviso_prog(mens, grave)

def mostra(ind,mens):
  """
  Escreve a mensagem {mens} na saída {sys.stderr}, indentada de {ind}
  colunas. Útil para imprimir variáveis internas no diagnóstico de
  programas
  """
  util_testes_IMP.mostra(ind,mens)
  
# DEPURAÇÂO DE FUNÇÕES QUE GERAM HTML

def escreve_resultado_html(modulo, rotulo, ht_res, frag, pretty):
  """
  Escreve o string {ht_res} no arquivo
  "testes/saida/{modulo}.{rotulo}.html". Supõe que {ht_res} é um string
  HTML5 que é o resultado de testar uma ou mais funções do {modulo}
  especificado. 
  
  O parâmetro {modulo} deve ser um módulo do site, importado,
  como {obj_usuario}; e não um string como "obj_usuario"
  
  Se o parâmetro {frag} é {False}, supõe que {ht_res} é uma página
  completa, e escreve a mesma como está.
  
  Se o parâmetro {frag} é {True}, supõe que {ht_res} é apenas um
  fragmento de HTML. Neste caso, acrescenta comandos de preâmbulo e
  postâmbulo, includindo "<html><body>" e "</body></html>", que
  transformam o fragmento em uma página completa que pode ser
  visualizada com browser. Neste caso, o parâmetro {ht_res} pode ser
  também uma lista ou tupla de strings, e cada elemento da mesma é
  mostrado como uma linha dessa página.
  
  Se {pretty} for {True}, passa a página resultante por um filtro
  ({bsoup(ht_res).prettify()}) que o reformata de modo a facilitar sua
  depuração por inspeção direta do código HTML5 com editor de texto ou
  com a opção "view source" do browser. Porém, esse filtro pode inserir
  espaços em branco em textos; por exemplo, "A<b>C</b>D" vira "A B C"
  no browser em vez de "ABC".
  """
  util_testes_IMP.escreve_resultado_html(modulo, rotulo, ht_res, frag, pretty)

def testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args):
  """
  Chama a função {funcao} do módulo {modulo} com os argumentos {*args}.
  Essa funçao deve devolver um string {res} que é uma página completa
  (e neste caso {frag} deve ser {False}), ou um fragmento HTML, ou uma lista
  ou tupla de fragmentos de HTML (e nestes casos {frag} deve ser
  {True}).  
  
  Esta rotina grava o resultado {res} da chamada em
  "testes/saida/{modulo}.{funcao}.{rotulo}.html", usando
  {escreve_resultado_html}.
  """
  util_testes_IMP.testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# FORMATAÇÃO DE DADOS PARA DEPURAÇÃO

def formata_dict(dados):
  """
  Esta função de depuração recebe um dicionário {dados} e devolve um
  fragmento HTML5 que mostra esses dados em formato relativamente
  legível (JSON com quebras de linha e indentação).
  """
  return util_testes_IMP.formata_dict(dados)
