# Implementação do módulo {comando_alterar_usuario}.

import html_pag_login
import html_pag_alterar_usuario
import obj_usuario
import obj_sessao
from util_valida_campo import ErroAtrib

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, args):
  args = args.copy() # Por via das dúvidas.

  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses is None:
    admin = False
  else:
    usr_ses = obj_sessao.obtem_usuario(ses)
    assert usr_ses is not None
    admin = obj_usuario.obtem_atributos(usr_ses)['administrador']

  id_usr = args["id_usuario"]
  assert id_usr is not None, "id_usuario obrigatório para atualizar"
  args.pop("id_usuario")

  # Tenta editar o usuário:
  try:
    obj_usuario.confere_e_elimina_conf_senha(args)
    usr = obj_usuario.busca_por_identificador(id_usr)

    obj_usuario.muda_atributos(usr, args)
    
    # Mostra de novo a página de alterar com dados novos:
    args_novos = obj_usuario.obtem_atributos(usr)
    pag = html_pag_alterar_usuario.gera(ses, id_usr, args_novos, admin, None)
  except ErroAtrib as ex:
    erros = ex.args[0]
    # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_usuario.gera(ses, id_usr, args, admin, erros)
  return pag
