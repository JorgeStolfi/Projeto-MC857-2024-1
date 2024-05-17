import html_bloco_lista_de_sessoes
import html_bloco_titulo
import html_pag_generica
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert cmd_args != None and type(cmd_args) is dict
  
  erros = []
  
  # Obtem o usuário {ses_dono} dono da sessão:
  ses_dono = None
  para_admin = None
  if ses == None:
    erros.append("É preciso estar logado para executar esta busca")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. É preciso estar logado para executar esta busca")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    para_admin = obj_usuario.eh_administrador(ses_dono)
  ses_dono_id = obj_usuario.obtem_identificador(ses_dono) if ses_dono != None else None
 
  # Obtém o usuário {usr_a_ver} a listar e seu identificador {usr_a_ver_id}:
  if 'usuario' in cmd_args:
    # Alguém quer ver sessões de usuário específico:
    usr_a_ver_id = cmd_args['usuario']
    usr_a_ver = obj_usuario.obtem_objeto(usr_a_ver_id)
    if usr_a_ver_id != ses_dono_id and not obj_sessao.de_administrador(ses):
      # Usuário comum não pode ver sessãoes de outros:
      erros.append(f"Você não tem permissão para executar esta busca")
  else:
    # Usuário da sessão {ses} quer ver as próprias sessões:
    usr_a_ver = ses_dono
    usr_a_ver_id = ses_dono_id
    
  # Se não houve erros, monta a página {pag} com resultado da busca:
  pag = None  
  if len(erros) == 0:
    ses_ids = obj_sessao.busca_por_campo('dono', usr_a_ver_id)
    if len(ses_ids) == 0:
      # Argumentos com erro ou não encontrou nada.
      erros.append(f"O usuário \"{usr_a_ver_id}\" não tem nenhuma sessão")
    else:
      # Encontrou pelo menos uma sessão.  Mostra em forma de tabela:
      if usr_a_ver == ses_dono:
        ht_titulo = html_bloco_titulo.gera("Minhas sessões")
      else:
        ht_titulo = html_bloco_titulo.gera(f"Sessões do usuário {usr_a_ver_id}")
      bt_ver = True
      bt_fechar = True
      mostrar_usr = False # Não mostrar a coluna Usuário para o comando buscar sessões de usuário.
      ht_tabela = html_bloco_lista_de_sessoes.gera(ses_ids, bt_ver, bt_fechar, mostrar_usr)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela
      pag = html_pag_generica.gera(ses, ht_bloco, erros)

  if pag == None:
    pag = html_pag_mensagem_de_erro.gera(ses, erros)
    
  return pag
