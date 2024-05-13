import obj_sessao
import obj_video
import obj_usuario
import html_pag_generica
import html_pag_alterar_video
from util_erros import ErroAtrib

def processa(ses, cmd_args):
  
  # Estas condições devem valer para comandos emitidos por páginas do sistema:
  assert ses != None and obj_sessao.aberta(ses), "Sessão inválida"
  assert isinstance(cmd_args, dict), "argumentos inválidos para o comando"
  
  cmd_args = cmd_args.copy() # Por via das dúvidas.
  erros = []
  
  # Obtem o dono da sessão corrente:
  usr_ses = obj_sessao.obtem_dono(ses)
  assert usr_ses is not None
  para_admin = obj_usuario.eh_administrador(usr_ses)

  # Obtém o vídeo {vid} a alterar, e elimina 'video' de {cmd_args}:
  vid_id = cmd_args.pop('video', None)
  if vid_id != None:
    vid = obj_video.obtem_objeto(vid_id)
    if vid == None:
      erros.append(f"Vídeo {vid_id} não existe")
  else
    erros.append("Vídeo não foi especificado")
    vid = None
  
  if vid != None:
    # Obtém atributos correntes do video {vid}:
    vid_atrs = obj_video.obtem_atributos(vid) if vid != None else None

    # Elimina campos de {cmd_args} cujo valor não vai mudar: 
    util_dict.elimina_alteracoes_nulas(cmd_args, vid_atrs)

    # Confere se não há chaves espúrias em {cmd_args}
    util_dict.verifica_chaves_espurias(cmd_args, vid_atrs)

    # Verifica se o usuário corrente {usr_ses} pode alterar este vídeo:
    autor = obj_video.obtem_autor(vid)
    if usr_ses != autor and not para_admin:
      erros.append("Você não tem permissão para alterar dados deste vídeo")
  
    # Verifica campos inalteráveis:
    alteraveis = { 'nota', 'titulo' }
    for chave in cmd_args.keys():
      if not chave in alteraveis:
        erros.append(f"atributo {chave} não pode ser alterado")

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
      sys.stderr.write(f"@#@ ex = {str(ex)}\n")
      erros += ex.args[0]

  if pag == None:
    # Rep a página de alterar vídeo, mais as mens de erro:
    pag = html_pag_alterar_video.gera(ses, vid_id, cmd_args, erros)

  return pag
