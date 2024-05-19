  
import html_bloco_titulo
import html_bloco_comentario
import html_pag_generica
import html_elem_span
import obj_comentario
import obj_sessao
import obj_usuario
import obj_video

def _formata_voto(com):  
  voto = obj_comentario.obtem_atributo(com, 'voto')
  pai = obj_comentario.obtem_atributo(com, 'pai')
  
  html = ''
  
  # Se o voto for inválido, não o formata e nem o exibe
  if (voto == None or voto < 0 or voto > 4):
    return html
  
  # Rótulo indicará sobre o que o voto é (o comentário pai ou sobre o vídeo)
  rotulo = 'Avaliação / Voto sobre o vídeo: ' if (pai == None) else 'Avaliação / Voto sobre o comentário pai: ' 
  html += html_elem_span.gera('font-size: 14; font-weight: bold', rotulo)
  
  # A formatação depende do valor numérico do voto e especifica um retorno visual (primeiro campo) e uma cor de texto para ser exibido (segundo campo)
  formatacao = {
    0: ('Detestei', '#af1c17'),
    1: ('Não gostei', '#cf7673'),
    2: ('Sem opinião', '#ffd934'),
    3: ('Gostei', '#8bd7b3'),
    4: ('Adorei', '#17af68'),
  }
  formatacao_do_voto = formatacao[voto]
  texto = str(voto) + " - " + formatacao_do_voto[0]
  cor = formatacao_do_voto[1]
  html += html_elem_span.gera('font-size: 14; font-weight: bold; color: ' + cor, texto)
  
  return html
  

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
  
  ht_comentario_voto = _formata_voto(com)
  
  ht_bloco = html_bloco_comentario.gera \
    ( com, 
      largura = 600, # Por enquanto.
      mostra_data = True, mostra_id = False, mostra_video = True, mostra_pai = True,
      bt_conversa = True, 
      bt_responder = (ses != None), 
      bt_editar  = ( ses_admin or ses_proprio )
    )
    
  ht_conteudo = ht_pag_tit + "\n" + ht_comentario_voto + "\n" + ht_bloco

  pag = html_pag_generica.gera(ses, ht_conteudo, erros)

  return pag
