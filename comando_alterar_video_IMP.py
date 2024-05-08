import obj_sessao
import obj_video
import obj_usuario
import html_pag_generica
import html_pag_alterar_video
from util_erros import ErroAtrib

def _usuario_pode_editar_video(ses, id_video):
  usuario_eh_admin = obj_sessao.de_administrador(ses)
  id_user = obj_usuario.obtem_identificador(obj_sessao.obtem_usuario(ses))
  usuario_eh_autor_do_video = id_video in obj_video.busca_por_autor(id_user)
  return usuario_eh_admin or usuario_eh_autor_do_video

def _busca_cmd_args(campo, cmd_args):
  return cmd_args[campo] if campo in cmd_args else None

def processa(ses, cmd_args):
  erros = [].copy()
  
  dados_video = {
    'autor': _busca_cmd_args('autor', cmd_args),
    'titulo': _busca_cmd_args('titulo', cmd_args),
    'data': _busca_cmd_args('data', cmd_args), 
  }
  
  id_video = _busca_cmd_args('video', cmd_args)
  ht_bloco = ''
  
  # Valida se a sessão é válida
  if (ses == None or not obj_sessao.aberta(ses)):
    erros.append("Sessão inválida!")
  # Valida se o identificador do vídeo foi enviado
  elif (id_video == None):
    erros.append("Um vídeo deve ser informado!")
  # Valida se o usuário pode editar o vídeo
  elif (not _usuario_pode_editar_video(ses, id_video)):
    erros.append("O usuário não tem permissão para editar esse vídeo!")
  
  if (len(erros) > 0):
    # Não permitimos a alteração do vídeo!
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    # Alteração do vídeo permitida
    video = obj_video.obtem_objeto(id_video)
    # Em caso de algum erro, mostramos a página de html_form_alterar_video novamente com o erro
    try:
      obj_video.muda_atributos(video, dados_video)
      # Vídeo alterado com sucesso... Exibimos a tela de alterar vídeo com os dados alterados novamente
      return html_pag_alterar_video.gera(ses, id_video, dados_video, erros)
    except ErroAtrib as ex:
      # Ocorreu um erro ao alterar o vídeo!
      erros = ex.args[0]
      ht_bloco = html_pag_alterar_video.gera(ses, id_video, dados_video, erros)
      return html_pag_generica.gera(ses, ht_bloco, erros)
    except Exception as ex:
      erros.append('Não foi possível alterar o vídeo!')
      return html_pag_generica.gera(ses, ht_bloco, erros)

  return pag
