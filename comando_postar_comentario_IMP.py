
import html_pag_login
import html_pag_postar_comentario
import obj_comentario
import obj_video
import obj_usuario
import obj_sessao
from util_erros import ErroAtrib, erro_prog, mostra
import re
import sys

def processa(ses, cmd_args):
  # Estas condições deveriam valer para páginas geradas pelo sistema:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert type(cmd_args) == dict

  erros = [].copy()
  
  # Obtém o usuário da sessão:
  usr_ses = obj_sessao.obtem_usuario(ses)
  assert usr_ses != None
  
  atrs_com = converte_argumentos(cmd_args, usr_ses, erros)

  # Tenta criar o comentário:
  com = None
  if len(erros) == 0:
    try:
      com = obj_comentario.cria(atrs_com)
    except ErroAtrib as ex:
      erros += ex.args[0]
      
  if com != None:
    pag = html_pag_ver_comentario.gera(ses, com)
  else:
    # Repete a página de postar comentarios com os mesmos argumentos e mens de erro:
    assert len(erros) > 0
    pag = html_pag_postar_comentario.gera(ses, atrs_com, erros)
  return pag

def converte_argumentos(cmd_args, usr_ses, erros):
  """ Converte os argumentos do comando {cmd_args} para atributos
  de {obj_comentario.Classe}.  Se houver erros, acrescenta à lista
  {erros}."""
  
  cmd_args = cmd_args.copy() # Para não estragar o original.
  atrs_com = {}.copy()
  
  assert 'video' in cmd_args and cmd_args['video'] != None, "Campo 'video' não especificado"
  id_video = cmd_args['video']
  if 'video' in cmd_args: del cmd_args['video']
  video = obj_video.busca_por_identificador(id_video)
  if video == None:
    erros.append(f"video {ìd_video} não existe")
  else:
    atrs_com['video'] = video
    
  if 'pai' in cmd_args and cmd_args['pai'] != None:
    id_pai = cmd_args['pai']
    if 'pai' in cmd_args: del cmd_args['pai']
    pai = obj_comentario.busca_por_identificador(id_pai)
    if pai == None:
      erros.append(f"comentario {ìd_pai} não existe")
    elif obj_comentario.obtem_atributo(pai, 'video') != video:
      erros.append(f"comentario {ìd_pai} é de outro vídeo")
    else:
      atrs_com['pai'] = pai
  else:
    atrs_com['pai'] = None
  
  if 'autor' in cmd_args and cmd_args['autor'] != None:
    id_autor = cmd_args['autor']
    if 'autor' in cmd_args: del cmd_args['autor']
    autor = obj_usuario.busca_por_identificador(id_autor)
    if autor == None:
      erros.append(f"usuario {ìd_autor} não existe")
    elif autor != usr_ses:
      erros.append(f"usuario logado não é {id_autor}")
    else:
      atrs_com['autor'] = autor
  else:
    atrs_com['autor'] = usr_ses
    
  if 'data' in cmd_args: del cmd_args['data']
  
  if 'titulo' in cmd_args and cmd_args['titulo'] != None:
    titulo = cmd_args['titulo']
    if 'titulo' in cmd_args: del cmd_args['titulo']
    atrs_com['titulo'] = titulo
  
  if len(cmd_args) != 0:
    erros.append(f"Argumentos espurios: {str(cmd_args)}")
    
  return atrs_com
  
