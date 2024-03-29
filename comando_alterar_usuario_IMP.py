# Implementação do módulo {comando_alterar_usuario}.

import html_pag_login
import html_pag_mensagem_de_erro
import html_pag_alterar_usuario
import obj_usuario
import obj_sessao
from util_valida_campo import ErroAtrib

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):
  cmd_args = cmd_args.copy() # Por via das dúvidas.
  erros = [].copy()
  
  # Determina se o usuário corrente {usr_ses} é administrador:
  if ses is None or not obj_sessao.aberta(ses):
    erros.append("sessão inativa")
    admin = False
    usr_ses = None
    usr = None
    id_usr = None
  else:
    usr_ses = obj_sessao.obtem_usuario(ses)
    assert usr_ses is not None
    admin = obj_usuario.obtem_atributos(usr_ses)['administrador']
    
    # Determina o usuário {usr} a alterar:
    if 'id_usuario' in cmd_args:
      id_usr = cmd_args['id_usuario']
      cmd_args.pop('id_usuario')
      usr = obj_usuario.busca_por_identificador(id_usr)
      if usr == None:
        erros.append(f"usuario {id_usr} não existe")
    else:
      usr = usr_ses
      assert usr is not None
      id_usr = obj_usuario.obtem_identificador(usr)  
  
    # Se desejarmos atualizar o email, validamos se o mesmo não é duplicado:
    if 'email' in cmd_args:
      novo_email = cmd_args['email']
      id_usuario_com_email_atual = obj_usuario.busca_por_email(novo_email)
      # Se o usuário atual deseja alterar o seu email para o mesmo que ele já usa, permitimos também
      if (id_usuario_com_email_atual != None and id_usuario_com_email_atual != id_usr):
        erros.append(f"já existe um usuário com o email {novo_email}")

  if len(erros) == 0:
    # Tenta editar o usuário:
    try:
      obj_usuario.confere_e_elimina_conf_senha(cmd_args)
      obj_usuario.muda_atributos(usr, cmd_args)
    except ErroAtrib as ex:
      erros.append(ex.args[0])
      
  if usr_ses == None:
    # Sessão inativa: mostra página de erro:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  elif len(erros) == 0:
    # Mostra de novo a página de alterar mas com dados alterados:
    cmd_args_novos = obj_usuario.obtem_atributos(usr)
    pag = html_pag_alterar_usuario.gera(ses, id_usr, cmd_args_novos, admin, None)
  else:
    # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_usuario.gera(ses, id_usr, cmd_args, admin, erros)
  return pag
