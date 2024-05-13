import comando_ver_usuario
import comando_ver_sessao
import comando_ver_video
import comando_ver_comentario

import html_pag_mensagem_de_erro
from util_erros import ErroAtrib
import sys

def processa(ses, cmd_args):
  erros = []
  
  id_obj = None
  if not 'objeto' in cmd_args or cmd_args['objeto'] == None:
    erros.append("O identificador do objeto não foi fornecido")
  else:
    id_obj = cmd_args['objeto'] 
    if not isinstance(id_obj, str) or len(id_obj) != 10:
      erros.append(f"O identificador \"{str(id_obj)}\" é inválido")
  
  pag = None
  if len(erros) == 0:
    letra = id_obj[0]
    if letra == "U":
      pag = comando_ver_usuario.processa(ses, {'usuario': id_obj})
    elif letra == "S":
      pag = comando_ver_sessao.processa(ses, {'sessao': id_obj})
    elif letra == "V":
      pag = comando_ver_video.processa(ses, {'video': id_obj})
    elif letra == "C":
      pag = comando_ver_comentario.processa(ses, {'comentario': id_obj})
    else:
      erros.append(f"Classe de objeto \"{letra}\" inválida")
  
  if pag == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)

  return pag

