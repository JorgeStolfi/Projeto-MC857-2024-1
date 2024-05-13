# Implementação do módulo {comando_buscar_usuarios}.

import obj_usuario
import obj_sessao
import html_bloco_lista_de_usuarios
import html_pag_generica
import html_pag_buscar_usuarios
import html_bloco_titulo
import util_valida_campo
from util_erros import ErroAtrib

def processa(ses, cmd_args):

  # Comando emitido por página do site deveria satisfazer isto:
  assert ses == None or obj_sessao.aberta(ses), f"Sessão inválida"
  assert cmd_args != None and type(cmd_args) is dict
  
  para_admin = ses != None and obj_sessao.eh_administrador(ses)
  
  erros = []

  # Valida os valores dos atributos da busca, e elimina campos {None}:
  atrs_bus = cmd_args.copy()
  nulo_ok = False
  for chave, val in atrs_bus.items():
    if val == None:
      
      del atrs_bus[chave]
    elif chave == 'usuario':
      erros += util_identificador.valida(chave, val, "U", nulo_ok)
    elif chave == 'email':
      erros += obj_usuario.valida_email(chave, val, nulo_ok)
    elif chave == 'nome':
      parcial = True
      erros += obj_usuario.valida_nome(chave, val, nulo_ok, parcial)
    elif chave == 'administrador':
      erros += util_booleano.valida(chave, val, nulo_ok)
    elif chave == 'senha':
      erros.append(f"Busca por '{chave}' não é permitida")
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Campo '{chave}' inválido"

  usr_res_ids = []
  if len(erros) == 0:
  # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
    try:
      if 'usuario' in atrs_bus:
        # Deve haver um único usuário com esse identificador:
        usr_bus_id = atrs_bus['usuario']
        obj_usr = obj_usuario.obtem_objeto(usr_bus_id) if usr_bus_id != None else None
        if obj_usr == None:
          erros.append(f"Usuário \"{usr_bus_id}\" não existe")
        else:
          usr_res_ids = [ usr_bus_id ]
      elif 'email' in atrs_bus:
        # Deve haver um único usuário com esse email
        if not para_admin:
          erros.append("Busca por email só é permitida para administradores")
        else:
          email_bus = atrs_bus['email']
          usr_res_id = obj_usuario.busca_por_email(email_bus)
          if usr_res_id == None:
            erros.append(f"Não existe usuário com email = \"{email_bus}\"")
          else:
            usr_res_ids = [ usr_res_id ]
      else:
        # Busca por campos aproximados:
        usr_res_ids = obj_usuario.busca_por_semelhanca(atrs_bus, False)

      if len(usr_res_ids) == 0:
        # Não encontrou nenhum usuário:
        erros.append("Não foi encontrado nenhum usuário com os dados fornecidos")
    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(usr_res_ids) != 0:
    # Encontrou pelo menos um usuário.  Mostra em forma de tabela:
    ht_titulo = ht_titulo = html_bloco_titulo.gera("Usuários encontrados")
    ht_tabela = html_bloco_lista_de_usuarios.gera(usr_res_ids)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Não encontrou nenhum usuário.
    # Repete a página de busca, com eventuais mensagens de erro:
    pag = html_pag_buscar_usuarios.gera(ses, atrs_bus, erros)

  return pag

