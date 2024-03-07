# Funções úteis para testes.

import util_testes_IMP

# MENSAGENS DE DIAGNÓSTICO

def erro_prog(mens):
  """Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o arquivo e linha da chamada
  e a palavra " ** erro: ", e aborta a execução com {assert False}.
  
  Esta função deve ser chamada apenas para informar erros do programa. 
  Erros em dados fornecidos pelo usuário (cliente ou administrador) devem ser enviados ao
  browser na forma de uma página HTML com a mensagem de erro (vide {html_pag_mensagem_de_erro.gera})."""
  util_testes_IMP.erro_prog(mens)

def aviso_prog(mens, grave):
  """Escreve a mensagem {mens} na saída {sys.stderr}, prefixada com o arquivo e linha da chamada.
  Se {grave} for {True}, insere também a palavra " ** erro: ", senão insere palavra " !! aviso: ".
  Não aborta a execução e não retorna nada.  
  
  Esta função deve ser chamada apenas para depuração do programa. 
  Avisos destinados ao usuário (cliente ou administrador) devem ser enviados ao browser na forma
  de uma página HTML com a mensagem de erro (vide {html_pag_mensagem_de_erro.gera})."""
  util_testes_IMP.aviso_prog(mens, grave)

def mostra(ind,mens):
  """Escreve a mensagem {mens} na saída {sys.stderr}, indentada de {ind} colunas.
  Útil para imprimir variáveis internas no diagnóstico de programas"""
  util_testes_IMP.mostra(ind,mens)
  
# VERIFICAÇÃO DE FUNÇÕES QUE GERAM HTML

def testa_modulo_html(modulo, rotulo, res, frag, pretty):
  """Escreve o string {res} em "testes/saida/{modulo}.{rotulo}.html".
  Supõe que {res} é um string HTML5 que é o resultado de 
  testar uma ou mais funções do {modulo} especificado.
  
  Supõe que {res} é uma página (se {frag=False}) ou fragmento (se {frag=True}
  de HTML.  Neste segundo caso, acrescenta comandos de preâmbulo e
  postâmbulo, includindo "<html><body>" e "</body></html>",
  que transformam o fragmento em uma página completa que pode ser
  visualizada com browser.
  
  Se {pretty} for {True}, passa o resultado por um filtro
  ({bsoup(res).prettify()}) que o reformata de modo a facilitar sua
  depuração por inspeção direta do código HTML5 com editor de texto.
  Porém, esse filtro pode inserir espaços em branco em textos, por
  exemplo em "A<b>C</b>D" vira "A B C" no browser em vez de "ABC"."""
  util_testes_IMP.testa_modulo_html(modulo, rotulo, res, frag, pretty)

def testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args):
  """Chama a função {funcao} do módulo {modulo} com os argumentos {*args}.
  A funçao deve devolver um string que é um fragmento HTML, ou 
  uma lista ou tupla de tais fragmentos.  (No segundo caso, {frag} 
  deve ser {True}).
  
  Grava o resultado {res} da chamada em "testes/saida/{modulo}.{funcao}.{rotulo}.html",
  usando {testa_modulo_html}."""
  util_testes_IMP.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)

# FORMATAÇÃO DE DADOS PARA DIAGNÓSTICO

def formata_dict(dados):
  """Esta função de depuração recebe um dicionário {dados}
  e devolve um string é um fragmento HTML5 que mostra esses
  dados em formato relativamente legível (JSON com quebras de
  linha e indentação)."""
  return util_testes_IMP.formata_dict(dados)
