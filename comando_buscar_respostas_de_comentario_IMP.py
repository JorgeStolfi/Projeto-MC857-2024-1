import html_bloco_titulo
import html_pag_generica
import html_bloco_lista_de_comentarios
import obj_sessao
import obj_comentario

def processa(ses, cmd_args):
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão do comando inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  assert 'comentario' in cmd_args, "Comentário não especificado"

  erros = []
  
  # Obtém o comentário {com_pai} em questão e seu identificador {com_pai_id}:
  com_pai_id = cmd_args['comentario']
  com_pai = obj_comentario.obtem_objeto(com_pai_id) if com_pai_id != None else None
  
  if com_pai == None:
    erros.append(f"Comentário {com_pai_id} não existe")
    ht_bloco = None
  else:
    com_ids = obj_comentario.busca_por_pai(com_pai_id)
    if len(com_ids) == 0:
      # Não tem respostas:
      erros.append(f"Comentário {com_pai_id} não tem nenhuma resposta")
      ht_bloco = None
    else:
      ht_titulo = html_bloco_titulo.gera(f"Respostas ao comentario {com_pai_id}", False)
      mostra_autor = True  # Autores das respostas variam.
      Mostra_video = False # Todas as respostas são do mesmo video.
      mostra_pai = False   # Todas as respostas tem o mesmo pai.
      ht_tabela = html_bloco_lista_de_comentarios.gera(com_ids, mostra_autor, mostra_video, mostra_pai)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
