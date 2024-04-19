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

  erros = [].copy()

  # Valida os valores dos atributos da busca, e elimina campos {None}:
  cmd_args_cp = cmd_args.copy() # Por via das dúvidas.
  for chave, val in cmd_args.items():
    # Elimina campos {None}:
    if val == None:
      del cmd_args_cp[chave]
    # Verifica validade de {val}: 
    if chave == 'video':
      erros += util_valida_campo.identificador(chave, val, "V", False)
    elif chave == 'titulo':
      # !!! Devia aceitar título parcial ou RE !!!
      erros += util_valida_campo.titulo_de_video(chave, val, False)
    elif chave == 'autor':
      erros += util_valida_campo.identificador(chave, val, "U", False)
    elif chave == 'arq':
      erros += util_valida_campo.nome_de_arq_video(chave, val, "U", False)
    elif chave == 'data':
      # !!! Devia aceitar data parcial e intervalo de datas !!!
      erros += util_valida_campo.data(chave, val, "U", False)
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Campo '{chave}' inválido"
  cmd_args = cmd_args_cp
  
  lista_ids_vid = [].copy()
  if len(erros) == 0:
    try:
      if 'video' in cmd_args:
        # Busca por vídeo determinado:
        id_vid = cmd_args['video']
        vid = obj_video.busca_por_identificador(id_vid)
        if vid == None:
          erros.append(f"Vídeo '{id_vid}' não existe")
        else:
          lista_ids_vid = [ id_vid ]
      elif 'arq' in cmd_args:
        # Busca por arquivo de vídeo determinado:
        arq = cmd_args['arq']
        vid = obj_video.busca_por_arquivo(arq)
        if vid == None:
          erros.append(f"Arquivo de vídeo '{arq}' não existe")
        else:
          id_vid = obj_video.obtem_identificador(vid)
          lista_ids_vid = [ id_vid ]
      else:
        # Busca por campos aproximados:
        lista_ids_vid = obj_video.busca_por_semelhanca(cmd_args, False)

      if len(lista_ids_vid) == 0:
        # Não encontrou nenhum usuário:
        erros.append(f"Não foi encontrado nenhum vídeo com os dados fornecidos")

    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(lista_ids_vid) != 0:
    # Encontrou pelo menos um vídeo.  Mostra em forma de tabela:
    ht_titulo = html_bloco_titulo.gera("Vídeos encontrados")
    ht_tabela = html_bloco_lista_de_videos.gera(lista_ids_vid)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Argumentos com erro ou não encontrou nada.
    # Repete a página de busca, com eventuais mensagens de erro:
    admin = obj_sessao.de_administrador(ses)
    pag = html_pag_buscar_videos.gera(ses, cmd_atrs, admin, erros)

  return pag
