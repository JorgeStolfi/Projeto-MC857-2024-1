# Implementação do módulo {comando_buscar_usuarios}.

import obj_video
import obj_sessao
import html_bloco_lista_de_videos
import html_bloco_titulo
import html_pag_generica
import html_pag_buscar_videos
import html_bloco_titulo
import util_valida_campo
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  # Comando emitido por página do site deveria satisfazer isto:
  assert ses == None or obj_sessao.aberta(ses), f"Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict

  erros = []

  # Valida os valores dos atributos da busca, e elimina campos {None}:
  cmd_args_cp = cmd_args.copy() # Por via das dúvidas.
  for chave, val in cmd_args.items():
    # Elimina campos {None}:
    if val == None:
      del cmd_args_cp[chave]
    # Verifica validade de {val}: 
    if chave == 'video':
      erros += util_identificador.valida(chave, val, "V", False)
    elif chave == 'titulo':
      # !!! Devia aceitar título parcial ou RE !!!
      erros += util_titulo_de_video.valida(chave, val, False)
    elif chave == 'autor':
      erros += util_identificador.valida(chave, val, "U", False)
    elif chave == 'data':
      # !!! Devia aceitar data parcial e intervalo de datas !!!
      erros += util_data.valida(chave, val, "U", False)
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Campo '{chave}' inválido"
  cmd_args = cmd_args_cp
  
  vid_ids = []
  if len(erros) == 0:
    try:
      if 'video' in cmd_args:
        # Busca por vídeo determinado:
        vid_id = cmd_args['video']
        vid = obj_video.obtem_objeto(vid_id)
        if vid == None:
          erros.append(f"Vídeo '{vid_id}' não existe")
        else:
          vid_ids = [ vid_id ]
      else:
        # Busca por campos aproximados:
        vid_ids = obj_video.busca_por_semelhanca(cmd_args, False)

      if len(vid_ids) == 0:
        # Não encontrou nenhum usuário:
        erros.append(f"Não foi encontrado nenhum vídeo com os dados fornecidos")

    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(vid_ids) != 0:
    # Encontrou pelo menos um vídeo.  Mostra em forma de tabela:
    ht_titulo = html_bloco_titulo.gera("Vídeos encontrados")
    ht_tabela = html_bloco_lista_de_videos.gera(vid_ids)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Argumentos com erro ou não encontrou nada.
    # Repete a página de busca, com eventuais mensagens de erro:
    admin = obj_sessao.de_administrador(ses)
    pag = html_pag_buscar_videos.gera(ses, cmd_args, erros)

  return pag
