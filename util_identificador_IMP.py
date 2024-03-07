# Implementação do módulo {util_identificador}.

import sys
from util_testes import erro_prog

def de_indice(let, indice):
  assert type(let) is str and len(let) == 1
  assert type(indice) is int and indice >= 0
  id = "%s-%08d" % (let,indice)
  return id

def para_indice(let, ident):
  assert type(let) is str and len(let) == 1
  assert type(ident) is str and len(ident) == 10 
  assert ident[0:1] == let 
  assert ident[1:2] == "-"
  indice = int(ident[2:])
  return indice

def de_lista_de_indices(let, indices):
  ids = [].copy()
  if indices != None:
    assert type(indices) is tuple or type(indices) is list
    # Resultado deve ser uma lista de tuplas, cada uma contendo apenas um índice:
    for el in indices:
      if type(el) is int:
        ids.append(de_indice(let,el))
      elif type(el) is tuple or type(el) is list:
        assert len(el) == 1
        ids.append(de_indice(let,el[0]))
    return ids
  else:
    erro_prog("tipo de " + str(indices) + " inválido")
  
def unico_elemento(ids):
  if ids == None:
    return None
  elif type(ids) is list or type(ids) is tuple:
    if len(ids) == 0:
      return None
    elif len(ids) == 1:
      id = ids[0];
      return id
    else:
      erro_prog("elemento não é único")
  else:
    erro_prog("argumento não é {None} ou lista")
