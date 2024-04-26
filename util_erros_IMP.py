import inspect
import json
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML
import sys, re, os

def mostra_pilha(n_pula, n_pega):
  """Para uso por {erro_prog} e {aviso_prog}. Mostra as {n_pega} 
  chamadas na pilha anteriores a essas funções."""
  
  cwd = os.getcwd() + "/"
  sys.stderr.write("  --- Traceback (most recent call last) %s\n" % ("-" * 40))
  stack = inspect.stack()
  ini = n_pula + n_pega # Indice da chamada mais antiga a mostrar.
  fin = n_pula          # Indice da chamada mais antiga a omitir.
  if ini >= len(stack): ini = len(stack) - 1;
  for k in range(ini - fin):
    fr = stack[ini - k]
    filename = fr[1].removeprefix(cwd)
    lineno = fr[2]
    funcname = fr[3]
    sys.stderr.write(f"  File {filename}:{lineno}: ** in {funcname}\n")
  sys.stderr.write("  " + ("-"*70) + "\n")

def erro_prog(mens):
  sys.stderr.write("** erro fatal: %s\n" % mens)
  mostra_pilha(2, 20) # Omite as entradas da pilha de {mostra_pilha} e {erro_prog}.
  assert False, mens # Tem que ser, para que apareça o traceback

def aviso_prog(mens, grave):
  tipo = ("** erro" if grave else "!! aviso")
  sys.stderr.write("%s: %s\n" % (tipo, mens))
  # mostra_pilha(2, 20) # Omite as entradas da pilha de {mostra_pilha} e {erro_prog}.
  return

def mostra(ind,mens):
  sys.stderr.write("%*s%s\n" % (ind,'',mens))
