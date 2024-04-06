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
  erros = [].copy()
  if ses == None or not obj_sessao.aberta(ses):
    erros.append("Precisa estar logado para executar esta função")
    vid = None
  else:
    # O autor do vídeo será sempre o dono da sessão:
    autor = obj_sessao.obtem_usuario(ses)
    id_autor = obj_usuario.obtem_identificador(autor)
    
    # Por via das dúvidas:
    if 'id_usuario' in cmd_args: assert id_autor == cmd_args['id_usuario']
    if 'id_autor' in cmd_args: assert id_autor == cmd_args['id_autor']
    
    # Nome do arquivo:
    arq = cmd_args['arq'] if 'arq' in cmd_args else None
    
    # Título:
    titulo = cmd_args['titulo'] if 'titulo' in cmd_args else None 

    # Cria data no formato ISO (aaaa-mm-dd hh:mm:ss fuso).
    data = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

    # Registra na tabela de vídeos e cria o objeto:
    atrs = {
      'autor': autor,             # {obj_usuario.Classe} o usuário que fez upload do vídeo.
      'arq': arq,                 # {str} nome do arquivo de vídeo.
      'titulo': titulo,           # {str} título do vídeo (max 60 caracteres)
      'data': data,               # data de upload, no formato ISO (aaaa-mm-dd hh:mm:ss fuso).
      'duracao': 0,               # duração do vídeo em millissegundos.
      'largura': 0,               # largura de cada frame, em pixels.
      'altura': 0                 # altura de cada frame, em pixels.
    }

    vid = obj_video.cria(atrs)

    # Grava o conteudo do arquivo no disco:
    wr = open("videos/" + arq, 'wb')

    wr.write(vid)
    
    wr.close()  

    # Insere objeto video na tabela `video`.
    db_base_sql.executa_comando_INSERT('video', vid)
    
  if vid != None:
    pag = html_pag_ver_video.gera(ses, vid, erros)
  else:
    pag = html_pag_mensagem_de_erro.gera(None, erros)

  return pag
