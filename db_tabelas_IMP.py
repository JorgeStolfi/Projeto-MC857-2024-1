# Implementação do módulo {tabelas}.

import sys

# Os principais objetos:
import obj_usuario
import obj_sessao
import obj_video
import obj_comentario
from util_testes import erro_prog, mostra

def inicializa_todas(limpa):
  obj_usuario.inicializa_modulo(limpa)
  obj_sessao.inicializa_modulo(limpa)
  obj_video.inicializa_modulo(limpa)
  obj_comentario.inicializa_modulo(limpa)
  
def identificador_para_objeto(id_obj):
  letra = id_obj[0];
  if letra == "U":
    obj = obj_usuario.busca_por_identificador(id_obj)
  elif letra == "S":
    obj = obj_sessao.busca_por_identificador(id_obj)
  elif letra == "V":
    obj = obj_video.busca_por_identificador(id_obj)
  elif letra == "C":
    obj = obj_comentario.busca_por_identificador(id_obj)
  else:
    erro_prog("identificador '" + id_obj + " inválido")
  return obj

def cria_todos_os_testes(verb):
  # A ordem é importante:
  obj_usuario.cria_testes(verb)    # Não tem atributos de tipo objeto.
  obj_sessao.cria_testes(verb)     # Tem atributos de tipo {obj_usuario.Classe}.
  obj_video.cria_testes(verb)      # Tem atributos de tipo {obj_usuario.Classe}.
  obj_comentario.cria_testes(verb) # Tem atributos de tipo {obj_usuario.Classe}, {obj_video.Classe}.
  


