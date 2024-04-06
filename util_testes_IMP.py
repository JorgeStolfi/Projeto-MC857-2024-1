# Implementação do módulo {util_testes}.

import sys
import re
import inspect
import json
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

def mostra_pilha(n):
  """Para uso por {erro_prog} e {aviso_prog}. Mostra as {n} 
  chamadas na pilha anteriores a essas funções."""
  sys.stderr.write("  --- Traceback (most recent call last) %s\n" % ("-" * 40))
  stack = inspect.stack()
  omite_recentes = 2 # Omite as chamadas mais recentes ({mostra_pilha} e {aviso_prog}).
  ini = omite_recentes + n # Indice da chamada mais antiga a mostrar.
  fin = omite_recentes     # Indice da chamada mais antiga a omitir.
  if ini >= len(stack): ini = len(stack) - 1;
  for k in range(ini - fin):
    fr = stack[ini - k]
    sys.stderr.write("%s:%d: ** in %s\n" % (fr[1],fr[2],fr[3]))
  sys.stderr.write("  %s\n" % ("-" * 70))

def erro_prog(mens):
  mostra_pilha(20)
  sys.stderr.write("    ** erro: %s\n" % mens)
  assert False # Tem que ser, para que apareça o traceback

def aviso_prog(mens, grave):
  mostra_pilha(20)
  tipo = ("** erro" if grave else "!! aviso")
  sys.stderr.write("    %s %s\n" % (tipo,mens))
  return

def mostra(ind,mens):
  sys.stderr.write("%*s%s\n" % (ind,'',mens))

def escreve_resultado_html(modulo, rotulo, ht_res, frag, pretty):
  prefixo = "testes/saida/"
  nome_mod = modulo.__name__
  nome_arq = nome_mod + "." + rotulo
  f = open(prefixo + nome_arq + '.html', 'w')
  # sys.stderr.buffer.write((str(*args) + "\n").encode('utf-8'))
  cabe = \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n"
  roda = \
    "</body>\n" + \
    "</html>\n"  
  if frag:
    if type(ht_res) is list or type(ht_res) is tuple:
      # Lista de elementos:
      ht_contents = f"<h3>Lista de {len(ht_res)} elementos:</h3>\n"
      for ht_el in ht_res:
        assert type(ht_el) is str, "tipo de elemento inválido"
        ht_contents += "<br/><hr/>" + ht_el
      ht_contents += "<br/><hr/>"
    else:
      # Deve ser um único elemento:
      assert type(ht_res) is str, "tipo de {ht_res} inválido"
      ht_contents = ht_res
    pag = cabe + ht_contents + roda
  else:
    assert type(ht_res) is str, ("tipo de {ht_res} inválido = %s" % str(ht_res))
    pag = ht_res
  if pretty:
    pag = bsoup(pag + "\n", "html.parser").prettify()
  f.buffer.write(str(pag).encode('utf-8'))
  f.close()

def testa_funcao_que_gera_html(modulo, funcao, rotulo, frag, pretty, *args):
  nome_fn = funcao.__name__
  func_rot = nome_fn + "." + rotulo
  try:
    ht_res = funcao(*args)
    if type(ht_res) is list or type(ht_res) is tuple:
      # Alguns comandos retornam outras informações além de 
      # uma página ou fragmento HTML.  Pegue só o primeiro
      # resultado:
      if len(ht_res) == 2 and not type(ht_res[1]) is str:
        ht_res = ht_res[0]
    escreve_resultado_html(modulo, func_rot, ht_res, frag, pretty)
  except Exception as ex:
    fr = inspect.stack()[2]
    msg = ("File %s, line %d, in %s\n" % (fr[1], fr[2], str(fr[3])))
    msg += ("** erro em testa(%s): %s\n" % (func_rot, str(ex)))
    sys.stderr.write(msg + "\n")
    ht_res = str(msg)
    escreve_resultado_html(modulo, func_rot, ht_res, True, pretty)
    raise

def formata_dict(dados):
  dados_lin = json.dumps(dados, indent='&nbsp;&nbsp;', sort_keys=True, separators=(',<br/>', ': '), ensure_ascii=False)
  dados_lin = re.sub(r'\[', '[<br/>', dados_lin)
  dados_lin = re.sub(r'\{', '{<br/>', dados_lin)
  dados_lin = re.sub(r'\},', '  \},', dados_lin)
  return dados_lin
