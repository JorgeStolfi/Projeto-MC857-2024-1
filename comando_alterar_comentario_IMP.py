import obj_sessao
import obj_comentario
import html_pag_generica
import html_pag_alterar_comentario
import obj_usuario
import html_pag_mensagem_de_erro
import html_pag_ver_comentario
import obj_video
import util_dict
from util_erros import ErroAtrib

import sys

caco_debug = False  # Deve imprimir mensagens para depuração?

def msg_campo_obrigatorio(nome_do_campo):
  return "O campo %s é obrigatório." % nome_do_campo

def processa(ses, cmd_args):

  # Estas condições deveriam ser garantidas para comandos emitidos
  # pelas páginas do sistema:
  assert ses != None and isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  cmd_args = cmd_args.copy() # Para não alterar o original.
  erros = [] # Mensagens de erro.

  if obj_sessao.aberta(ses):
    # Obtem o dono da sessão corrente:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono is not None
    para_admin = obj_usuario.eh_administrador(ses_dono)
  else:
    erros.append("Esta sessão de login foi fechada. Precisa estar logado para executar este comando")
    ses_dono = None
    para_admin = False

  # Obtém o comentário {com} a alterar, e elimina 'comentario' de {cmd_args}:
  com_id = cmd_args.pop('comentario', None)
  if com_id != None:
    com = obj_comentario.obtem_objeto(com_id)
    if com == None:
      erros.append(f"O comentário \"{com_id}\" não existe")
  else:
    erros.append("O comentário a alterar não foi especificado")
    com = None
  
  if com != None:
    # Obtém atributos correntes do comentario {com}:
    com_atrs = util_dict.para_identificadores(obj_comentario.obtem_atributos(com))
    util_dict.elimina_alteracoes_nulas(cmd_args, com_atrs)
    assert set(cmd_args.keys()) <= set(com_atrs.keys()), "Argumentos espúrios"

  if len(erros) == 0:
    # Verifica se o usuário corrente {ses_dono} pode alterar este comentário:
    autor = com_atrs['autor']
    editavel = para_admin or autor == ses_dono
    if not editavel:
      erros.append(f"Você não tem permissão para alterar este comentário")

    # Verifica campos inalteráveis:
    alteraveis = { 'texto', 'nota', 'voto', }
    for chave in cmd_args.keys():
      if not chave in alteraveis:
        erros.append(f"O atributo '{chave}' não pode ser alterado")

    if 'nota' in cmd_args:
      # Somente administrador pode alterar a nota:
      if not para_admin:
        erros.append("Você não tem permissão para alterar a nota do comentário")

    if 'voto' in cmd_args:
      # Somente administrador ou o dono do comentário pode altera-lo
      if not editavel:
        erros.append("Você não tem permissão para alterar o voto do comentário") 

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
      # sys.stderr.write(f"@#@ ex = {str(ex)}\n")
      erros += ex.args[0]
  else:
    if caco_debug: sys.stderr.write("    NÃO chamou {obj_comentario.muda_atributos}\n")

  if pag == None:
    # Repete a página de alterar comentário com os mesmos argumentos, mais as mens de erro:
    pag = html_pag_alterar_comentario.gera(ses, com, cmd_args, erros)

  return pag
