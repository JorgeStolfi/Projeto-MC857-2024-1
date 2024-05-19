import obj_comentario
import obj_sessao
import html_bloco_lista_de_comentarios
import html_bloco_titulo
import html_pag_generica
import html_pag_buscar_comentarios
import util_identificador
import util_dict
import util_data

import sys

def processa(ses, cmd_args):

  # Estas condições deveriam valer para comandos emitidos pelas páginas do site:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  erros = []
  resultados = []

  # Obtém os valores dos campos para busca, ou {None} se não fornecidos:
  atrs_busca = { }
  for chave, val in cmd_args.items():
    item_erros = [ ]
    if chave == 'pai':
      # Valor {None} é significativo para 'pai':
      # !!! Esta convenção é confusa. !!!
      item_erros = util_identificador.valida(chave, val, "C", nulo_ok = True)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif val == None or (isinstance(val, str) and len(val) == 0):
      # Valor {None} nos demais casos significa "qualquer valor":
      pass
    elif chave == 'comentario':
      item_erros = util_identificador.valida(chave, val, "C", nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'autor':
      item_erros = util_identificador.valida(chave, val, "U", nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'video':
      item_erros = util_identificador.valida(chave, val, "V", nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'data' or chave == 'data_min' or chave == 'data_max':
      item_erros = util_data.valida(chave, val, nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'texto':
      # Busca por semelhança, não precisa validar:
      if val[0] == "~":
        # Já é padrão:
        atrs_busca[chave] = val
      else:
        # Transforma em padrão para {busca_por_campos}:
        atrs_busca['texto'] = f"~%{val}%"
    elif chave == 'bloqueado':
      # Valor 'on' significa "só abertas", 'off' significa "qualquer"
      if val == 'True':
        atrs_busca[chave] = True
      elif val == 'False':
        atrs_busca[chave] = False
      else:
        item_erros = [ f"O valor do atributo '{chave}' = \"{val}\" é inválido" ]
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Chave inválida '{chave}'"

    erros += item_erros
  
  if len(atrs_busca) == 0:
    erros.append(f"É preciso especificar pelo menos um parâmetro para a busca")
  
  # Converte 'data_min', 'data_max' para 'data' intervalar:
  erros += util_dict.normaliza_busca_por_data(atrs_busca)

  if 'comentario' in atrs_busca:
    if len(atrs_busca) != 1:
      erros.append("Busca por ID de comentário não permite outros critérios")

  # Faz a busca, resultado é a lista {com_ids_res} de identificadores de comentarios:
  com_ids_res = []
  if len(erros) == 0:
    if 'comentario' in atrs_busca:
      com_id_res = atrs_busca['comentario']
      com_res = obj_comentario.obtem_objeto(com_id_res)
      if com_res == None:
        erros.append(f"O comentário \"{com_id_res}\" não existe")
      else:
        com_ids_res = [ com_id_res, ]
    else:
      # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
      try:
        com_ids_res = obj_comentario.busca_por_campos(atrs_busca, unico = False)
        if len(com_ids_res) == 0:
          erros.append("Não foi encontrado nenhum comentário com os dados fornecidos")
      except ErroAtrib as ex:
        erros += ex.args[0]

  if len(erros) == 0:
    assert len(com_ids_res) > 0
    # Mostra os comentários encontrados na forma de tabela:
    assert len(com_ids_res) > 0
    com_ids_res = sorted(list(com_ids_res))
    ht_titulo = html_bloco_titulo.gera("Comentários encontrados")
    ht_tabela = html_bloco_lista_de_comentarios.gera \
      ( com_ids_res, 
        mostra_autor = True,
        mostra_video = True,
        mostra_pai = True,
      )
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Repete o formulário com os dados válidos:
    pag = html_pag_buscar_comentarios.gera(ses, cmd_args, erros)

  return pag
