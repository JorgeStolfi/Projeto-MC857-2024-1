import html_elem_span
import html_elem_paragraph
import html_elem_button_simples
import re

def gera(erros):
  # Cabeçalho espalhafatoso:
  estilo_cabecalho = f"font-family: Courier; font-size: 24px; font-weight: bold; padding: 5px; text-align: left; color: #880000;"
  ht_tit = html_elem_span.gera(estilo_cabecalho, "Não foi possível completar a operação")

  if type(erros) is list or type(erros) is tuple:
    erros = "\n".join(erros)

  # Processa quebras de linha em {erros}:
  erros = re.sub(r'\n', r'<br/>Erro: \n', erros)

  # Formata a mensagem:
  estilo_erro = f"font-family: Courier; font-size: 20px; font-weight: bold; padding: 5px; text-align: left; color: #000000;"
  ht_erros = html_elem_span.gera(estilo_erro, erros)

  # Junta as partes:
  ht_tudo = ht_tit + "<br/>" + ht_erros

  # Formata:
  estilo_parag = " width: 600px; margin-top: 2px;margin-bottom: 2px; text-indent: 0px; align: center;"
  bloco_final = html_elem_paragraph.gera(estilo_parag, ht_tudo)

  return bloco_final
