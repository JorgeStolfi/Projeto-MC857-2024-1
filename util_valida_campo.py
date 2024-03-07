# Este módulo define funções para verificar a validade de dados digitados
# pelo usuário em diversos formulários.

# Cada função abaixo verifica se o parâmetro {val}
# satisfaz certas condições. Em caso afirmativo,
# a função devolve uma lista vazia.  Senão devolve uma lista de 
# uma ou mais mensagens de erro (strings).  O parâmetro 
# {rotulo} é usado para montar as mensagens de erro.

# O parâmetro booleano {nulo_ok} diz se {None} deve ser considerado
# um valor válido de {val} (se {True}) ou não (se {False}).

import util_valida_campo_IMP

class ErroAtrib(Exception):
  pass

def booleano(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um booleano."""
  return util_valida_campo_IMP.booleano(rotulo, val, nulo_ok)

def identificador(rotulo, val, letra, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  identificador, no formato "{L}-{NNNNNNNN} onde {L} é a {letra}
  dada e {NNNNNNNN} são 8 dígitos decimais.  Se {letra} for {None},
  aceita qualquer letra maiúscula."""
  return util_valida_campo_IMP.identificador(rotulo, val, letra, nulo_ok) 

def nome_de_usuario(rotulo, val, nulo_ok):
  """Exige que o parâmetro {val} seja um string com aparência de
  nome de usuário, com no mínimo 10 e no máximo 60 caracteres.
  São permitidas letras acentuadas, brancos, hífen, ponto, e apóstrofe."""
  return util_valida_campo_IMP.nome_de_usuario(rotulo, val, nulo_ok)
  
def senha(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return util_valida_campo_IMP.senha(rotulo, val, nulo_ok)

def email(rotulo, val, nulo_ok):
  """ !!! documentar !!! """
  return util_valida_campo_IMP.email(rotulo, val, nulo_ok)

# !!! A completar !!!
