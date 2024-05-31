# Implementação do módulo {comando_buscar_usuarios}.

import obj_video
import obj_sessao
import html_bloco_lista_de_videos
import html_bloco_titulo
import html_pag_generica
import html_pag_buscar_videos
import html_bloco_titulo
import util_identificador
import util_data
import util_dict
import util_booleano
import util_nota
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  # Comando emitido por página do site deveria satisfazer isto:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  erros = []

  # Valida os valores dos atributos da busca, excluindo campos {None}:
  atrs_busca = {}
  for chave, val in cmd_args.items():
    # Elimina campos {None}:
    item_erros = [ ]
    if val == None or val == "":
      pass
    elif chave == 'video':
      item_erros = util_identificador.valida(chave, val, "V", nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'autor':
      item_erros = util_identificador.valida(chave, val, "U", nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'titulo':
      # Busca por semelhança, não deve validar
      if val[0] == "~":
        # Já é padrão:
        atrs_busca[chave] = val
      else:
        # Transforma em padrão para {busca_por_campos}:
        atrs_busca['titulo'] = f"~%{val}%"
    elif chave == 'data' or chave == 'data_min' or chave == 'data_max':
      item_erros = util_data.valida(chave, val, nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'bloqueado':
      item_erros = util_booleano.valida(chave, val, nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = util_booleano.converte(val)
    elif chave == 'nota_min' or chave == 'nota_max':
      item_erros = util_nota.valida(chave, val, nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val

    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Chave inválida '{chave}'"

    erros += item_erros
  
  # Converte 'data_min', 'data_max' para 'data' intervalar:
  erros += util_dict.normaliza_busca_por_data(atrs_busca)
  erros += util_dict.normaliza_busca_por_nota(atrs_busca)
  vid_ids = []
  if len(erros) == 0:
    try:
      if 'video' in cmd_args:
        # Busca por vídeo determinado:
        vid_id = cmd_args['video']
        vid = obj_video.obtem_objeto(vid_id)
        if vid == None:
          erros.append(f"Vídeo \"{vid_id}\" não existe")
        else:
          vid_ids = [ vid_id ]
      else:
        if "bloqueado" not in cmd_args:
          atrs_busca["bloqueado"] = False
        # Busca por campos aproximados:
        vid_ids = obj_video.busca_por_campos(atrs_busca, unico = False)

    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(vid_ids) == 0:
    # Encontrou pelo menos um vídeo.  Mostra em forma de tabela:
    ht_titulo = html_bloco_titulo.gera("Nenhum vídeo foi encontrado")
  else:
    ht_titulo = html_bloco_titulo.gera("Vídeos encontrados")

  ht_tabela = html_bloco_lista_de_videos.gera(vid_ids, mostra_autor = True)
  ht_bloco = \
    ht_titulo + "<br/>\n" + \
    ht_tabela
  pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
