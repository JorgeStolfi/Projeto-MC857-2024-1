# Implementação do módulo {comando_fazer_upload_video}.

# Interfaces do projeto usadas por esta implementação:
import obj_usuario
import obj_sessao
import obj_video
import html_pag_mensagem_de_erro
import html_pag_principal
import html_pag_ver_video
import db_base_sql
import datetime

def processa(ses, cmd_args):
  # Estas condições deveriam valer para comandos gerados
  # pelas páginas do site:
  assert ses != None and obj_sessao.aberta(ses), "Sessao inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = []
  
  # O autor do vídeo será sempre o dono da sessão:
  autor = obj_sessao.obtem_dono(ses)
  autor_id = obj_usuario.obtem_identificador(autor)

  # Estas condições também deveriam valer para comandos gerados pelo site:
  if 'usuario' in cmd_args: assert cmd_args['usuario'] == autor_id
  if 'autor' in cmd_args: assert cmd_args['autor'] == autor_id

  if 'titulo' in cmd_args:
    titulo = cmd_args['titulo']
  else:
    erros.append("Precisa definir o título do video") 
    titulo = None
    
  # Pega o conteúdo do arquivo:
  if 'arquivo' in cmd_args:
    conteudo = cmd_args['arquivo']
  else:
    erros.append("Bytes do vídeo não foram enviados") 
    conteudo = None

  # Salva o arquivo, cria o objeto, e registra na tabela de vídeos:
  atrs = {
    'autor': autor,
    'titulo': titulo,
    'conteudo': conteudo
  }
  vid = obj_video.cria(atrs)
    
  if vid != None:
    pag = html_pag_ver_video.gera(ses, vid, erros)
  else:
    pag = html_pag_upload_video.gera(ses, atrs, erros)

  return pag
