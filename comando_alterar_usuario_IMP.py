# Implementação do módulo {comando_alterar_usuario}.

import html_pag_login
import html_pag_mensagem_de_erro
import html_pag_ver_usuario
import html_pag_alterar_usuario
import obj_usuario
import obj_sessao
import util_dict
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  
  # Estas condições devem valer para comandos emitidos por páginas do sistema:
  assert ses != None and isinstance(ses, obj_sessao.Classe), "sessão inválida"
  assert isinstance(cmd_args, dict), "argumentos inválidos para o comando"
  
  cmd_args = cmd_args.copy() # Por via das dúvidas.
  erros = []
  
  if obj_sessao.aberta(ses):
    # Obtem o dono da sessão corrente:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    para_admin = obj_usuario.eh_administrador(ses_dono)
  else:
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta ação.")
    ses_dono = None
    para_admin = False

  # Determina o usuário {usr} a alterar, e elimina 'usuario' de {cmd_args}:
  if 'usuario' in cmd_args:
    usr_id = cmd_args.pop('usuario')
    usr = obj_usuario.obtem_objeto(usr_id)
    if usr == None:
      erros.append(f"O usuário \"{usr_id}\" não existe")
  elif ses_dono != None:
    usr = ses_dono
    usr_id = obj_usuario.obtem_identificador(usr)  
  else:
    usr = None
    usr_id = None
  
  if usr != None:
    erros += obj_usuario.confere_e_elimina_conf_senha(cmd_args)
  
    # Obtém atributos correntes do usuário {usr}:
    usr_atrs = obj_usuario.obtem_atributos(usr)

    # Elimina campos de {cmd_args} cujo valor não vai mudar: 
    util_dict.elimina_alteracoes_nulas(cmd_args, usr_atrs)

    # Determina se o usuário corrente {ses_dono} pode alterar {usr}:
    if ses_dono == None or ( usr != ses_dono and not para_admin ):
      erros.append("Você não tem permissão para alterar dados deste usuário")
  
    # Verifica campos inalteráveis:
    alteraveis = { 'nome', 'email', 'administrador', 'senha' }
    for chave in cmd_args.keys():
      if not chave in alteraveis:
        erros.append(f"O atributo '{chave}' não pode ser alterado")

    if 'administrador' in cmd_args:
      # Só um administardor pode mudar o estado de 'administrador':
      if not para_admin:
        erros.append("Você não tem permissão para alterar o atributo 'administrador'")

    if 'email' in cmd_args:
      # Se email vai mudar, garante que novo email não está em uso:
      email_novo = cmd_args['email']
      assert email_novo != usr_atrs['email']
      email_usr_id = obj_usuario.busca_por_email(email_novo)
      if email_usr_id != None:
        erros.append(f"Já existe um usuário com o email \"{email_novo}\"")

  pag = None
  if len(erros) == 0:
    # Tenta modificar os atributos do usuário:
    try:
      # Por via das dúvidas:
      atrs_mod = util_dict.para_objetos(cmd_args)
      obj_usuario.muda_atributos(usr, atrs_mod)
      # Sucesso. Exibimos o usuário com os dados alterados:
      pag = html_pag_ver_usuario.gera(ses, usr, erros)
    except ErroAtrib as ex:
      # sys.stderr.write(f"@#@ ex = {str(ex)}\n")
      erros += ex.args[0]
      
  if pag == None:
    # Repete a página de alterar usuário com os mesmos argumentos, mais as mens de erro:
    cmd_args.pop('senha', None)
    cmd_args.pop('conf_senha', None)
    pag = html_pag_alterar_usuario.gera(ses, usr_id, cmd_args, erros)

  return pag
