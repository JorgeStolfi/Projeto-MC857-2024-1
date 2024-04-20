
import obj_sessao
import obj_usuario
import html_bloco_titulo
import html_pag_generica
import html_bloco_lista_de_comentarios
import obj_comentario

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão do comando inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  # Caso ses seja None, é necessário que seja passado um id de usuário de parâmetro
  assert not (ses == None and 'usuario' not in cmd_args), "Argumentos inválidos"
 
  erros = [].copy()

  # Caso ses != None, obtem o usuário {usr_ses} dono da sessão:
  usr_ses = None
  if ses != None:
    usr_ses = obj_sessao.obtem_usuario(ses); assert usr_ses != None
    id_usr_ses = obj_usuario.obtem_identificador(usr_ses)
  
  # Obtém o usuário {autor} a listar e seu identificador {id_autor}:
  if 'usuario' in cmd_args:
    # Alguém quer ver comentários de usuário específico:
    id_autor = cmd_args['usuario']
    autor = obj_usuario.busca_por_identificador(id_autor)
  else:
    autor = usr_ses
    id_autor = id_usr_ses

  if autor == None:
    erros.append(f"Usuário indeterminado")
    ht_bloco = None
  else:
    lista_ids_com = obj_comentario.busca_por_autor(id_autor)
    if len(lista_ids_com) == 0:
      # Argumentos com erro ou não encontrou nada.
      erros.append("Usuário não tem nenhum comentário")
      ht_conteudo = None
    else:
      # Encontrou pelo menos um comentário. Mostra em forma de tabela:
      if autor == usr_ses:
        ht_titulo = html_bloco_titulo.gera("Meus comentários")
      else:
        ht_titulo = html_bloco_titulo.gera(f"Comentários do usuário {id_autor}")
      ms_autor = False # Pois todos do mesmo autor.
      ms_video = True  # Podem ser de videos diferentes.
      ht_tabela = html_bloco_lista_de_comentarios.gera(lista_ids_com, ms_autor, ms_video)
      ht_conteudo = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_conteudo == None:
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_conteudo, erros)
  return pag
