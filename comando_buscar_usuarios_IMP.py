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
  
  erros = [].copy()

  # Valida os valores dos atributos da busca, e elimina campos {None}:
  cmd_args_cp = cmd_args.copy()
  for chave, val in cmd_args.items():
    if val == None:
      del cmd_args_cp[chave]
    # Verifica validade de {val}:
    elif chave == 'usuario':
      erros += util_valida_campo.identificador(chave, val, "U", False)
    elif chave == 'email':
      # !!! Deveria aceitar email parcial, como "@unicamp.br" ou RE. !!!
      erros += util_valida_campo.email(chave, val, False)
    elif chave == 'nome':
      # !!! Devia aceitar nome parcial ou RE !!!
      erros += util_valida_campo.nome_de_usuario(chave, val, False)
    elif chave == 'administrador' or chave == 'senha':
      erros.append(f"Busca por '{chave}' não é permitida")
    else:
      # Comando emitido por página do site não deveria ter outros campos:
      assert False, f"Campo '{chave}' inválido"
  cmd_args = cmd_args_cp
  
  lista_ids_usr = [].copy()
  if len(erros) == 0:
  # Faz a busca dentro de um {try:} caso ela levante {ErroAtrib}:
    try:
      if 'usuario' in cmd_args:
        # Deve haver um único usuário com esse identificador:
        id_usr = cmd_args['usuario']
        obj_usr = obj_usuario.busca_por_identificador(id_usr) if id_usr != None else None
        if obj_usr == None:
          erros.append(f"Usuário '{id_usr}' não existe")
        else:
          lista_ids_usr = [ id_usr ]
      elif 'email' in cmd_args:
        # Deve haver um único usuário com esse email
        admin = obj_sessao.de_administrador(ses)
        if not admin:
          erros.append("Busca por email só é permitida para administradores")
        else:
          email = cmd_args['email']
          id_usr = obj_usuario.busca_por_email(email)
          if id_usr == None:
            erros.append(f"Não existe usuário com email '{email}'")
          else:
            lista_ids_usr = [ id_usr ]
      else:
        # Busca por campos aproximados:
        lista_ids_usr = obj_usuario.busca_por_semelhanca(cmd_args, False)

      if len(lista_ids_usr) == 0:
        # Não encontrou nenhum usuário:
        erros.append("Não foi encontrado nenhum usuário com os dados fornecidos")
    except ErroAtrib as ex:
      erros += ex.args[0]

  if len(lista_ids_usr) != 0:
    # Encontrou pelo menos um usuário.  Mostra em forma de tabela:
    ht_titulo = ht_titulo = html_bloco_titulo.gera("Usuários encontrados")
    ht_tabela = html_bloco_lista_de_usuarios.gera(lista_ids_usr)
    ht_bloco = \
      ht_titulo + "<br/>\n" + \
      ht_tabela
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Não encontrou nenhum usuário.
    # Repete a página de busca, com eventuais mensagens de erro:
    admin = obj_sessao.de_administrador(ses)
    pag = html_pag_buscar_usuarios.gera(ses, cmd_args, erros)

  return pag

