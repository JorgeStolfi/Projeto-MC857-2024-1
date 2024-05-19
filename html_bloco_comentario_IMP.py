import obj_video
import obj_usuario
import obj_comentario
import html_bloco_cabecalho_de_comentario
import html_elem_button_simples
import html_elem_div
import html_elem_span
import html_estilo_texto

def gera(com, largura, mostra_id, mostra_data, mostra_video, mostra_pai, bt_conversa, bt_responder, bt_editar):

  # Validação de tipos (paranóia):
  assert com != None and isinstance(com, obj_comentario.Classe)
  assert isinstance(largura, int)
  assert isinstance(mostra_video, bool)
  assert isinstance(mostra_pai, bool)
  assert isinstance(bt_conversa, bool)
  assert isinstance(bt_responder, bool)
  assert isinstance(bt_editar, bool)
  
  com_id = obj_comentario.obtem_identificador(com)
  com_atrs = obj_comentario.obtem_atributos(com)
  
  estilo_texto = html_estilo_texto.gera("18px", "medium", "#000000", None, None)
  estilo_texto_div = f"display:block; width: {largura}px; word-wrap:break-word; padding: 5px 0px 10px 10px;"
  
  ht_cabeca = html_bloco_cabecalho_de_comentario.gera(com_id, com_atrs, largura, mostra_id, mostra_data, mostra_video, mostra_pai)
  
  # ----------------------------------------------------------------------
  # Texto do comentário:
  
  texto = com_atrs['texto']
  ht_texto = html_elem_span.gera(estilo_texto, html_elem_div.gera(estilo_texto_div, texto))

  # ----------------------------------------------------------------------
  # Botões:

  cmd_args = { 'comentario': com_id }
  ht_botoes = ""

  if bt_conversa:
    ht_bt_conversa = html_elem_button_simples.gera("Ver respostas", 'ver_conversa', cmd_args, None)
    ht_botoes += ht_bt_conversa

  if bt_responder:
    ht_bt_responder = html_elem_button_simples.gera("Responder", "solicitar_pag_postar_comentario", cmd_args, None)
    ht_botoes += ht_bt_responder

  if bt_editar:
    ht_bt_alterar = html_elem_button_simples.gera(f"Editar", "solicitar_pag_alterar_comentario", cmd_args, None)
    ht_botoes += ht_bt_alterar
    
  ht_bloco = \
    ht_cabeca + \
    ht_texto + \
    ht_botoes

  return ht_bloco
