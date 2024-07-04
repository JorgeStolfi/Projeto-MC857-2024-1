import obj_sessao
import obj_video
import obj_usuario
import html_pag_generica
import html_pag_alterar_video
import html_pag_ver_video
import html_pag_mensagem_de_erro
import util_dict
from util_erros import ErroAtrib

import sys

def processa(ses, cmd_args):
  
  # Estas condições devem valer para comandos emitidos por páginas do sistema:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)
  
  cmd_args = cmd_args.copy() # Por via das dúvidas.
  erros = []
  
  # Obtem o dono da sessão corrente:
  ses_dono = None
  para_admin = False
  if ses == None:
    erros.append("É preciso estar logado para executar esta ação.")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta ação.")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono is not None
    para_admin = obj_usuario.eh_administrador(ses_dono)

  # Obtém o vídeo {vid} a alterar, e elimina 'video' de {cmd_args}:
  vid_id = cmd_args.pop('video', None)
  if vid_id != None:
    vid = obj_video.obtem_objeto(vid_id[0])
    if vid == None:
      erros.append(f"O vídeo \"{vid_id}\" não existe")
  else:
    erros.append("O vídeo a alterar não foi especificado")
    vid = None
  
  if vid != None:
    # Obtém atributos correntes do video {vid}:
    vid_atrs = obj_video.obtem_atributos(vid) if vid != None else None

    # Se um vídeo está bloqueado então não é possível editá-lo se não for administrador.
    if 'bloqueado' in vid_atrs and vid_atrs['bloqueado'] and not para_admin:
      erros.append("Este vídeo está bloqueado, não é possível editá-lo.")

    # Elimina campos de {cmd_args} cujo valor não vai mudar: 
    util_dict.elimina_alteracoes_nulas(cmd_args, vid_atrs)

    # Verifica se o usuário corrente {ses_dono} pode alterar este vídeo:
    autor = obj_video.obtem_autor(vid)
    assert autor != None
    if ses_dono == None or (ses_dono != autor and not para_admin):
      erros.append("Você não tem permissão para alterar dados deste vídeo")
  
    # Verifica campos alteráveis:
    alteraveis = { 'titulo', 'nota', }
    #o campo 'bloqueado' só é alterável para quem é administrador.
    if 'bloqueado' in cmd_args:
      if para_admin:
        alteraveis.add('bloqueado')
        cmd_args['bloqueado'] = True if cmd_args['bloqueado'] == 'on' else False
      else:
        erros.append("Este vídeo está bloqueado, não é possível editá-lo.")

    for chave in cmd_args.keys():
      if not chave in alteraveis:
        erros.append(f"O atributo '{chave}' não pode ser alterado")

    if 'nota' in cmd_args:
      # Somente administrador pode alterar a nota:
      if not para_admin:
        erros.append("Você não tem permissão para alterar a nota do vídeo")
  
  pag = None
  if (len(erros) == 0):
    # Tenta modificar os atributos do vídeo:
    try:
      atrs_mod = util_dict.para_objetos(cmd_args)
      obj_video.muda_atributos(vid, atrs_mod)
      # Sucesso. Exibimos o vídeo com os dados alterados:
      pag = html_pag_ver_video.gera(ses, vid, erros)
    except ErroAtrib as ex:
      # sys.stderr.write(f"@#@ ex = {str(ex)}\n")
      erros += ex.args[0]

  if pag == None:
    if ses_dono == None or vid_id == None:
      # Não vale a pena repetir o formulário:
      pag = html_pag_mensagem_de_erro.gera(ses, erros)
    else:
      # Repete a página de alterar vídeo, mais as mens de erro:
      pag = html_pag_alterar_video.gera(ses, vid_id, cmd_args, erros)

  return pag
