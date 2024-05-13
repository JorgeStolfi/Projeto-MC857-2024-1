import util_titulo_de_video_IMP
 
def valida(chave, val, nulo_ok, padrao_ok):
  """
  Verifica a validade de um string {val} que vai ser o atributo 'titulo' 
  de um vídeo, ou o argumento de uma busca por esse atributo.
  
  Se {nulo_ok} for {True}, o parâmetro {val} pode ser {None}. Se
  {padrao_ok} for {True}, {val} pode ser um string que começa e termina
  '*', significando que é um padrão para usar em buscas
  por semelhança. Em qualquer caso, {val} pode ser um string
  que satisfaz as seguintes condições:
  
    * (G) Usa apenas caracters visíveis ASCII [!-~], brancos, e as 
      letras acentuadas do conjunto ISO-Latin-1
      !!! Acrescentar alguns dos símbolos do ISO-Latin-1 !!!

    * (G) Deve ter no máximo 60 caracteres.
    
    * (E) Deve ter no mínimo 10 caracteres.
    * (E) Deve começar com uma letra maiúscula.
    * (E) Não pode terminar com branco.

    * (G) Não pode ter dois ou mais brancos seguidos.

  Se {val} for um padrão "*...*", a cadeia menos os dois "*" deve satisfazer
  as regras acima, exceto que as regras marcadas com (E) são substituídas
  por 
  
    * (P) Deve ter pelo menos 3 caracteres.
    
  Caso {val} seja considerado válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_titulo_de_video_IMP.valida(chave, val, nulo_ok, padrao_ok)
