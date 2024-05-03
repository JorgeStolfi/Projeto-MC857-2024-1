import html_bloco_lista_de_sessoes
import html_bloco_titulo
import html_pag_generica
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario

def processa(ses, cmd_args):
  
  # Páginas do sistema deveriam garantir estas condições:
  assert ses == None or obj_sessao.aberta(ses), "Sessão do comando inválida"
  assert cmd_args != None and type(cmd_args) is dict, "Argumentos inválidos"
  
  erros = [].copy()
  
  # Obtem o usuário {usr_ses} dono da sessão:
  usr_ses = obj_sessao.obtem_usuario(ses); assert usr_ses != None
  id_usr_ses = obj_usuario.obtem_identificador(usr_ses)
 
  # Obtém o usuário {usr} a listar e seu identificador {id_usr}:
  if 'usuario' in cmd_args:
    # Alguém quer ver sessões de usuário específico:
    id_usr = cmd_args['usuario']
    usr = obj_usuario.obtem_objeto(id_usr)
    if id_usr != id_usr_ses and not obj_sessao.de_administrador(ses):
      # Usuário comum não pode ver sessãoes de outros:
      erros.append(f"Permissão negada")
  else:
    # Usuário da sessão {ses} uer ver as próprias sessões:
    usr = usr_ses
    id_usr = id_usr_ses
    
  if usr == None:
    erros.append(f"Usuario indeterminado")
    ht_bloco = None
  else:
    lista_ids_ses = obj_sessao.busca_por_campo('usr', id_usr)
    if len(lista_ids_ses) == 0:
      # Argumentos com erro ou não encontrou nada.
      erros.append("Usuário não tem nenhuma sessão")
      ht_bloco = None
    else:
      # Encontrou pelo menos uma sessão.  Mostra em forma de tabela:
      if usr == usr_ses:
        ht_titulo = html_bloco_titulo.gera("Minhas sessões")
      else:
        ht_titulo = html_bloco_titulo.gera(f"Sessões do usuário {id_usr}")
      bt_ver = True
      bt_fechar = True
      ht_tabela = html_bloco_lista_de_sessoes.gera(lista_ids_ses, bt_ver, bt_fechar)
      ht_bloco = \
        ht_titulo + "<br/>\n" + \
        ht_tabela

  if ht_bloco == None:
    pag = html_pag_mensagem_de_erro(ses, erros)
  else:
    pag = html_pag_generica.gera(ses, ht_bloco, erros)
  return pag
