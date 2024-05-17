import util_nome_de_usuario_IMP

def valida(chave, val, nulo_ok):
  """
  Verifica a validade de um string {val} que vai ser o atributo 'nome' 
  de um usuário.
  
  O parâmetro {val} pode ser {None} desde que {nulo_ok} seja {None}.
  Se não for {one}, deve ser um string que satisfaz as condições abaixo;.

    * Deve ter no nínimo 10 caracteres.
    * Deve ter no máximo 60 caracteres.
  
    * Deve usar apenas as letras acentuadas do conjunto ISO-Latin-1,
      mais brancos (ASCII octal 040), hífens (055), pontos (056) e
      apóstrofes (047).
    * Deve começar com letra maiúscula.
    * Deve terminar com letra maiúscula ou minúscula.
    
    * Cada ponto deve seguir uma letra maiúscula ou minúscula.
    * Cada ponto deve ser seguido por um branco.
    * Cada apóstrofe deve seguir uma letra maiúscula ou minúscula.
    * Cada apóstrofe deve ser seguido por uma letra maiúscula.
    * Cada hífen deve seguir um ponto ou uma letra maiúscula ou minúscula.
    * Cada hífen deve ser seguido por uma letra maiúscula.
    * Cada branco deve ser seguido de uma letra maiúscula ou minúscula.
    
  Estas regras excluem nomes como "José M.'Souza", "Pedro L- Smith",
  "João M.", "Maria Costa", etc. Em particular, elas implicam que
  qualificadores finais como "Júnior", "Junior", "Neto", etc não podem
  ser abreviados ("Jr.", "Nt.", etc.).
  
  Caso {val} seja considerado válido, a função devolve uma lista vazia. Senão
  devolve uma lista de uma ou mais mensagens de erro (strings). O
  parâmetro {chave} é usado apenas para montar as mensagens de erro.
  """
  return util_nome_de_usuario_IMP.valida(chave, val, nulo_ok)
