import obj_sessao
import obj_comentario
import html_pag_generica
import html_pag_alterar_comentario
import obj_usuario #adicionado
import html_pag_mensagem_de_erro #adicionado
import html_pag_ver_comentario #adicionado
import obj_video #adicionado
from util_erros import ErroAtrib

import sys

caco_debug = False  # Deve imprimir mensagens para depuração?

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):

  # Estas condições deveriam ser garantidas para comandos emitidos
  # pelas páginas do sistema:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert isinstance(cmd_args, dict), "Argumentos do comando inválidos"
  assert 'comentario' in cmd_args, "Comentario a editar não especificado"

  erros = [].copy() # Mensagens de erro.
  atrs_mod = {}.copy()  # Atributos a modificar.
  cmd_args = cmd_args.copy() # Para não alterar o original.

  usr_ses = obj_sessao.obtem_usuario(ses)
  assert usr_ses is not None
  ses_admin = obj_usuario.obtem_atributos(usr_ses)['administrador']
  usr_ses_id = obj_usuario.obtem_identificador(usr_ses)

  # Determina o comentário {com} a alterar:
  id_com = cmd_args['comentario']
  cmd_args.pop('comentario')
  com = obj_comentario.obtem_objeto(id_com)
  if com == None:
    erros.append(f"comentario {id_com} não existe")
  else:
    # Atributos atuais do comentério:
    atrs_atu = obj_comentario.obtem_atributos(com)

    autor = atrs_atu['autor']
    if not (ses_admin or autor == usr_ses):
      erros.append(f"Você não tem permissão para alterar este comentário")
    else:
      # Conjunto de atributos que PODEM ser alterados:
      atrs_mod_ok = { 'texto', }

      for chave, val_atu in atrs_atu.items():
        val_cmd = cmd_args[chave] if chave in cmd_args else None
        if val_cmd != None:
          # Converte identificador em {cmd_args} para objeto:
          if chave == 'autor':
            val_cmd = obj_usuario.obtem_objeto(val_cmd)
          elif chave == 'video':
            val_cmd = obj_video.obtem_objeto(val_cmd)
          elif chave == 'pai':
            val_cmd = obj_comentario.obtem_objeto(val_cmd)
            
          if val_cmd == val_atu:
            # Atributo não está sendo modificado:
            pass
          elif chave in atrs_mod_ok:
            # Atributo está sendo modificado e é modificável:
            atrs_mod[chave] = val_cmd
          else:
            # Tentativa de modifcar atributo não modificável:
            erros.append(f"Não é possível alterar o atributo {chave} do comentário")
  
  if len(erros) == 0:
    # Tenta editar o comentario:
    if caco_debug: sys.stderr.write("    chamando {obj_comentario.muda_atributos}...\n")
    try:
      obj_comentario.muda_atributos(com, atrs_mod)
      if caco_debug: sys.stderr.write("    chamada retornou normalmente\n")
    except ErroAtrib as ex:
      erros += ex.args[0]
  else:
    if caco_debug: sys.stderr.write("    NÃO chamou {obj_comentario.muda_atributos}\n")
      
  if len(erros) == 0:
    # Mostra comentário com dados alterados:
    pag = html_pag_ver_comentario.gera(ses, com, None)
  else:
    # Repete a página de alterar comentário com os mesmos argumentos e mens de erro:
    pag = html_pag_alterar_comentario.gera(ses, id_com, cmd_args, erros)
  return pag
