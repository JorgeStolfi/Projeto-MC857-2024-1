import html_pag_alterar_comentario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_comentario
from util_erros import erro_prog

def _usuario_pode_acessar_comentario(ses, id_com):
  usuario_eh_admin = obj_sessao.de_administrador(ses)
  usuario_eh_autor_do_comentario = obj_sessao.obtem_identificador(ses) == obj_comentario.busca_por_identificador(id_com)
  return usuario_eh_admin or usuario_eh_autor_do_comentario

def processa(ses, cmd_args):
  erros = [ ].copy()
  id_com = cmd_args['comentario'] if 'comentario' in cmd_args else None
  
  # Valida a sessão do usuário
  if (ses == None or not obj_sessao.aberta(ses)):
    erros.append("Sessão inválida!")
  else:
    # Valida se o comentário é informado para acessar a página
    if (id_com == None):
      erros.append("Um comentário deve ser especificado!")
    # Valida se o comentário existe
    elif (obj_comentario.busca_por_identificador(id_com) == None):
      erros.append("O comentário não existe!")
    # Valida se o usuário tem permissões para editar o comentário
    elif (not _usuario_pode_acessar_comentario(ses, id_com)):
      erros.append("O usuário não pode editar esse comentário!")
  
  if len(erros) > 0:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    comentario_classe = obj_comentario.obtem_atributos(obj_comentario.busca_por_identificador(id_com))
    dados_comentario_atual = {
      'video': comentario_classe['video'],
      'autor': comentario_classe['autor'],
      'data': comentario_classe['data'],
      'texto': comentario_classe['texto'],
      'pai': comentario_classe['pai'],
    }
    pag = html_pag_alterar_comentario.gera(ses, id_com, dados_comentario_atual, None)
  return pag
    
