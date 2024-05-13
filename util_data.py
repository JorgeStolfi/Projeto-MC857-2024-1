import util_data_IMP

def valida(chave, val, nulo_ok):
  """Verifica se {val} é uma data válida para o sistema.
  
  Exige que {val} seja um string estritamente no formato ISO 
  "{yyyy}-{mm}-{dd} {HH}:{MM}:{SS} UTC". O campo {yyyy}
  deve ter quatro dígitos começando com "19" ou "20". 
  Os demais campos devem ter exatamente dois algarismos.  O mes 
  {mm} pode ser de "01" a "12", o dia {dd} pode ser de "01" a "31",
  a hora {HH} de "00" a "23", o minuto {MM} de "01" a "59",
  e o segundo {SS} de "01" a "60" [sic].
  
  Caso {val} seja uma data válida, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_data_IMP.valida(chave, val, nulo_ok)

