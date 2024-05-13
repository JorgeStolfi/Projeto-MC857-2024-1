import util_dict_IMP

def elimina_alteracoes_nulas(args_cmd, atrs_obj):
  """
  Supõe que {args_cmd} são argumentos de um comando de alterar
  algum objto {obj} cujos atributos atuais são {atrs_obj}.
  Elimina de {args_cmd} todos os campos cujo valor é igual ao
  valor em {atrs_obj}. 
  
  Supõe que os valores em {args_cmd} não são objetos. Valores em
  {obj_args} que são objetos são considerados iguais aos seus
  identificadores.
  
  Se {obj_args} for {None}, não faz nada.
  """
  return util_dict_IMP.elimina_alteracoes_nulas(args_cmd, atrs_obj)
  
def verifica_chaves_espurias(args_cmd, atrs_obj):
  """Falha com {AssertFailure} se {args_cmd} tiver alguma chave 
  que não está presente em {obj-args}.
  
  Se {obj_args} for {None}, não faz nada."""
  return util_dict_IMP.verifica_chaves_espurias(args_cmd, atrs_obj)

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
  
def para_identificadores(atrs_obj): 
  """Retorna uma cópia do dicionário {atrs} exceto que
  todos os valores que são instâncias de {obj_raiz.Classe}
  são substituídos pelos respectivos identificadores.
  
  Esta função pode ser útil para construir argumentos para comandos
  HTTP."""
  return util_dict_IMP.para_identificadores(atrs)

# !!! Comandos que tratam dados vindos de formularios devem eliminar brancos e newlines inciais e finais de valores de campos antes de validar e usar. !!!
