import obj_sessao
import obj_comentario
import html_pag_generica
import html_pag_alterar_comentario
import obj_usuario #adicionado
import html_pag_mensagem_de_erro #adicionado
import html_pag_ver_comentario #adicionado
import obj_video #adicionado
from util_erros import ErroAtrib

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):

  # Estas condições deveriam ser garantidas para comandos emitidos
  # pelas páginas do sistema:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert isinstance(cmd_args, dict), "Argumentos do comando inválidos"
  assert 'comentario' in cmd_args, "Comentario a editar não especificado"

  atrs_mod = cmd_args.copy() # Por via das dúvidas.
  erros = [].copy()

  usr_ses = obj_sessao.obtem_usuario(ses)
  assert usr_ses is not None
  ses_admin = obj_usuario.obtem_atributos(usr_ses)['administrador']
  usr_ses_id = obj_usuario.obtem_identificador(usr_ses)

  # Determina o comentário {com} a alterar:
  id_com = atrs_mod['comentario']
  atrs_mod.pop('comentario')
  com = obj_comentario.busca_por_identificador(id_com)
  if com == None:
    erros.append(f"comentario {id_com} não existe")
  else:
    autor = obj_comentario.obtem_atributo(com, 'autor')
    autor_id = obj_usuario.obtem_identificador(autor)

    if not (ses_admin or autor == usr_ses):
      erros.append(f"Você não tem permissão para alterar este comentário")
    
    # Verificando se há tentativa de alterar atributos que não podem ser alterados
    if 'autor' in atrs_mod:
      atrs_mod['autor'] = obj_usuario.busca_por_identificador(atrs_mod['autor']) # Converter ID para obj_usuario
      if atrs_mod['autor'] != autor:
        erros.append(f"Não é possível alterar o autor do comentário")
  
    if 'video' in atrs_mod:
      atrs_mod['video'] = obj_video.busca_por_identificador(atrs_mod['video']) # Converter ID para obj_video
      if atrs_mod['video'] != obj_comentario.obtem_atributo(com, 'video'):
        erros.append(f"Não é possível alterar o vídeo em que este comentário foi feito")
  
  if len(erros) == 0:
    # Tenta editar o comentario:
    try:
      obj_comentario.muda_atributos(com, atrs_mod)
    except ErroAtrib as ex:
      erros += ex.args[0]
      
  if len(erros) == 0:
    # Mostra comentário com dados alterados:
    pag = html_pag_ver_comentario.gera(ses, com, None)
  else:
    # Repete a página de alterar comentário com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_comentario.gera(ses, id_com, atrs_mod, erros)
  return pag
