import html_estilo_de_botao
from util_testes import erro_prog
import re

def gera(texto, URL, cmd_args, cor_fundo):
  if cmd_args != None:
    # Acrescenta argumentos ao {URL}:
    sep = '?'
    for chave, val in cmd_args.items():
      verifica_chave(chave)
      if val != None and val != "":
        verifica_valor(val)
        URL += sep + chave + "=" + val
        sep = '&'

  # Constrói o botão propriamente dito:
  estilo = html_estilo_de_botao.gera(cor_fundo)
  html = "<button type=\"button\" style=\"" + estilo + "\" onclick=\"location.href='" + URL + "'\">" + texto + "</button>"
  return html
      
def verifica_chave(chave): 
  """ Verifica se {chave} pode ser um nome válido de 
  parãmetro do comando."""
  chave_invs = re.findall("[^-a-zA-Z0-9_]", chave)
  if len(chave_invs) != 0:
    erro_prog(f"chave inválida: '{chave}'")

def verifica_valor(val): 
  """ Verifica se {val} pode ser um valor válido para um 
  parãmetro do comando."""
  val_invs = re.findall("[^-+a-zA-Z0-9.,_]", val)
  if len(val_invs) != 0:
    erro_prog(f"valor inválido: '{val}'")
