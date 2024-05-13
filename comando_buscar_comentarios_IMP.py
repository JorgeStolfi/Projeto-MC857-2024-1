import sys
import obj_comentario
import obj_sessao
import html_bloco_lista_de_comentarios
import html_pag_generica
import html_pag_buscar_comentarios


def processa(ses, cmd_args):

  # Estas condições deveriam valer para comandos emitidos pelas páginas do site:
  assert ses == None or obj_sessao.aberta(ses), "Sessão inválida"

  erros = []
  resultados = []

  # Obtém os valores dos campos para busca, ou {None} se não fornecidos:
  com_id = cmd_args.get("comentario", None)
  id_aut = cmd_args.get("autor", None) 
  vid_id = cmd_args.get("video", None)
  pai_id = cmd_args.get("pai", None)
  texto = cmd_args.get("texto", None)
  data = cmd_args.get("data", None)

  if com_id is not None:
    if vid_id is not None or id_aut is not None or pai_id is not None or texto is not None or data is not None:
      erros.append("Busca por ID de comentário não permite outros critérios")
    else:
      com = obj_comentario.obtem_objeto(com_id)
      if com is None:
        erros.append(f"Comentário {com_id} não existe")
      else:
        resultados.append(com_id)
  else:
    campos_definidos = []

    for chave, val in  [
      ("autor", id_aut),
      ("video", vid_id), 
      ("pai", pai_id), 
      ("texto", texto), 
      ("data", data)
      ]:
      if val is not None:
        campos_definidos.append((chave, val))

    dict_de_busca = dict(campos_definidos)
    lista_ids = obj_comentario.busca_por_campos(dict_de_busca)

    resultados += lista_ids if lista_ids is not None else []
    
    if len(resultados) == 0 or lista_ids is None:
      erros.append("Nenhum comentário encontrado.")

  if len(erros) != 0:
    pag = html_pag_buscar_comentarios.gera(ses, cmd_args, erros)
  else:
    # Elimina repetições e ordena:
    resultados = sorted(list(set(resultados)))
    # Converte a lista de identificadores para tabela de atributos:
    ht_bloco = html_bloco_lista_de_comentarios.gera(resultados, True, True, True)
    pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
