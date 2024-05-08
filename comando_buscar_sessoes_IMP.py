import obj_sessao
import html_bloco_lista_de_sessoes
import html_bloco_titulo
import html_pag_generica
import html_pag_buscar_sessoes
import util_valida_campo
import html_pag_mensagem_de_erro
import obj_usuario
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  # Comando emitido por página do site deveria satisfazer isto:
  assert ses == None or obj_sessao.aberta(ses), f"Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict
  
  erros = [].copy()
  ht_bloco = None

  # Valida os valores dos atributos da busca, e elimina campos {None}:
  cmd_args_cp = cmd_args.copy()
  for chave, val in cmd_args.items():
    if val == None:
      del cmd_args_cp[chave]
    # Verifica validade de {val}:
    if chave == 'usuario':
      erros += util_valida_campo.identificador(chave, val, "U", False)
    elif chave == 'sessao':
      erros += util_valida_campo.identificador(chave, val, "S", False)
    elif chave == 'aberta':
      continue
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Campo '{chave}' inválido"
  cmd_args = cmd_args_cp
  
  lista_ids_sessoes = [].copy()
  if len(erros) == 0:
  # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
    try:
      soh_abertas = False
      if 'aberta' in cmd_args:
        if cmd_args['aberta'] == 'on':
          soh_abertas = True
      if 'usuario' in cmd_args:
        # Deve haver um único usuário com esse identificador:
        id_usr = cmd_args['usuario']
        obj_usr = obj_usuario.obtem_objeto(id_usr) if id_usr != None else None
        if obj_usr == None:
          erros.append(f"Usuário '{id_usr}' não existe")
        else:
          obj_sect = obj_sessao.busca_por_usuario(obj_usr, soh_abertas) if obj_usr != None else None
          for item in obj_sect:
            lista_ids_sessoes.append(item)
      elif 'sessao' in cmd_args:
        # Deve haver uma única sessão com esse identificador:
        id_sessao = cmd_args['sessao']
        obj_sect = obj_sessao.obtem_objeto(id_sessao) if id_sessao != None else None
        if obj_sect == None:
          erros.append(f"Sessão '{id_sessao}' não existe")
        else:
          lista_ids_sessoes = [ id_sessao ]
      else:
        # Busca por campos:
        lista_ids_sessoes = obj_sessao.busca_por_campos(cmd_args, False)

      if len(lista_ids_sessoes) == 0:
        # Não encontrou nenhuma sessão:
        erros.append("Não foi encontrada nenhuma sessão com os dados fornecidos")
    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(lista_ids_sessoes) != 0:
    # Encontrou pelo menos uma sessão.  Mostra em forma de tabela:
    ht_titulo = html_bloco_titulo.gera("Sessões encontradas")
    bt_ver = True
    bt_fechar = True
    mostrar_usr = True # Mostrar a coluna Usuário para o comando buscar sessões.
    ht_tabela = html_bloco_lista_de_sessoes.gera(lista_ids_sessoes, bt_ver, bt_fechar, mostrar_usr)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
