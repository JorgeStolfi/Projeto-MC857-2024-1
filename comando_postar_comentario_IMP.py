import html_pag_login
import html_pag_postar_comentario
import html_pag_ver_comentario
import obj_comentario
import obj_video
import obj_usuario
import obj_sessao
import util_dict
import util_identificador
import util_texto_de_comentario
from util_erros import ErroAtrib, erro_prog, mostra

import sys

def processa(ses, cmd_args):
  # Estas condições deveriam valer para páginas geradas pelo sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert type(cmd_args) == dict

  erros = []
  cmd_args = cmd_args.copy() # Para não estragar o original.
  
  # Obtém o usuário da sessão:
  ses_dono = None
  ses_dono_id = None
  if ses == None:
    erros.append("É preciso estar logado para postar comentarios")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para postar comentarios")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    ses_dono_id = obj_usuario.obtem_identificador(ses_dono)
  
  # Converte {cmd_args} na lista de atributos {atrs_com} para postagem:
  cmd_args = util_dict.para_identificadores(cmd_args)
  atrs_com = converte_argumentos(cmd_args, ses_dono_id, erros)

  # Tenta criar o comentário:
  com = None
  if len(erros) == 0:
    try:
      com = obj_comentario.cria(atrs_com)
    except ErroAtrib as ex:
      erros += ex.args[0]
      
  if com != None:
    pag = html_pag_ver_comentario.gera(ses, com, erros)
  else:
    # Repete a página de postar comentarios com os mesmos argumentos e mens de erro:
    assert len(erros) > 0
    pag = html_pag_postar_comentario.gera(ses, atrs_com, erros)
  return pag

def converte_argumentos(cmd_args, ses_dono_id, erros):
  """ Converte os argumentos do comando {cmd_args} para atributos
  de {obj_comentario.Classe}.  Se houver erros, acrescenta à lista
  {erros}."""
  
  cmd_args = cmd_args.copy() # Para não estragar o original.
  atrs_com = {}
  
  video_id = cmd_args.pop('video', None)
  if video_id != None:
    erros_item = util_identificador.valida('video', video_id, "V", False)
    if len(erros_item) == 0:
      video = obj_video.obtem_objeto(video_id)
      if video == None:
        erros.append(f"O vídeo {video_id} não existe")
      else:
        atrs_com['video'] = video
    else:
      erros += erros_item
  else:
    erros.append("O atributo 'video' não foi especificado")
    
  # Neste contexto, 'pai' {None} é o mesmo que chave ausente:
  pai_id = cmd_args.pop('pai', None)
  if pai_id != None:
    erros_item = util_identificador.valida('pai', pai_id, "C", False)
    if len(erros_item) == 0:
      pai = obj_comentario.obtem_objeto(pai_id)
      if pai == None:
        erros.append(f"O comentario \"{pai_id}\" não existe")
      elif obj_comentario.obtem_atributo(pai, 'video') != video:
        erros.append(f"O comentario \"{pai_id}\" é a respeito de outro vídeo")
      else:
        atrs_com['pai'] = pai
    else:
      erros += erros_item
  else:
    atrs_com['pai'] = None
  
  autor_id = cmd_args.pop('autor', None)
  if autor_id == None: autor_id = ses_dono_id
  if autor_id != None:
    erros_item = util_identificador.valida('autor', autor_id, "U", False)
    if len(erros_item) == 0:
      autor = obj_usuario.obtem_objeto(autor_id)
      if autor == None:
        erros.append(f"O usuario \"{autor_id}\" não existe")
      elif autor_id != ses_dono_id:
        erros.append(f"O 'autor' especificado tem que ser \"{ses_dono_id}\"")
      else:
        atrs_com['autor'] = autor
    else:
      erros += erros_item
  else:
    erros.append(f"O autor do vídeo não foi especificado")
    
  if 'data' in cmd_args: del cmd_args['data']
  
  texto = cmd_args.pop('texto', None)
  if texto != None:
    erros_item = util_texto_de_comentario.valida('texto', texto, False)
    if len(erros_item) == 0:
      atrs_com['texto'] = texto
    else:
      erros += erros_item
  else:
    erros.append("O texto do comentário não foi especificado")
  
  assert len(cmd_args) == 0, f"Argumentos espurios: \"{str(cmd_args)}\""
    
  return atrs_com
  
