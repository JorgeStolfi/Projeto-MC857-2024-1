# Funções úteis para testes.

import util_testes_IMP
  
# DEPURAÇÂO DE FUNÇÕES QUE GERAM HTML

def escreve_resultado_html(modulo, rot_teste, ht_res, frag, pretty):
  """Escreve o string {ht_res} no arquivo "testes/saida/{modulo}.{rot_teste}.html". 
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
  
  O parâmetro {modulo} deve ser um módulo do site, importado,
  (como {obj_usuario}); e não um string (como "obj_usuario").
  
  Em qualquer caso, cada página ou fragmento em {ht_res}
  deve ter seus os marcadores HTML corretamente balanceados 
  (como "<i>..</i>", "<table>...</table>", etc.).

  Em qualquer caso, se {pretty} for {True}, a função passa a página
  resultante por um filtro ({bsoup(ht_res).prettify()}) que o reformata
  de modo a facilitar sua depuração por inspeção direta do código HTML5
  com editor de texto ou com a opção "view source" do browser. Porém,
  note que esse filtro pode inserir espaços em branco em textos; por
  exemplo, "A<b>C</b>D" vira "A B C" no browser em vez de "ABC"."""
  util_testes_IMP.escreve_resultado_html(modulo, rot_teste, ht_res, frag, pretty)

def testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args):
  """Chama a função {funcao} do módulo {modulo} com os argumentos {*args}.
  O resultado {res} da {funcao} deve ser {None}, ou um string que é uma página completa
  (e neste caso {frag} deve ser {False}), ou um fragmento HTML, ou uma lista
  ou tupla de fragmentos de HTML (e nestes dois casos {frag} deve ser
  {True}).  
  
  Esta rotina grava o resultado {res} da chamada em
  "testes/saida/{modulo}.{funcao}.{rot_teste}.html", usando
  {escreve_resultado_html}.
  
  Se {frag} é {False}, o resultado {res} de {funcao} também
  também pode ser uma lista de dois elementos, onde o
  primeiro é uma página completa ou {None} e o segundo é um objeto de
  sessão ({obj_sessao.Classe}). Esta segunda opção permite testar
  funções como {comando_fazer_login.processa}."""
  util_testes_IMP.testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args)

# FORMATAÇÃO DE DADOS PARA DEPURAÇÃO

def formata_dict(dados):
  """Esta função de depuração recebe um dicionário {dados} e devolve um
  fragmento HTML5 que mostra esses dados em formato relativamente
  legível (JSON com quebras de linha e indentação)."""
  return util_testes_IMP.formata_dict(dados)

def unico_elemento(lista):
  """O parâmetro {lista} deve ser {None}  ou uma lista ou tupla.
  Se {lista} for {None} ou vazia, devolve {None}.  Se
  {lista} tiver um único elemento, devolve esse elemento. 
  Em todos os outros casos, levanta a exceção {ErroAtrib}
  com uma mensagem explicando o erro."""
  return util_testes_IMP.unico_elemento(lista)
