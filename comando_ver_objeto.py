import comando_ver_objeto_IMP

def processa(ses, args):
  """Essa função retorna uma página HTML com as informações referentes ao 
  objeto cujo identificador é {args['id_objeto']}.  A classe do objeto é
  determinada pela primeira letra ("U" para {obj_usuario.Classe},  
  "S" para {obj_sessao.Classe}, etc."""
  return comando_ver_objeto_IMP.processa(ses, args)
