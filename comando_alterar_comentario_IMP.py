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

  cmd_args = cmd_args.copy() # Para não alterar o original.
  erros = [] # Mensagens de erro.

  # Obtem o dono da sessão corrente:
  usr_ses = obj_sessao.obtem_dono(ses)
  assert usr_ses is not None
  para_admin = obj_usuario.eh_administrador(usr_ses)

  # Obtém o comentário {com} a alterar, e elimina 'comentario' de {cmd_args}:
  com_id = cmd_args.pop('comentario', None)
  if com_id != None:
    com = obj_comentario.obtem_objeto(com_id)
    if com == None:
      erros.append(f"Comentário {com_id} não existe")
  else
    erros.append("Comentário não foi especificado")
    com = None
  
  if com != None:
    # Obtém atributos correntes do comentario {com}:
    com_atrs = obj_comentario.obtem_atributos(com)

    # Elimina campos de {cmd_args} cujo valor não vai mudar: 
    util_dict.elimina_alteracoes_nulas(cmd_args, com_atrs)

    # Confere se não há chaves espúrias em {cmd_args}
    util_dict.verifica_chaves_espurias(cmd_args, com_atrs)

    # Verifica se o usuário corrente {usr_ses} pode alterar este comentário:
    autor = obj_comentario.obtem_atributo(com, 'autor')
    if usr_ses != autor and not para_admin:
      erros.append("Você não tem permissão para alterar dados deste comentário")

    autor = com_atrs['autor']
    if not (para_admin or autor == usr_ses):
      erros.append(f"Você não tem permissão para alterar este comentário")

    # Verifica campos inalteráveis:
    alteraveis = { 'texto' }
    for chave in cmd_args.keys():
      if not chave in alteraveis:
        erros.append(f"atributo {chave} não pode ser alterado")

  pag = None
  if (len(erros) == 0):
    # Tenta modificar os atributos do vídeo:
    atrs_mod = util_dict.para_objetos(cmd_args)
    if caco_debug: sys.stderr.write("    chamando {obj_comentario.muda_atributos}...\n")
    try:
      obj_comentario.muda_atributos(com, atrs_mod)
      if caco_debug: sys.stderr.write("    chamada retornou normalmente\n")
      # Sucesso. Exibimos o vídeo com os dados alterados:
      pag = html_pag_ver_comentario.gera(ses, com, erros)
    except ErroAtrib as ex:
      sys.stderr.write(f"@#@ ex = {str(ex)}\n")
      erros += ex.args[0]
  else:
    if caco_debug: sys.stderr.write("    NÃO chamou {obj_comentario.muda_atributos}\n")
      
  if pag == None:
    # Repete a página de alterar comentário com os mesmos argumentos, mais as mens de erro:
    pag = html_pag_alterar_comentario.gera(ses, com_id, cmd_args, erros)

  return pag
