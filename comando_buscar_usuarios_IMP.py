import obj_usuario
import obj_sessao
import html_bloco_lista_de_usuarios
import html_pag_generica
import html_pag_buscar_usuarios
import html_bloco_titulo
import util_identificador
import util_email
import util_nome_de_usuario

from util_erros import ErroAtrib

def processa(ses, cmd_args):
  # Comando emitido por página do site deveria satisfazer isto:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and type(cmd_args) is dict
  
  para_admin = ses != None and obj_sessao.de_administrador(ses)
  
  erros = []
  # Valida os valores dos atributos da busca, e elimina campos {None}:
  atrs_busca = {}
  for chave, val in cmd_args.items():
    item_erros = [ ]
    if val == None or (isinstance(val, str) and len(val) == 0):
      pass
    elif chave == 'usuario':
      item_erros = util_identificador.valida(chave, val, "U", nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'email':
      item_erros = util_email.valida(chave, val, nulo_ok = False)
      if len(item_erros) == 0: atrs_busca[chave] = val
    elif chave == 'nome':
      # Busca por semelhança, não precisa validar:
      if val[0] == "~":
        # Já é padrão:
        atrs_busca[chave] = val
      else:
        # Transforma em padrão para {busca_por_campos}:
        atrs_busca['nome'] = f"~%{val}%"
    elif chave == 'administrador':
      item_erros = util_booleano.valida(chave, val, nulo_ok)
      if len(item_erros) == 0: atrs_busca[chave] = util_booleano.converte(val)
    elif chave == 'senha':
      item_erros = [ f"Busca por '{chave}' não é permitida" ]
    elif chave == 'vnotaMin' or chave == 'vnotaMax':
      if float(val) > 4:
        assert False, f"Chave inválida '{chave}'"
    elif chave == 'cnotaMin' or chave == 'cnotaMax':
      if float(val) > 4:
        assert False, f"Chave inválida '{chave}'"
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Chave inválida '{chave}'"

    erros += item_erros

  atrs_busca['vnota'] = (
    max(float(cmd_args.get('vnotaMin', 0)), 0),
    min(float(cmd_args.get('vnotaMax', 4)), 4)
  )
  atrs_busca['cnota'] = (
    max(float(cmd_args.get('cnotaMin', 0)), 0),
    min(float(cmd_args.get('cnotaMax', 4)), 4)
  )

  usr_res_ids = []
  if len(erros) == 0:
  # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
    try:
      if 'usuario' in atrs_busca:
        # Deve haver um único usuário com esse identificador:
        usr_bus_id = atrs_busca['usuario']
        obj_usr = obj_usuario.obtem_objeto(usr_bus_id) if usr_bus_id != None else None
        if obj_usr == None:
          erros.append(f"O usuário \"{usr_bus_id}\" não existe")
        else:
          usr_res_ids = [ usr_bus_id ]
      elif 'email' in atrs_busca:
        # Deve haver um único usuário com esse email
        if not para_admin:
          erros.append("Busca por email só é permitida para administradores")
        else:
          email_bus = atrs_busca['email']
          usr_res_id = obj_usuario.busca_por_email(email_bus)
          if usr_res_id == None:
            erros.append(f"Não existe usuário com email \"{email_bus}\"")
          else:
            usr_res_ids = [ usr_res_id ]
      else:
        # Busca por campos:
        usr_res_ids = obj_usuario.busca_por_campos(atrs_busca, unico = False)

      if len(usr_res_ids) == 0:
        # Não encontrou nenhum usuário:
        erros.append("Não foi encontrado nenhum usuário com os dados fornecidos")
    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(usr_res_ids) != 0:
    # Encontrou pelo menos um usuário.  Mostra em forma de tabela:
    ht_titulo = ht_titulo = html_bloco_titulo.gera("Usuários encontrados")
    ht_tabela = html_bloco_lista_de_usuarios.gera(para_admin, usr_res_ids)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Não encontrou nenhum usuário.
    # Repete a página de busca, com eventuais mensagens de erro:
    pag = html_pag_buscar_usuarios.gera(ses, cmd_args, erros)

  return pag

