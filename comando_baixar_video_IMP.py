import obj_sessao
import obj_video
import obj_usuario
import html_bloco_titulo
import html_elem_button_simples
import html_pag_generica
import html_pag_mensagem_de_erro
import util_video

import sys

def processa(ses, cmd_args):
  
  # Estas condições devem valer para comandos emitidos por páginas do sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  cmd_args = cmd_args.copy() # Por via das dúvidas.
  erros = []
  
  # Obtem o dono da sessão corrente:
  ses_dono = None
  para_admin = False
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação.")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta ação.")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono is not None
    para_admin = obj_usuario.eh_administrador(ses_dono)

  # Obtém o vídeo {vid} para baixar, e elimina 'video' de {cmd_args}:
  vid_id = cmd_args.pop('video', None)
  if vid_id != None:
    vid = obj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"O vídeo \"{vid_id}\" não existe")
  else:
    erros.append("O vídeo a baixar não foi especificado")
    vid = None
  
  if vid != None:
    # Converte 'inicio', 'fim' para tempos em segundos, fracionários.
    inicio = float(cmd_args["inicio"])
    fim = cmd_args["fim"]
    if fim is not None:
        fim = float(fim)

    # Se iguais ou 'fim' == None, devolve o nome do quadro em "quadros/{vid_id}-{RRRRRRRR}.mp4"
    # Se diferentes, devolve o nome do vídeo em "videos/{vid_id}-{RRRRRRRR}.mp4"
    if inicio == fim or fim is None:
        nome = util_video.extrai_quadro(vid_id, inicio)
        url = "quadros/" + nome
    else:
        nome = util_video.extrai_trecho(vid_id, inicio, fim)
        url = "videos/" + nome
  
  pag = None
  if (len(erros) == 0):
    ht_titulo = html_bloco_titulo.gera("Vídeo pronto para baixar")
    ht_bt_baixar = html_elem_button_simples.gera("Baixar", url, None, None)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_bt_baixar 
    pag = html_pag_generica.gera(ses, ht_bloco, erros)

  if pag == None:
    # Não vale a pena repetir:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)

  return pag
