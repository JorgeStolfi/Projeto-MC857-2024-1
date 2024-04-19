# Implementação do módulo {util_identificador}.

import sys
from util_erros import erro_prog

def de_indice(let, indice):
  assert type(let) is str and len(let) == 1
  assert type(indice) is int and indice >= 0
  id_obj = "%s-%08d" % (let,indice)
  return id_obj

def para_indice(let, id_obj):
  assert type(let) is str and len(let) == 1
  assert type(id_obj) is str and len(id_obj) == 10 
  assert id_obj[0:1] == let 
  assert id_obj[1:2] == "-"
  indice = int(id_obj[2:])
  return indice

def de_lista_de_indices(let, lista_indices):
  lista_ids_obj = [].copy()
  if lista_indices != None:
    assert type(lista_indices) is tuple or type(lista_indices) is list
    # Resultado deve ser uma lista de tuplas, cada uma contendo apenas um índice:
    for el in lista_indices:
      if type(el) is int:
        lista_ids_obj.append(de_indice(let,el))
      elif type(el) is tuple or type(el) is list:
        assert len(el) == 1
        lista_ids_obj.append(de_indice(let,el[0]))
    return lista_ids_obj
  else:
    erro_prog("tipo de " + str(lista_indices) + " inválido")
