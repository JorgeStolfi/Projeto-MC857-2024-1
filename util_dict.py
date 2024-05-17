import util_dict_IMP

def elimina_alteracoes_nulas(args_cmd, obj_atrs):
  """
  Supõe que {args_cmd} são argumentos de um comando de alterar
  algum objto {obj} cujos atributos atuais são {obj_atrs}.
  Modifica {args_cmd} eliminando todos os campos cujo valor é igual ao
  valor em {obj_atrs}. 
  
  Valores que são objetos são considerados iguais aos seus
  identificadores.
  
  Falha com {AssertFailure} se {args_cmd} tiver alguma chave 
  que não está presente em {obj_atrs}.
  
  Se {obj_atrs} for {None}, não faz nada.
  """
  return util_dict_IMP.elimina_alteracoes_nulas(args_cmd, obj_atrs)

def para_objetos(args_cmd):
  """Retorna uma cópia do dicionário {args_cmd} exceto que
  todos os valores que tem aparência de identificadores 
  de objetos são substituídos pelos objetos correspondentes.
  
  Se algum identificador não corresponder a um objeto existente,
  levanta a exceção {ErroAtrib} com as mensagens de erro 
  correspondentes.
  
  Esta função é útil para processar argumentos de comandos
  HTTP."""
  return util_dict_IMP.para_objetos(args_cmd)
  
def para_identificadores(obj_atrs): 
  """Retorna uma cópia do dicionário {obj_atrs} exceto que
  todos os valores que são instâncias de {obj_raiz.Classe}
  são substituídos pelos respectivos identificadores.
  
  Esta função pode ser útil para construir argumentos para comandos
  HTTP."""
  return util_dict_IMP.para_identificadores(obj_atrs)

def normaliza_busca_por_data(atrs):
  """Se {atrs} tiver campos 'data_min' e 'data_max',
  substitui ambos por 'data' cujo valoe é a lista
  {(val_min, val_max)} dos respectivos valores.
  
  Se uma dessas duas chaves estiver presente em {atrs},
  autra também deve estar, a chave 'data' não deve estar.
  
  Em caso de erro, devolve uma lista de mensagens (strings).
  Se não houver erros, devolve uma lista vazia."""
  return util_dict_IMP.normaliza_busca_por_data(atrs)

# !!! Comandos que tratam dados vindos de formularios devem eliminar brancos e newlines inciais e finais de valores de campos antes de validar e usar. !!!
