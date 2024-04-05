# Implementação do módulo {comando_fazer_upload_video}.

# Interfaces do projeto usadas por esta implementação:
import obj_usuario
import obj_sessao
import obj_video
import html_pag_mensagem_de_erro
import html_pag_principal
import db_base_sql
import datetime

# Outros módulos usados por esta implementação:
import secrets

def processa(ses, dados):
  erros = [ "!!! {comando_fazer_upload_video} ainda não foi implementado !!!" ]
  pag = html_pag_mensagem_de_erro.gera(None, erros)
  
  # Cria data no formato ISO (aaaa-mm-dd hh:mm:ss fuso).
  data = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

  dados_do_video = {
    'usr': ses.usr,             # {obj_usuario.Classe} o usuário que fez upload do vídeo.
    'arq': dados['arq'],        # {str} nome do arquivo de vídeo.
    'titulo': dados['titulo'],  # {str} título do vídeo (max 60 caracteres).
    'data': data,               # data de upload, no formato ISO (aaaa-mm-dd hh:mm:ss fuso).
    'duracao': 0,               # duração do vídeo em millissegundos.
    'largura': 0,               # largura de cada frame, em pixels.
    'altura': 0                 # altura de cada frame, em pixels.
  }

  # Cria objeto de video para inserir no banco de dados.
  video = obj_video.cria(dados_do_video)

  # Insere objeto video na tabela `video`.
  db_base_sql.executa_comando_INSERT('video', video)

  return pag
