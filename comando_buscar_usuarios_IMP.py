# Implementação do módulo {comando_buscar_usuarios}.

import obj_usuario
import obj_sessao
import html_bloco_lista_de_usuarios
import html_pag_generica
import html_pag_buscar_usuarios

from util_valida_campo import ErroAtrib

def processa(ses, cmd_args):
  try:
    # Campos que podem ser usados na busca:
    campos_busc = ['id_usr', 'email', 'nome']

    # Garante que existe pelo menos um campo:
    if not verifica_pelo_menos_um_campo(campos_busc, cmd_args):
      raise ErroAtrib(f"Pelo menos um dos campos {str(campos_busc)} precisa estar preenchido")

    id_usr = None
    lista_ids_usr = [].copy()
    if 'id_usr' in cmd_args:
      # Deve haver um único usuário com esse identificador:
      obj_usr = obj_usuario.busca_por_identificador(cmd_args['id_usr'])
      id_usr = obj_usuario.obtem_identificador(obj_usr)
    elif 'email' in cmd_args:
      # Deve haver um único usuário com esse email
      id_usr = obj_usuario.busca_por_email(cmd_args['email'])
    elif 'nome' in cmd_args:
      # Pode haver vários usuários com este nome
      lista_ids_usr = obj_usuario.busca_por_nome(cmd_args['nome'])
 
    if id_usr != None:
      lista_ids_usr.append(id_usr)
      is_usr = None
 
    if len(lista_ids_usr) == 0:
      raise ErroAtrib("Não foi encontrado um usuário com os dados fornecidos")

    bloco = html_bloco_lista_de_usuarios.gera(lista_ids_usr)
    pag = html_pag_generica.gera(ses, bloco, None)
    return pag

  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página com mensagem de erro:
    pag = html_pag_buscar_usuarios.gera(ses, ex.args, obj_sessao.eh_administrador(ses), erros)
    return pag

def verifica_pelo_menos_um_campo(campos_busc, cmd_args):
  """ Garante que pelo menos um campo da lista {campos_busc}
  está definido em {cmd_args} com valor diferente de {None}
  ou ""."""

  tem_campo = False
  for chave in campos_busc:
    if chave in cmd_args and cmd_args[chave] is not None and cmd_args[chave] != "":
      tem_campo = True
  return tem_campo

