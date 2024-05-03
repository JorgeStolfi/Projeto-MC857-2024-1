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

  erros = [].copy()
  
  # Obtém o comentário {com_pai} em questão e seu identificador {id_com_pai}:
  id_com_pai = cmd_args['comentario']
  com_pai = obj_comentario.obtem_objeto(id_com_pai) if id_com_pai != None else None
  
  if com_pai == None:
    erros.append(f"Comentário {id_com_pai} não existe")
    ht_bloco = None
  else:
    lista_ids_com = obj_comentario.busca_por_pai(id_com_pai)
    if len(lista_ids_com) == 0:
      # Não tem respostas:
      erros.append(f"Comentário {id_com_pai} não tem nenhuma resposta")
      ht_bloco = None
    else:
      ht_titulo = html_bloco_titulo.gera(f"Respostas ao comentario {id_com_pai}", False)
      mostra_autor = True  # Autores das respostas variam.
      Mostra_video = False # Todas as respostas são do mesmo video.
      mostra_pai = False   # Todas as respostas tem o mesmo pai.
      ht_tabela = html_bloco_lista_de_comentarios.gera(lista_ids_com, mostra_autor, mostra_video, mostra_pai)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
