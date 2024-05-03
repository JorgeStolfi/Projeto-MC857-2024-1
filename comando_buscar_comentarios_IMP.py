import obj_comentario
import obj_sessao
import html_bloco_lista_de_comentarios
import html_pag_generica
import html_pag_buscar_comentarios


def processa(ses, cmd_args):

  # Estas condições deveriam valer para comandos emitidos pelas páginas do site:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"

  erros = [].copy()
  resultados = [].copy()

  # Obtém os valores dos campos para busca, ou {None} se não fornecidos:
  id_com = cmd_args.get("comentario", None)
  id_aut = cmd_args.get("autor", None) 
  id_vid = cmd_args.get("video", None)
  id_pai = cmd_args.get("pai", None)
  texto = cmd_args.get("texto", None)
  data = cmd_args.get("data", None)

  if id_com is not None:
    if id_vid != None or id_aut != None or id_pai != None or texto != None or data != None:
      erros.append(f"Busca por ID de comentário não permite outros critérios")
    else:
      com = obj_comentario.obtem_objeto(id_com)
      if com is None:
        erros.append(f"Comentário {id_com} não existe")
      else:
        resultados.append(id_com)
  else:
    # !!! Condição de busca deveria ser "E" não "OU" !!!
    if id_aut is not None:
      resultados += obj_comentario.busca_por_autor(id_aut)

    if id_vid is not None:
      resultados += obj_comentario.busca_por_video(id_vid)

    if id_pai is not None:
      resultados += obj_comentario.busca_por_pai(id_pai)

    if texto is not None:
      # !!! Implementar {obj_comentario.busca_por_campo} !!!
      # !!! resultados += obj_comentario.busca_por_campo('texto', texto) !!!
      pass

    if data is not None:
      # !!! Implementar {obj_comentario.busca_por_campo} !!!
      # !!! resultados += obj_comentario.busca_por_campo('data', data) !!!
      pass

    if len(resultados) == 0:
      erros.append("Nenhum comentário encontrado.")

  if len(erros) != 0:
    pag = html_pag_buscar_comentarios.gera(ses, cmd_args, erros)
  else:
    # Elimina repetições e ordena:
    resultados = list(set(resultados))
    resultados.sort()
    # Converte a lista de identificadores para tabela de atributos:
    ht_bloco = html_bloco_lista_de_comentarios.gera(resultados, True, True, True)
    pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
