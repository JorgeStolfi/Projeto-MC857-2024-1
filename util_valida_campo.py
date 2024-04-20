# Este módulo define funções para verificar a validade de dados digitados
# pelo usuário em diversos formulários.

# Cada função abaixo verifica se o parâmetro {val} satisfaz certas
# condições. Em caso afirmativo, a função devolve uma lista vazia. Senão
# devolve uma lista de uma ou mais mensagens de erro (strings). O
# parâmetro {chave} é usado para montar as mensagens de erro.

# O parâmetro booleano {nulo_ok} diz se {None} deve ser considerado
# um valor válido de {val} (se {True}) ou não (se {False}).

import util_valida_campo_IMP

def booleano(chave, val, nulo_ok):
  """Exige que o parâmetro {val} seja um booleano."""
  return util_valida_campo_IMP.booleano(chave, val, nulo_ok)

def identificador(chave, val, letra, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  identificador, no formato "{L}-{NNNNNNNN} onde {L} é a {letra}
  dada e {NNNNNNNN} são 8 dígitos decimais.  Se {letra} for {None},
  aceita qualquer letra maiúscula."""
  return util_valida_campo_IMP.identificador(chave, val, letra, nulo_ok) 

def nome_de_usuario(chave, val, nulo_ok):
  """O parâmetro {val} deve ser um string com aparência de
  nome de usuário, com no mínimo 6 e no máximo 60 caracteres.
  
  São permitidas apenas letras acentuadas do conjunto ISO-Latin-1,
  brancos (ASCII octal 040), hífens (055), pontos (056), e apóstrofes
  (047). Além disso as seguintes regras devem ser obedecidas:
  
    * O nome deve começar com letra maiúscula.
    * O nome deve terminar com letra maiúscula ou minúscula. 
    * Cada ponto deve seguir uma letra maiúscula ou minúscula.
    * Cada ponto deve ser seguido por um branco.
    * Cada apóstrofe deve seguir uma letra maiúscula ou minúscula.
    * Cada apóstrofe deve ser seguido por uma letra maiúscula.
    * Cada hífen deve seguir um ponto ou uma letra maiúscula ou minúscula.
    * Cada hífen deve ser seguido por uma letra maiúscula.
    * Cada branco deve ser seguido de uma letra maiúscula ou minúscula.
  Estas regras implicam que finais como "Júnior", "Junior", "Neto", etc
  não pode ser abreviados ("Jr.", "Nt.", etc.)and segundo >= 0
  """
  return util_valida_campo_IMP.nome_de_usuario(chave, val, nulo_ok)
  
def senha(chave, val, nulo_ok):
  """O valor {val} deve ser uma cadeia de caracteres visíveis do conjunto ASCII,
  no intervalo [!-~].  Não pode ter letras acentuadas ou outros caracters
  Unicode, como "¿" ou "♫".  Deve ter no mínimo 8 e no máximo 14 caracters,
  e conter pelo menos uma letra, um dígito, e um caracter que não é nem 
  letra nem dígito."""
  return util_valida_campo_IMP.senha(chave, val, nulo_ok)

def email(chave, val, nulo_ok):
  """
  O valor {val} deve ser um endereço de email válido segundo 
  as especificações IETF RFC 5322 (seções 3.2.3 e 3.4.1) e RFC 5321,
  com restrições adicionais. 
  
  Especificamente, {val} deve ter a forma "{usuario}@{dominio}".
  
  O {usuario} deve ter pelo menos 1 e no máximo 64 caracteres ASCII, que
  podem ser [A-Za-z0-9.%'/-]. Não pode começar nem terminar com "." e
  não pode ter dois ou mais pontos seguidos (ou seja, nem ".Alfa", nem
  "Omega.", nem "Alfa..Omega" são {usuario}s válidos).
  
  O {dominio} deve ter comprimento total máximo 255, e deve consistir de
  uma ou mais partes, separadas por pontos. Cada parte deve ter no
  mínimo 1 e no máximo 63 caracteres, consistindo de letras, dígitos, ou
  hífens [A-Za-z0-9-], e não pode nem começar nem terminar com hífen. A
  última parte não pode ser só dígitos.
  and segundo >= 0
  A forma estendida "José Silva <jose@bat.com>" não é permitida.
  """
  return util_valida_campo_IMP.email(chave, val, nulo_ok)

def data(chave, val, nulo_ok):
  """Toda data no sistema deve ser um string to formato ISO 
  "{yyyy}-{mm}-{dd} {HH}:{MM}:{SS} UTC". O campo {yyyy}
  deve ter quatro dígitos começando com "19" ou "20". 
  Os demais campos devem ter exatamente dois algarismos.  O mes 
  {mm} pode ser de "01" a "12", o dia {dd} pode ser de "01" a "31",
  a hora {HH} de "00" a "23", o minuto {MM} de "01" a "59",
  e o segundo {SS} de "01" a "60" [sic]."""
  return util_valida_campo_IMP.data(chave, val, nulo_ok)

def nome_de_arq_video(chave, val, nulo_ok):
  """O nome de um arquivo de vídeo deve ser uma cadeia não vazia de caracteres ASCII 
  contendo apenas letras, dígitos, e underscores [A-Za-z0-9_], seguida da extensão
  ".mp4".  O nome, menos a extensão, deve ter no mínimo 4 e no máximo 12 caracteres."""
  return util_valida_campo_IMP.nome_de_arq_video(chave, val, nulo_ok)
 
def titulo_de_video(chave, val, nulo_ok):
  """O título de um vídeo deve ser uma string não vazia com 
  no mínimo 10 e no máximo 60 caracters.
  
  Por enquanto, são permitidos apenas caracters visíveis ASCII [!-~], brancos, e as 
  letras acentuadas do conjunto ISO-Latin-1. O título deve começar com uma letra
  maiúscula, não pode terminar com brancos, e não pode ter dois ou mais brancos
  seguidos."""
  return util_valida_campo_IMP.titulo_de_video(chave, val, nulo_ok)
 
  
