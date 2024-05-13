import obj_sessao
import obj_usuario
import html_bloco_lista_de_sessoes
import html_bloco_titulo
import html_pag_generica
import html_pag_buscar_sessoes
import html_pag_mensagem_de_erro
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  # Comando emitido por página do site deveria satisfazer isto:
  assert ses == None or obj_sessao.aberta(ses), f"Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict
  
  erros = []
  ht_bloco = None

  # Valida os valores dos atributos da busca, e elimina campos {None}:
  cmd_args_cp = cmd_args.copy()
  for chave, val in cmd_args.items():
    if val == None:
      del cmd_args_cp[chave]
    # Verifica validade de {val}:
    if chave == 'usuario':
      erros += util_identificador.valida(chave, val, "U", False)
    elif chave == 'sessao':
      erros += util_identificador.valida(chave, val, "S", False)
    elif chave == 'aberta':
      continue
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Campo '{chave}' inválido"
  cmd_args = cmd_args_cp
  
  ses_ids_res = []
  if len(erros) == 0:
  # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
    try:
      soh_abertas = False
      if 'aberta' in cmd_args:
        if cmd_args['aberta'] == 'on':
          soh_abertas = True
      if 'usuario' in cmd_args:
        # Deve haver um único usuário com esse identificador:
        usr_id = cmd_args['usuario']
        obj_usr = obj_usuario.obtem_objeto(usr_id) if usr_id != None else None
        if obj_usr == None:
          erros.append(f"Usuário '{usr_id}' não existe")
        else:
          obj_sect = obj_sessao.busca_por_dono(obj_usr, soh_abertas) if obj_usr != None else None
          for item in obj_sect:
            ses_ids_res.append(item)
      elif 'sessao' in cmd_args:
        # Deve haver uma única sessão com esse identificador:
        sessao_id = cmd_args['sessao']
        obj_sect = obj_sessao.obtem_objeto(sessao_id) if sessao_id != None else None
        if obj_sect == None:
          erros.append(f"Sessão '{sessao_id}' não existe")
        else:
          ses_ids_res = [ sessao_id ]
      else:
        # Busca por campos:
        ses_ids_res = obj_sessao.busca_por_campos(cmd_args, False)

      if len(ses_ids_res) == 0:
        # Não encontrou nenhuma sessão:
        erros.append("Não foi encontrada nenhuma sessão com os dados fornecidos")
    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(ses_ids_res) != 0:
    # Encontrou pelo menos uma sessão.  Mostra em forma de tabela:
    ht_titulo = html_bloco_titulo.gera("Sessões encontradas")
    bt_ver = True
    bt_fechar = True
    mostrar_usr = True # Mostrar a coluna Usuário para o comando buscar sessões.
    ht_tabela = html_bloco_lista_de_sessoes.gera(ses_ids_res, bt_ver, bt_fechar, mostrar_usr)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
