
import util_texto_de_comentario_IMP
 
def valida(chave, val, nulo_ok):
  """
  Verifica a validade de um string {val} que vai ser o atributo 'texto' 
  de um comentário.
  
  Se {nulo_ok} for {True}, o parâmetro {val} pode ser {None}. 
  Em qualquer caso, {val} pode ser um string
  que satisfaz as seguintes condições:
  
    * Usa apenas caracters visíveis ASCII [!-~], brancos, as 
      letras acentuadas do conjunto ISO-Latin-1, e mudanças de linha "\n"
      !!! Expandir para Unicode bem-comportado, emojis, etc. !!!

    * Deve ter no máximo 1003 caracteres.
    * Deve ter no mínimo 1 caracter.
    
    * Não pode começar com branco ou newline.
    * Não pode terminar com branco ou newline.
  
  Caso {val} seja considerado válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_texto_de_comentario_IMP.valida(chave, val, nulo_ok)
