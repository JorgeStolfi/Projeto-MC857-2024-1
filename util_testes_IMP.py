
import sys
import re
import inspect
import json
from util_erros import ErroAtrib
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

def escreve_resultado_html(modulo, rot_teste, ht_res, frag, pretty):
  nome_mod = modulo.__name__

  # Transforma o resultado numa página {pag}:
  if frag or ht_res == None:
    pag = gera_pagina_de_fragmentos(ht_res)
  else:
    assert type(ht_res) is str, ("{ht_res} = %s deveria ser string (página)" % str(ht_res))
    pag = ht_res
    
  if pretty:
    # Torna o HTML legível:
    pag = bsoup(pag + "\n", "html.parser").prettify()

  # Grava a página {pag} no arquivo:
  prefixo = "testes/saida/"
  nome_arq = nome_mod + "." + rot_teste
  sys.stderr.write(f"  gravando arquivo {nome_arq} ...\n")
  f = open(prefixo + nome_arq + '.html', 'w')
  f.buffer.write(str(pag).encode('utf-8'))
  f.close()

def testa_funcao_que_gera_html(modulo, funcao, rot_teste, frag, pretty, *args):
  nome_mod = modulo.__name__
  nome_fn = funcao.__name__
  func_rot = nome_fn + "." + rot_teste
  sys.stderr.write("  " + "-"*70 + "\n")
  try:
    sys.stderr.write(f"  util_testes.testa_funcao_que_gera_html: testando {nome_mod}.{nome_fn}\n")
    sys.stderr.write(f"  rot_teste = {rot_teste} args = {str(args)}\n")
    ht_res = funcao(*args)
    if len(str(ht_res)) <= 60: sys.stderr.write(f"  util_testes.testa_funcao_que_gera_html: resultado = {str(ht_res)}\n")
    if not frag and (type(ht_res) is list or type(ht_res) is tuple):
      # Deve ser um comando que retorna uma página e uma nova sessão:
      assert len(ht_res) == 2 and type(ht_res[1]) is not str, "resultado inválido"
      ht_res = ht_res[0]
    escreve_resultado_html(modulo, func_rot, ht_res, frag, pretty)
  except Exception as ex:
    fr = inspect.stack()[2]
    msg = ("File %s, line %d, in %s\n" % (fr[1], fr[2], str(fr[3])))
    msg += ("** erro em %s(%s): %s\n" % (nome_fn, str(args), str(ex)))
    sys.stderr.write(msg + "\n")
    ht_res = str(msg)
    escreve_resultado_html(modulo, func_rot, ht_res, True, pretty)
    raise
  sys.stderr.write("  " + "-"*70 + "\n")
  sys.stderr.write("\n")
  return

def gera_pagina_de_fragmentos(ht_res):
  """Gera uma página que mostra a lista de fragmentos HTML"""
  if ht_res == None:
    ht_titulo = "<h3>Resultado é {None}.</h3>\n"
  elif type(ht_res) is list or type(ht_res) is tuple:
    # Lista de elementos:
    if len(ht_res) == 0:
      ht_titulo = "<h3>Resultado é uma lista vazia.</h3>\n"
    else:
      ht_titulo = f"<h3>Resultado é uma lista de {len(ht_res)} elementos:</h3>\n"
  else:
    # Deve ser um único string:
    assert type(ht_res) is str, "tipo de {ht_res} inválido"
    ht_titulo = "<h3>Resultado é um string:</h3>\n"
    ht_res = [ ht_res, ]
  
  if ht_res == None:
    ht_cor_fundo = "#ff7733"
    ht_res_formatado = ""
  else:
    ht_cor_fundo = "#cccccc"
    ht_res_formatado = ""
    for ht_el in ht_res:
      assert type(ht_el) is str, "tipo de elemento inválido"
      ht_res_formatado += "<br/><hr/>" + ht_el
    ht_res_formatado += "<br/><hr/>"

  ht_cabecalho = \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n"
  ht_rodape = \
    "</body>\n" + \
    "</html>\n"  
  pag = ht_cabecalho + ht_titulo + ht_res_formatado + ht_rodape
  return pag

def formata_dict(dados):
  dados_lin = json.dumps(dados, indent='&nbsp;&nbsp;', sort_keys=True, separators=(',<br/>', ': '), ensure_ascii=False)
  dados_lin = re.sub(r'\[', '[<br/>', dados_lin)
  dados_lin = re.sub(r'\{', '{<br/>', dados_lin)
  dados_lin = re.sub(r'\},', '  \},', dados_lin)
  return dados_lin
  
def unico_elemento(lista):
  if lista == None:
    return None
  elif type(lista) is list or type(lista) is tuple:
    if len(lista) == 0:
      return None
    elif len(lista) == 1:
      res = lista[0];
      return res
    else:
      raise ErroAtrib([ f"argumento {str(lista)} tem mais de um elemento" ])
  else:
    raise ErroAtrib([ f"argumento {str(lista)} não é {None} ou lista" ])
