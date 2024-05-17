import comando_ver_usuario
import comando_ver_sessao
import comando_ver_video
import comando_ver_comentario

import html_pag_mensagem_de_erro
from util_erros import ErroAtrib
import sys

def processa(ses, cmd_args):
  erros = []
  
  obj_id = None
  if not 'objeto' in cmd_args or cmd_args['objeto'] == None:
    erros.append("O identificador do objeto não foi fornecido")
  else:
    obj_id = cmd_args['objeto'] 
    if not isinstance(obj_id, str) or len(obj_id) != 10:
      erros.append(f"O identificador \"{obj_id}\" é inválido")
  
  pag = None
  if len(erros) == 0:
    letra = obj_id[0]
    if letra == "U":
      pag = comando_ver_usuario.processa(ses, {'usuario': obj_id})
    elif letra == "S":
      pag = comando_ver_sessao.processa(ses, {'sessao': obj_id})
    elif letra == "V":
      pag = comando_ver_video.processa(ses, {'video': obj_id})
    elif letra == "C":
      pag = comando_ver_comentario.processa(ses, {'comentario': obj_id})
    else:
      erros.append(f"A classe de objeto \"{letra}\" é inválida")
  
  if pag == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)

  return pag

