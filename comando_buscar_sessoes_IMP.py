import obj_sessao
import obj_usuario
import html_bloco_lista_de_sessoes
import html_bloco_titulo
import html_pag_generica
import html_pag_buscar_sessoes
import html_pag_mensagem_de_erro
from util_erros import ErroAtrib
import util_data
import util_dict
import util_identificador

def processa(ses, cmd_args):

  # Chamadas de {processa_comando_http.preocessa} devem satisfazer isto:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  erros = []
  
  ses_dono = None
  if ses == None:
    erros.append("É preciso estar logado para efetuar esta ação")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para efetuar esta ação")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)

  para_admin = ses != None and obj_sessao.de_administrador(ses)

  # Pega os valores dos atributos da busca, e elimina campos {None}:
  atrs_busca = { }
  for chave, val in cmd_args.items():
    item_erros = [ ]
    if val == None:
      # Valor {None} signfica "qualquer valor":
      pass
    elif chave == 'dono':
      item_erros = util_identificador.valida(chave, val, "U", False)
      if len(item_erros) == 0: atrs_busca['dono'] = val
    elif chave == 'sessao':
      item_erros = util_identificador.valida(chave, val, "S", False)
      if len(item_erros) == 0: atrs_busca['sessao'] = val
    elif chave == 'aberta':
      # Valor 'on' significa "só abertas", 'off' significa "qualquer"
      if val == 'on':
        atrs_busca[chave] = True
      elif val == 'off':
        pass
      else:
        item_erros = [ f"O valor do atributo '{chave}' = \"{val}\" é inválido" ]
    elif chave == 'criacao' or chave == 'criacao_min' or chave == 'criacao_max':
      item_erros = util_data.valida(chave, val, nulo_ok=False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'cookie':
      atrs_busca[chave] = val
    else:
      item_erros = [ f"Sessões não tem o atributo '{chave}'" ]

    erros += item_erros
  
  if len(atrs_busca) == 0:
    erros.append(f"É preciso especificar pelo menos um parâmetro para a busca")
  
  # Converte 'data_min', 'data_max' para 'data' intervalar:
  erros += util_dict.normaliza_busca_por_data(atrs_busca)
      
  # Busca por 'sessao' é categórica:
  if 'sessao' in atrs_busca:
    if len(atrs_busca) != 1:
      erros.append("Busca por ID de sessão não deve ser combinada com outros critérios")
  
  # Faz a busca, resultado é a lista {ses_ids_res} de identificadores de sessões:
  ses_ids_res = []
  if len(erros) == 0:
    if 'sessao' in atrs_busca:
      ses_id_res = atrs_busca['sessao']
      ses_res = obj_sessao.obtem_objeto(ses_id_res)
      if ses_res == None:
        erros.append(f"A sessão \"{ses_id_res}\" não existe")
      else:
        ses_ids_res = [ ses_id_res, ]
    else:
      # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
      try:
        ses_ids_res = obj_sessao.busca_por_campos(atrs_busca, unico = False)
        if len(ses_ids_res) == 0:
          erros.append("Não foi encontrada nenhuma sessão com os dados fornecidos")
      except ErroAtrib as ex:
        erros += ex.args[0]

  if len(erros) == 0:
    # Mostra as sessãoes encontradas na forma de tabela:
    assert len(ses_ids_res) > 0
    ses_ids_res = sorted(list(ses_ids_res))
    ht_titulo = html_bloco_titulo.gera("Sessões encontradas")
    ht_tabela = html_bloco_lista_de_sessoes.gera\
      ( ses_ids_res, 
        bt_ver = True, bt_fechar = para_admin, 
        mostra_dono = True,
      )
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  elif ses_dono != None:
    # Repete o formulário com os dados válidos:
    pag = html_pag_buscar_sessoes.gera(ses, atrs_busca, erros)
  else:
    # Não vale a pena repetir of formulário:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)

  return pag
