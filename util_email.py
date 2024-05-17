import util_email_IMP

def valida(chave, val, nulo_ok):
  """
  Verifica se {val} é um endereço de email válido.
  
  Exige que {val} seja um endereço de email válido segundo 
  as especificações IETF RFC 5322 (seções 3.2.3 e 3.4.1) e RFC 5321,
  com restrições adicionais. 
  
  Especificamente, {val} deve ter a forma "{cx_postal}@{dominio}".
  
  A parte {cx_postal} deve ter pelo menos 1 e no máximo 64 caracteres
  ASCII, que podem ser [A-Za-z0-9.%'/-]. Não pode começar nem terminar
  com "." e não pode ter dois ou mais pontos seguidos (ou seja, nem
  ".Alfa", nem "Omega.", nem "Alfa..Omega" são {cx_postal}s válidos).
  
  A parte {dominio} deve ter comprimento total máximo 255, e deve
  consistir de uma ou mais partes, separadas por pontos. Cada parte deve
  ter no mínimo 1 e no máximo 63 caracteres, consistindo de letras,
  dígitos, ou hífens [A-Za-z0-9-], e não pode nem começar nem terminar
  com hífen. A última parte não pode ser só dígitos.
  
  A forma estendida "José Silva <jose@bat.com>" não é permitida.
  """
  return util_email_IMP.valida_email(chave, val, nulo_ok)
