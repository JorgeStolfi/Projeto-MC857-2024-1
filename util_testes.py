# Funções úteis para testes.

import util_testes_IMP
  
# DEPURAÇÂO DE FUNÇÕES QUE GERAM HTML

def escreve_resultado_html(modulo, funcao, rot_teste, ht_res, frag, pretty):
  """Escreve o string {ht_res} no arquivo "testes/saida/{modulo.__name__}.{funcao.__name__}.{rot_teste}.html".
  Se {modulo} e/ou {funcão} forem {None}, o campo correspondente será omitido.
  
  Supõe que {ht_res} é o resultado de testar uma ou mais funções do {modulo}
  especificado. 
  
  Se {ht_res} é {None}, a função grava uma página que 
  diz {None} em cor e fonte especial.
  
  Se {ht_res} não é {None}, e o parâmetro {frag} é {True}, o parâmetro
  {ht_res} pode ser um string HTML5, ou uma lista ou tupla de strings
  HTML5, possivelmente vazia. Neste caso, a função acrescenta comandos
  de preâmbulo e postâmbulo, includindo "<html><body>" e
  "</body></html>", que transformam {ht_res} em uma página completa que
  pode ser visualizada com browser. Se {ht_res} é uma lista ou tupla,
  cada elemento da mesma é mostrado como uma linha dessa página.
  
  Se {ht_res} não é {None}, e {frag} é {False}, a função supõe que
  {ht_res} é uma página completa, e escreve a mesma como está.
  
  O parâmetro {modulo}, se não for {None}, deve ser um módulo do site, importado,
  (como {obj_usuario}); e não um string (como "obj_usuario").
  A {funcao} não pode ser {None}.
  
  Em qualquer caso, cada página ou fragmento em {ht_res}
  deve ter seus os marcadores HTML corretamente balanceados 
  (como "<i>..</i>", "<table>...</table>", etc.).

  Em qualquer caso, se {pretty} for {True}, a função passa a página
  resultante por um filtro ({bsoup(ht_res).prettify()}) que o reformata
  de modo a facilitar sua depuração por inspeção direta do código HTML5
  com editor de texto ou com a opção "view source" do browser. Porém,
  note que esse filtro pode inserir espaços em branco em textos; por
  exemplo, "A<b>C</b>D" vira "A B C" no browser em vez de "ABC"."""
  util_testes_IMP.escreve_resultado_html(modulo, funcao, rot_teste, ht_res, frag, pretty)

def testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args):
  """
  Chama a {funcao} com argumentos {(*args)}.
  Compara resultado com {res_esp}. Se bater, escreve "CONFERE!" em {stderr} e devolve
  {True}, senão escreve "** " seguido de mensagem de erro, e devolve {False}.
  
  Também escreve o resultado no arquivo "testes/saida/{modulo}.{funcao}.{rot_teste}.html"
  Veja {escreve_resultado_html}.  
  
  Se o resultado for um string, ou lista de strings, o booleano {html} diz se 
  esses strings estão em HTML ({True}) ou não ({False}).  Nesse caso, os 
  booleanos {frag} e {pretty} tem o mesmo sentido que
  em {escreve_resultado_html}. Se {html} for {False}, estes parãmetros são
  ignorados e o resultado é convertido pata HTML na marra.
  
  Se {res_esp} for valor vazio ({None}, {[]}, {()}, {{}} ou {""}), exige
  que o resultado da {funcao} seja igual a {res_esp}. O parâmetro
  {res_esp} pode ser um tipo, como {str} ou {list}, caso em que só é
  verificado se o resultado não é vazio e for desse tipo. Se {res_esp}
  for "*ANY*", qualquer resultado é aceito. Senão, se {res_esp} for uma
  tupla, lista, ou dict, o resultado deve ser do mesmo tipo, e cada
  elemento/campo é verificado do mesmo modo, recursivamente. 
  
  Em todos os casos acima, espera-se que a {funcao} retorne normalmene.
  Porém, se o parâmetro {res_esp} for "AssertionError" ou "ErroAtrib", 
  espera-se que a {funcao} levante esses erros.
  """
  return util_testes_IMP.testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args)

def testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args):
  """Equivale a {testa_funcao} com o parâmetro {html} fixo em {True}."""
  return util_testes_IMP.testa_funcao_que_gera_html(modulo, funcao, rot_teste, res_esp, frag, pretty, *args)

# FORMATAÇÃO DE DADOS PARA DEPURAÇÃO

def formata_valor(dado, html, max_len):
  """Esta função de depuração recebe um valor simples ou estruturado {dado} e devolve um
  string que mostra esses velor em formato relativamente
  legível.  O {dado} é primeiro processado com {trunca_tamanho(dado,max_len)}.
  
  O resultado é basicamente JSON com quebras de linha e indentação.
  
  Se o booleano {html} é {False}, o resultado é um string que pode
  ser impresso em {stderr}.  Se {html} é {True}, o resultado 
  usa formatação HTML, que pode ser incluído numa página HTML."""
  return util_testes_IMP.formata_valor(dado, html, max_len)

def unico_elemento(lista):
  """O parâmetro {lista} deve ser {None}  ou uma lista ou tupla.
  Se {lista} for {None} ou vazia, devolve {None}.  Se
  {lista} tiver um único elemento, devolve esse elemento. 
  Em todos os outros casos, levanta a exceção {ErroAtrib}
  com uma mensagem explicando o erro."""
  return util_testes_IMP.unico_elemento(lista)

def trunca_tamanho(dado, max_len):
  """Percorre recursivamente os campos de {dado}, truncando campos 
  {str} que tem mais de {max_len} caracteres,
  e campos {list} ou {tuple} que tem mais de {max_len//10} elementos.
  Também converte elementos {bytes} para um {str} curto indicativo.
  Retorna uma cópia de {dado} com zero ou mais campos truncados."""
  return util_testes_IMP.trunca_tamanho(dado, max_len)
