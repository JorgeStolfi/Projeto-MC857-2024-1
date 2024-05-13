
import util_texto_de_comentario_IMP
 
def valida(chave, val, nulo_ok, padrao_ok):
  """
  Verifica a validade de um string {val} que vai ser o atributo 'texto' 
  de um comentário, ou o argumento de uma busca por esse atributo.
  
  Se {nulo_ok} for {True}, o parâmetro {val} pode ser {None}. Se
  {padrao_ok} for {True}, {val} pode ser um string que começa e termina
  '*', significando que é um padrão para usar em buscas
  por semelhança. Em qualquer caso, {val} pode ser um string
  que satisfaz as seguintes condições:
  
    * (G) Usa apenas caracters visíveis ASCII [!-~], brancos, as 
      letras acentuadas do conjunto ISO-Latin-1, e mudanças de linha "\n"
      !!! Expandir para Unicode bem-comportado, emojis, etc. !!!

    * (G) Deve ter no máximo 1003 caracteres.
    * (G) Deve ter no mínimo 1 caracter.
    
    * (E) Não pode começar com branco ou newline.
    * (E) Não pode terminar com branco ou newline.

  Se {val} for um padrão "*...*", a cadeia menos os dois "*" deve satisfazer
  apenas as regras (G) acima, mas pode violar as (E).
  
  Caso {val} seja considerado válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_texto_de_comentario_IMP.valida(chave, val, nulo_ok, padrao_ok)
