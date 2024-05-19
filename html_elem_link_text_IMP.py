from util_erros import erro_prog, aviso_prog
import re

def gera(texto, url, cmd_args):
    assert type(texto) is str # Confere o argumento
    # Acrescenta argumentos ao {url}:
    sep = '?'
    for chave, val in cmd_args.items():
      verifica_chave(chave)
      if val != None and val != "":
        verifica_valor(val)
        url += sep + chave + "=" + val
        sep = '&'
    html = "<a href='" + url + "'>" + texto + "</a>"
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
