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
  nome de usuário, com no mínimo 6 e no máximo 60 caracteres.
  São permitidas letras acentuadas, brancos, hífen, ponto, e apóstrofe."""
  return util_valida_campo_IMP.nome_de_usuario(rotulo, val, nulo_ok)
  
def senha(rotulo, val):
  """ALUNO: Exige que o paramêtro {val} seja uma string e contenha no mínimo 8 e 
  no máximo 16 caracteres, no minimo uma letra maúscula, uma minúscula, um 
  número e um caracter especial.
  
  MAIN: A senha deve ser uma cadeia de caracteres visíveis do conjunto ASCII,
  incluindo letras ou dígitos [A-Za-z0-9] e alguns caracteres especiais.  
  Deve ter pelo menos um caracter que não é letra ou dígito, no mínimo
  8 e no máximo 14 caracters."""
  return util_valida_campo_IMP.senha(rotulo, val)

def email(rotulo, val, nulo_ok):
  """ALUNO: Exige que o parâmetro {val} seja uma string e valida se {val} está contido no contexto
  De um email padrão, ou seja, inicio@dominio.domSuperior onde inicio permite letras maiúsculas ou minusculas, digitos e caracteres especiais. 
  Dominio permite letras maiusculas, minusculas, numeros, . e _. domSuperior permite 
  letras maiusculas ou minúsculas e deve conter no minimo 2 caracteres.
  MAIN: Um endereço de email deve ser "{usuario}@{host}" onde {usuario} 
  e {host} não podem ser vazios e devem ter só letras, dígitos, hifens, underscoeres, e pontos. 
  O {host} deve ter pelo menos um ponto. O comprimento total arbitrariamente limitado
  a 80 caracteres."""
  return util_valida_campo_IMP.email(rotulo, val, nulo_ok)

def data(rotulo, val, nulo_ok):
  """Toda data no sistema deve ser um string to formato ISO 
  "{yyyy}-{mm}-{dd} {HH}:{MM}:{SS} UTC". O campo {yyyy}
  deve ter quatro dígitos começando com "19" ou "20". 
  Os demais campos devem ter exatamente dois algarismos.  O mes 
  {mm} pode ser de "01" a "12", o dia {dd} pode ser de "01" a "31",
  a hora {HH} de "00" a "23", o minuto {MM} de "01" a "59",
  e o segundo {SS} de "01" a "60" [sic]."""
  return util_valida_campo_IMP.data(rotulo, val, nulo_ok)

def nome_de_arq_video(rotulo, val, nulo_ok):
  """O nome de um arquivo de vídeo deve ser uma cadeia não vazia de caracteres ASCII 
  contendo apenas letras, dígitos, e underscores, seguida da extensão ".mp4"."""
  return util_valida_campo_IMP.nome_de_arq_video(rotulo, val, nulo_ok)
  
  
