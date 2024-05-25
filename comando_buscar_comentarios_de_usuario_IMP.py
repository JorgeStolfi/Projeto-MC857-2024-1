
import obj_sessao
import obj_usuario
import html_bloco_titulo
import html_pag_generica
import html_bloco_lista_de_comentarios
import html_pag_mensagem_de_erro
import obj_comentario

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and type(cmd_args) is dict
 
  erros = []

  # Caso ses != None, obtem o usuário {ses_dono} dono da sessão:
  ses_dono = None
  if ses != None:
    ses_dono = obj_sessao.obtem_dono(ses); assert ses_dono != None
    ses_dono_id = obj_usuario.obtem_identificador(ses_dono)
  
  # Obtém o usuário {autor} a listar e seu identificador {autor_id}:
  if 'usuario' in cmd_args:
    # Alguém quer ver comentários de usuário específico:
    autor_id = cmd_args['usuario']
    autor = obj_usuario.obtem_objeto(autor_id)
  elif ses_dono != None:
    autor = ses_dono
    autor_id = ses_dono_id
  else:
    autor = None
    autor_id = None

  ht_conteudo = None # A menos que seja gerado.
  if autor == None:
    erros.append(f"O usuário a buscar não foi especificado")
  else:
    com_ids = obj_comentario.busca_por_autor(autor_id)
    if len(com_ids) == 0:
      erros.append(f"O usuário \"{autor_id}\" não postou nenhum comentário")
    else:
      # Encontrou pelo menos um comentário. Mostra em forma de tabela:
      if autor == ses_dono:
        ht_titulo = html_bloco_titulo.gera("Meus comentários")
      else:
        assert autor_id != None
        ht_titulo = html_bloco_titulo.gera(f"Comentários do usuário {autor_id}")
      ht_tabela = html_bloco_lista_de_comentarios.gera\
        ( ses,
          com_ids,
          mostra_autor = False, # Pois são todos do mesmo autor.
          mostra_video = True,  # Podem ser de videos diferentes.
          mostra_pai = True,    # Podem ter pais diferentes.
          mostra_nota = True,   # Porque não mostraria?
        )
      ht_conteudo = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_conteudo == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
