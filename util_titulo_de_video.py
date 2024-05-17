import util_titulo_de_video_IMP
 
def valida(chave, val, nulo_ok):
  """
  Verifica a validade de um string {val} que vai ser o atributo 'titulo' 
  de um vídeo.
  
  Se {nulo_ok} for {True}, o parâmetro {val} pode ser {None}.
  Em qualquer caso, {val} pode ser um string que satisfaz as seguintes condições:
  
    * Usa apenas caracters visíveis ASCII [!-~], brancos, e as 
      letras acentuadas do conjunto ISO-Latin-1
      !!! Acrescentar alguns dos símbolos do ISO-Latin-1 !!!

    * Deve ter no máximo 60 caracteres.
    * Deve ter no mínimo 10 caracteres.
    * Deve começar com uma letra maiúscula.
    * Não pode terminar com branco.
    * Não pode ter dois ou mais brancos seguidos.
    
  Caso {val} seja considerado válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado para montar as mensagens de erro."""
  return util_titulo_de_video_IMP.valida(chave, val, nulo_ok)
