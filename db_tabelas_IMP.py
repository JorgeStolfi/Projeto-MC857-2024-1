# Implementação do módulo {tabelas}.

import sys

# Os principais objetos:
import obj_usuario
import obj_sessao
from util_testes import erro_prog, mostra

def inicializa_todas(limpa):
  obj_usuario.inicializa_modulo(limpa)
  obj_sessao.inicializa_modulo(limpa)
  
def id_para_objeto(id):
  letra = id[0];
  if letra == "U":
    obj = obj_usuario.busca_por_identificador(id)
  elif letra == "S":
    obj = obj_sessao.busca_por_identificador(id)
  else:
    erro_prog("identificador '" + id + " inválido")
  return obj

def cria_todos_os_testes(verb):
  # A ordem é importante:
  obj_usuario.cria_testes(verb) # Não tem atributos de tipo objeto.
  obj_sessao.cria_testes(verb)  # Tem atributos de tipo {obj_usuario.Classe}.
  


