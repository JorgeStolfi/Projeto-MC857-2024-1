  
import html_bloco_titulo
import html_bloco_comentario
import html_pag_generica
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video

def gera(ses, com, erros):
  
  # Verificação de tipos de dados (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert com != None and isinstance(com, obj_comentario.Classe)
  assert erros == None or isinstance(erros, list) or isinstance(erros, tuple)
  
  ses_dono = obj_sessao.obtem_dono(ses) if ses != None else None
  ses_admin = obj_usuario.eh_administrador(ses_dono) if ses != None else False
  ses_proprio = (ses_dono == obj_comentario.obtem_atributo(com, 'autor'))
  
  com_id = obj_comentario.obtem_identificador(com)
  ht_pag_tit = html_bloco_titulo.gera(f"Comentário {com_id}")
  
  ht_bloco = html_bloco_comentario.gera \
    ( com, 
      largura = 600, # Por enquanto.
      mostra_data = True, mostra_id = False, mostra_video = True, mostra_pai = True,
      bt_conversa = True, 
      bt_responder = (ses != None), 
      bt_editar  = ( ses_admin or ses_proprio )
    )
    
  ht_conteudo = ht_pag_tit + "\n" + ht_bloco

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
