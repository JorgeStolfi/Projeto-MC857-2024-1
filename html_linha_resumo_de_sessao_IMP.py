import obj_sessao
import obj_usuario
import html_elem_item_de_resumo
import html_elem_button_simples
import html_elem_link_text

import sys

def gera(ses, bt_ver, bt_fechar, mostra_dono):

  ses_id = obj_sessao.obtem_identificador(ses) if ses != None else None
  atrs = obj_sessao.obtem_atributos(ses) if ses != None else None
  
  ht_campos = []
  
  colunas = [ 'sessao', 'aberta', 'dono', 'criacao', 'cookie' ]
  
  for chave in colunas:
    if chave == 'sessao':
      mostra = True
      texto = html_elem_link_text.gera(ses_id, "ver_sessao", { 'sessao': ses_id }) if ses != None else "Sessão"
    elif chave == 'dono':
      mostra = mostra_dono
      texto = html_elem_link_text.gera(obj_usuario.obtem_identificador(atrs['dono']), "ver_usuario", { 'usuario': obj_usuario.obtem_identificador(atrs['dono']) }) if ses != None else "Dono"
    elif chave == 'aberta':
      mostra = True
      texto = ("Aberta" if atrs['aberta'] else "Fechada") if ses != None else "Estado"
    elif chave == 'criacao':
      mostra = True
      texto = atrs[chave] if ses != None else "Data de criação"
    else:
      mostra = True
      texto = atrs[chave] if ses != None else chave.capitalize()

    if mostra:
      cab = (ses == None)
      cor_fundo = None # Precisariamos saber a sessão atual, poderia passar como parâmetro mas não consegui Professor. Peço desculpas.
      alinha = "left"
      ht_item = html_elem_item_de_resumo.gera(texto, cab, cor_fundo, alinha)
      ht_campos.append(ht_item)
  
  if ses != None:
    args_bt = { 'sessao': ses_id } # Argumentos para os botões.

    if bt_ver:
      bt_ver = html_elem_button_simples.gera("Ver", 'ver_sessao', args_bt, None)
      ht_campos.append("<td>" + bt_ver + "</td>")

    if bt_fechar:
      if atrs['aberta']:
        bt_fechar = html_elem_button_simples.gera("Fechar", 'fechar_sessao', args_bt, None)
      else:
        bt_fechar = " "
      ht_campos.append("<td>" + bt_fechar + "</td>")

  return ht_campos
