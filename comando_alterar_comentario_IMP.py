import obj_sessao
import obj_comentario
import html_pag_generica
import html_pag_alterar_comentario
import obj_usuario #adicionado
import html_pag_mensagem_de_erro #adicionado
from util_erros import ErroAtrib


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
    
    # Determina o comentário {com} a alterar:
    if 'comentario' in cmd_args:
      id_com = cmd_args['comentario']
      cmd_args.pop('comentario')
      com = obj_comentario.busca_por_identificador(id_com)
      if com == None:
        erros.append(f"comentario {id_com} não existe")
    else:
      erros.append(f"comentario não encontrado")

  if len(erros) == 0:
    # Determina se é autor do comentário
    if obj_comentario.busca_por_autor(usr_ses) == None:
      erros.append(f"autor não encontrado")

  if len(erros) == 0:
    # Tenta editar o comentario:
    try:
      #obj_usuario.confere_e_elimina_conf_senha(cmd_args)
      obj_comentario.muda_atributos(com, cmd_args)
    except ErroAtrib as ex:
      erros.append(ex.args[0])
      
  if usr_ses == None:
    # Sessão inativa: mostra página de erro:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  elif len(erros) == 0:
    # Mostra de novo a página de alterar mas com dados alterados:
    cmd_args_novos = obj_comentario.obtem_atributos(usr)
    pag = html_pag_alterar_comentario.gera(ses, id_usr, cmd_args_novos, admin, None)
  else:
    # Repete a página de cadastrar com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_comentario.gera(ses, id_usr, cmd_args, admin, erros)
  return pag
