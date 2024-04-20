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
  assert ses == None or obj_sessao.aberta(ses), "Sessao inválida"
  assert type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = [].copy()
  
  if ses == None or not obj_sessao.aberta(ses):
    erros.append("Precisa estar logado para executar esta função")
    vid = None
  else:
    # O autor do vídeo será sempre o dono da sessão:
    autor = obj_sessao.obtem_usuario(ses)
    id_autor = obj_usuario.obtem_identificador(autor)
    
    # Por via das dúvidas:
    if 'usuario' in cmd_args: assert id_autor == cmd_args['usuario']
    if 'autor' in cmd_args: assert id_autor == cmd_args['autor']
    
    # Nome do arquivo:
    
    # Título:
    titulo = cmd_args['titulo'] if 'titulo' in cmd_args else None
    
    rd = open('videos/virus.mp4', 'rb')
    conteudo = rd.read()
    rd.close()
    # Grava o conteudo do arquivo no disco:
    wr = open("videos/" + 'teste.mp4', 'wb')
    # !!! Implementar o upload do arquivo {arq} e gravação no disco !!!
   
    
    wr.write(conteudo)

    wr.close()

    # Registra na tabela de vídeos e cria o objeto:
    atrs = {
      'autor': autor,
      'arq' : 'teste.mp4',
      'titulo': titulo,
    }
    vid = obj_video.cria(atrs)
    
  if vid != None:
    pag = html_pag_ver_video.gera(ses, vid, erros)
  else:
    # !!! Devia retornar a página de upload !!!
    pag = html_pag_mensagem_de_erro.gera(None, erros)

  return pag
