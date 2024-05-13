import util_nome_de_usuario_IMP

def valida(chave, val, nulo_ok, padrao_ok):
  """
  Verifica a validade de um string {val} que vai ser o atributo 'nome' 
  de um usuário, ou o argumento de uma busca por esse atributo.
  
  Se {nulo_ok} for {True}, o parâmetro {val} pode ser {None}. se
  {padrao_ok} for {True}, {val} pode ser um string que começa e termina
  terminar com '*', significando que é um padrão SQL para usar em buscas
  por semelhança. Em qualquer caso, {val} pode ser um string que
  satisfaz as condições abaixo:
  
  Se não for {None} nem um padrão "*...*", o parâmetro {val} deve 
  ter no mínimo 6 caracteres e satisfazer as seguintes condições:
  
    * (G) Deve usar apenas as letras acentuadas do conjunto ISO-Latin-1,
      mais brancos (ASCII octal 040), hífens (055), pontos (056) e
      apóstrofes (047).

    * (G) Deve ter no máximo 60 caracteres.

    * (E) Deve começar com letra maiúscula.
    * (E) Deve terminar com letra maiúscula ou minúscula.
    
    * (T) Cada ponto deve seguir uma letra maiúscula ou minúscula.
    * (T) Cada ponto deve ser seguido por um branco.
    * (T) Cada apóstrofe deve seguir uma letra maiúscula ou minúscula.
    * (T) Cada apóstrofe deve ser seguido por uma letra maiúscula.
    * (T) Cada hífen deve seguir um ponto ou uma letra maiúscula ou minúscula.
    * (T) Cada hífen deve ser seguido por uma letra maiúscula.
    * (T) Cada branco deve ser seguido de uma letra maiúscula ou minúscula.
    
  Estas regras excluem nomes como "José M.'Souza", "Pedro L- Smith",
  "João M.", "Maria Costa", etc. Em particular, elas implicam que
  qualificadores finais como "Júnior", "Junior", "Neto", etc não podem
  ser abreviados ("Jr.", "Nt.", etc.).
  
  Se {val} for um padrão "*...*", a cadeia menos os dois "*" deve ter
  pelo menos 3 caracteres, e deve ser uma subcadeia possivel de um nome
  válido. Em particular, as regras (E) não são exigidas, e as regras (T)
  são consideradas satisfeitas se o caractere anterior ou seguinte não
  existe. Por exemplo, numa busca por semelhança {val} pode ser
  "*-Gravas5", "*José P.*", "*'Hara*", "*fina *" (com branco final),
  etc.
  
  Note que a distinção entre maoúsculas e minúsculas é sempre relevante
  para a verificação das regras acima, mesmo que na busca em si ela
  venha a ser ignorada.
  
  Caso {val} seja considerado válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado apenas para montar as mensagens de erro.
  """
  return util_nome_de_usuario_IMP.valida(chave, val, nulo_ok, padrao_ok)
