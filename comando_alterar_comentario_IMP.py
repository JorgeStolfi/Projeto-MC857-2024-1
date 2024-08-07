import obj_sessao
import obj_comentario
import html_pag_generica
import html_pag_alterar_comentario
import obj_usuario
import html_pag_mensagem_de_erro
import html_pag_ver_comentario
import obj_video
import util_dict
import util_nota
import util_voto
from util_erros import ErroAtrib

import sys

caco_debug = False  # Deve imprimir mensagens para depuração?

def processa(ses, cmd_args_original):

  # Estas condições deveriam ser garantidas para comandos emitidos
  # pelas páginas do sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args_original, dict)

  cmd_args = cmd_args_original.copy() # Para não alterar o original.
  erros = [] # Mensagens de erro.
  
  ses_dono = None
  if ses == None:
    erros.append("É preciso estar logado para executar este comando")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar este comando")
  else: 
    # Obtem o dono da sessão corrente:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono is not None

  para_admin = obj_usuario.eh_administrador(ses_dono) if ses_dono != None else False

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
    assert ses_dono != None
    assert com != None
    # Verifica se o usuário corrente {ses_dono} pode alterar este comentário:
    autor = com_atrs['autor']
    assert autor != None
    bloqueado = com_atrs['bloqueado']
    editavel = para_admin or (autor == ses_dono and not bloqueado)
    if not editavel:
      erros.append(f"Você não tem permissão para alterar este comentário")

    # Verifica campos inalteráveis:
    alteraveis = { 'texto', 'nota', 'voto', 'bloqueado'}
    for chave in cmd_args.keys():
      if not chave in alteraveis:
        erros.append(f"O atributo '{chave}' não pode ser alterado")   #aqui está a mensagem
    if 'nota' in cmd_args:
      # Somente administrador pode alterar a nota:
      if not para_admin:
        erros.append("Você não tem permissão para alterar a nota do comentário")
        
    if 'voto' in cmd_args:
      # Somente administrador ou o dono do comentário pode altera-lo
      if not editavel:
        erros.append("Você não tem permissão para alterar o voto do comentário")
    if 'bloqueado' in cmd_args:
        if not editavel:
          erros.append("Você não pode desbloquear esse comentário")
    
  pag = None
  if (len(erros) == 0):
    # Tenta modificar os atributos do vídeo:
    atrs_mod = util_dict.para_objetos(cmd_args)
    if 'nota' in atrs_mod:
      erros+= util_nota.valida('nota', atrs_mod['nota'], False)
      if len(erros) == 0:
        atrs_mod['nota'] = float(atrs_mod['nota'])
    if 'voto' in atrs_mod:
      erros+= util_voto.valida('voto', atrs_mod['voto'], False)
      if len(erros) == 0:
        atrs_mod['voto'] = int(atrs_mod['voto'])
    if 'bloqueado' in atrs_mod:
      if len(erros) == 0:
        if(atrs_mod['bloqueado'] == 'True'):
          atrs_mod['bloqueado'] = True
        else:
          atrs_mod['bloqueado'] = False
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
    pag = html_pag_alterar_comentario.gera(ses, com, cmd_args_original, erros)

  return pag
