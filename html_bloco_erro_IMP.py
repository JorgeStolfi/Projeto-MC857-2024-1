import html_estilo_titulo
import html_estilo_texto
import html_elem_span
import html_elem_paragraph
import html_elem_button_simples
import re

def gera(erros):
  
  # Quebra e limpa as mensagens:
  if erros == None:
    erros = []
  elif type(erros) == str:
    # Quebra em linhas:
    erros = re.split('[\n]', erros)
  assert type(erros) is list or type(erros) is tuple
  erros = [ er for er in erros if er != None ]
  erros = [ er.strip() for er in erros ]
  erros = [ er for er in erros if len(er) > 0 ]
  if len(erros) == 0:
    ht_bloco_final = ""
  else:
    # Cabeçalho espalhafatoso:
    estilo_cabecalho = html_estilo_titulo.gera("#b00000")
    ht_tit = html_elem_span.gera(estilo_cabecalho, "Não foi possível completar a operação")

    # Formata as mensagens:
    cor_texto = "#000000"
    cor_fundo = None
    margens = None
    estilo_erro = html_estilo_texto.gera("20px", "bold", cor_texto, cor_fundo, margens)
    ht_erros = "<br/>\n" + "<br/>\n".join(erros)
    ht_erros = html_elem_span.gera(estilo_erro, ht_erros)

    # Junta as partes:
    ht_tudo = ht_tit + "<br/>" + ht_erros

    # Formata:
    estilo_parag = " width: 600px; margin-top: 2px;margin-bottom: 2px; text-indent: 0px; align: center;"
    ht_bloco_final = html_elem_paragraph.gera(estilo_parag, ht_tudo)

  return ht_bloco_final
