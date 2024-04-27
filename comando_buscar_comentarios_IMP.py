import obj_comentario
import obj_sessao
import html_bloco_lista_de_comentarios
import html_pag_generica
import html_pag_buscar_comentarios


def processa(ses, cmd_args):
  erros = [].copy()
  
  if ses is not None:
    if not obj_sessao.aberta(ses):
      erros.append("Sessão inválida.")

  result_coms = []

  if cmd_args.get("comentario", None) is not None:
    com = obj_comentario.busca_por_identificador(cmd_args["comentario"])

    if com is None:
      erros.append("Comentário não encontrado pelo identificador.")

    result_coms.append(obj_comentario.obtem_identificador(com))


  if cmd_args.get("autor", None) is not None:
    result_coms.extend(obj_comentario.busca_por_autor(cmd_args["autor"]))

  if cmd_args.get("video", None) is not None:
    result_coms.extend(obj_comentario.busca_por_video(cmd_args["video"]))

  if cmd_args.get("pai", None) is not None:
    # !! BUSCA POR PAI AINDA NÃO IMPLEMENTADA !!	
    result_coms.extend(obj_comentario.busca_por_pai(cmd_args["pai"]))
  
  if cmd_args.get("texto", None) is not None:
    # !! BUSCA POR TEXTO AINDA NÃO IMPLEMENTADA !!	
    result_coms.extend(obj_comentario.busca_por_texto(cmd_args["texto"]))

  if cmd_args.get("data", None) is not None:
    # !! BUSCA POR DATA AINDA NÃO IMPLEMENTADA !!	
    result_coms.extend(obj_comentario.busca_por_data(cmd_args["data"]))

  if not result_coms:
    erros.append("Nenhum comentário encontrado.")

  if erros:
    return html_pag_buscar_comentarios.gera(ses, cmd_args, erros)

  ht_bloco = html_bloco_lista_de_comentarios.gera(result_coms, True, True, True)
  pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
