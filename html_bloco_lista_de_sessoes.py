
import html_bloco_lista_de_sessoes_IMP

def gera(ses_ids, bt_ver, bt_fechar, mostra_dono):
  """Retorna um trecho de HTML que descreve as sessoes cujos identificadores
  estão na lista {ses_ids}, uma por linha.
  
  Os parâmetros booleanos {bt_ver} e {bt_fechar} determinam se os 
  botões "Ver" e "Fechar" devem ser exibidos em cada linha.
  
  O parâmetro booleano {mostra_dono} determina se a lista deve ter 
  a coluna "Dono".
  """
  return html_bloco_lista_de_sessoes_IMP.gera(ses_ids, bt_ver, bt_fechar, mostra_dono)
