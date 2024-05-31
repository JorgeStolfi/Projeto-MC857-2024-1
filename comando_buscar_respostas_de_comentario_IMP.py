import html_bloco_titulo
import html_pag_generica
import html_bloco_lista_de_comentarios
import html_pag_mensagem_de_erro
import obj_sessao
import obj_comentario
import obj_usuario

def processa(ses, cmd_args):
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and type(cmd_args) is dict

  ses_dono = obj_sessao.obtem_dono(ses); 
  para_admin = obj_usuario.eh_administrador(ses_dono)

  erros = []
  
  # Obtém o comentário {com_pai} em questão e seu identificador {com_pai_id}:
  pai_id = cmd_args.pop('comentario', None)
  if pai_id != None:
    pai = obj_comentario.obtem_objeto(pai_id)
    if pai == None:
      erros.append(f"O comentário \"{pai_id}\" não existe")

  ht_bloco = None
  if len(erros) == 0:
    assert pai != None
    com_ids = obj_comentario.busca_por_pai(pai_id)
    if len(com_ids) == 0:
      erros.append(f"O comentário \"{pai_id}\" não tem nenhuma resposta")
    else:
      ht_titulo = html_bloco_titulo.gera(f"Respostas ao comentario {pai_id}")
      ht_tabela = html_bloco_lista_de_comentarios.gera\
        ( com_ids, 
          mostra_autor = True,  # Autores das respostas variam.
          mostra_video = False, # Todas as respostas são do mesmo video.
          mostra_pai = False,   # Todas as respostas tem o mesmo pai.
          mostra_nota = True,   # Porque não mostraria?
          forcar_mostrar_texto = para_admin # Apenas admins forçam a visualização do texto
        )
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if len(erros) == 0:
    assert ht_bloco != None
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  else:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  return pag
