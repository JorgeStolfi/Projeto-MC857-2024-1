# Implementação do módulo {comando_solicitar_pag_alterar_usuario}. 

import html_pag_alterar_usuario
import html_pag_mensagem_de_erro
import obj_sessao
import obj_usuario
from util_erros import erro_prog, aviso_prog

def processa(ses, cmd_args):
  # Páginas geradas pelo sistema deveriam garantir estas condições:
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(cmd_args, dict)

  erros = []
  
  ses_dono = None
  ses_dono_id = None
  para_admin = False
  if ses == None:
    erros.append("Precisa estar logado para postar um comentário")
  elif not obj_sessao.aberta(ses):
    erros.append("Esta sessão de login foi fechada. Precisa estar logado para postar um comentário")
  else:
    ses_dono = obj_sessao.obtem_dono(ses)
    assert ses_dono != None
    ses_dono_id = obj_usuario.obtem_identificador(ses_dono)
    para_admin = obj_usuario.eh_administrador(ses_dono)

  usr_id = cmd_args.pop('usuario', None)
  if usr_id == None: 
    # O parâmetro 'usuario' do comando nao foi especificado em {cmd_args}; supõe que é o dono da sessao:
    usr_id = ses_dono_id
  
  # Obtém o objeto {usr}
  usr = None
  if usr_id != None:
    usr = obj_usuario.obtem_objeto(usr_id)
    if usr == None:
      erros.append(f"O usuario \"{usr_id}\" não existe")
    
  # Verifica permissões:
  if usr != None:
    if ses_dono == None or (usr != ses_dono and not para_admin):
      erros.append("Você não tem permissão para alterar dados deste usuario")

  if len(erros) > 0:
    pag  = html_pag_mensagem_de_erro.gera(ses, erros)
  else:
    assert usr != None
    usr_atrs = obj_usuario.obtem_atributos(usr)
    pag = html_pag_alterar_usuario.gera(ses, usr_id, usr_atrs, None)
  return pag
    
