import sys
import re
import inspect
import json
from util_erros import ErroAtrib
from bs4 import BeautifulSoup as bsoup  # Pretty-print of HTML

max_len_debug = 120  # Aumente este valor se necessário

def escreve_resultado_html(modulo, funcao, rot_teste, ht_res, frag, pretty):
  nome_mod = modulo.__name__ + "." if modulo != None else ""
  nome_fun = funcao.__name__ + "."

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
  nome_arq = nome_mod + nome_fun + rot_teste + ".html"
  sys.stderr.write(f"    gravando arquivo {nome_arq} ...\n")
  f = open(prefixo + nome_arq, 'w')
  f.buffer.write(str(pag).encode('utf-8'))
  f.close()

def testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args):

  ok = True # Este teste deu resultado esperado se {True}, innesperado se {False}.
  
  sys.stderr.write(f"  {'-'*70}\n")
  sys.stderr.write(f"    testando {modulo.__name__}.{funcao.__name__}\n")
  st_args = trunca_tamanho(str(args), max_len_debug)
  sys.stderr.write(f"    rot_teste = '{rot_teste}' args = {st_args}'\n")
  
  try:
    res = funcao(*args)
    st_res = trunca_tamanho(str(res), max_len_debug)
    st_res = re.sub("\n", r"\\n", st_res)
    sys.stderr.write(f"    retorno normal, resultado = {st_res}\n")
  except AssertionError as ex:
    res = "AssertionError"
    sys.stderr.write(f"    levantou {res} ex =  {str(ex)}\n")
    if res_esp != res:
      # Re-raise to get diagnostics.
      raise
  except ErroAtrib as ex:
    res = "ErroAtrib"
    sys.stderr.write(f"    levantou {res} ex =  {str(ex)}\n")
    if res_esp != res:
      # Re-raise to get diagnostics.
      raise
    
  if res_esp == "AssertionError" or res_esp == "ErroAtrib":
    # Deve ter levantado esses erros:
    ok = (res == res_esp)
    if not ok:
      sys.stderr.write(f"    ** devia ter levantado exceção {res_esp}!\n")
  else:
    ok = check_result_recursive(res, res_esp)
    if not ok:
      sys.stderr.write(f"    ** devia ter devolvido {str(res_esp)}!\n")

  if ok:
    sys.stderr.write("    CONFERE!\n")
    
  if html:
    ht_res = res
  else:
    # Converte resultado para html:
    if isinstance(res, list) or isinstance(res, tuple):
      ht_res = list()
      # Converte cada elemento:
      for el in res:
        if not isinstance(el, str): el = str(el)
        st_el = protege_html(trunca_tamanho(el, max_len_debug))
        ht_res.append(st_el);
    else:
      res = str(res)
      ht_res = protege_html(trunca_tamanho(res, max_len_debug))

  escreve_resultado_html(modulo, funcao, rot_teste, ht_res, (not html or frag), pretty)

  sys.stderr.write(f"  {'-'*70}\n")
  return ok

def testa_funcao_validadora(rot_teste, valido, modulo, funcao, *args):
  html = False   # Resultados string jã são HTML?
  frag = False   # Resultados string são só fragmentos de página?
  pretty = False # Deve formatar o HTML para facilitar view source?
  res_esp = [] if valido else list
  ok = testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args)
  return ok

def testa_funcao_validadora_nulo_padrao(modulo, funcao, xrot, chave, valido_ex, valido_pt, val):
  ok = True
  for nulo_ok in ( False, True ):
    for padrao_ok in ( False, True ):
      for parcial in ( False, True ):
        if val != None or not ( parcial or padrao_ok):
          if val == None:
             valm = None
             valido = nulo_ok
          elif parcial:
            valm = "*" + val + "*"
            valido = valido_pt and padrao_ok
          else:
            valm = val
            valido = valido_ex
          rot_teste = xrot + "_pad" + str(parcial)[0] + "_padok" + str(padrao_ok)[0] + "_nulok" + str(nulo_ok)[0] + ("_GUD" if valido else "_BAD")
          res_esp = [] if valido else list
          ok_caso = testa_funcao_validadora(rot_teste, valido, modulo, funcao, chave, valm, nulo_ok, padrao_ok)
          ok = ok and ok_caso
  return ok

def check_result_recursive(r, r_esp):
  ok = True
  if r_esp == "*ANY*":
    # Qualquer resultado ou exceção está OK:
    return True
  elif r_esp == None or r_esp == [] or r_esp == () or r_esp == {} or r_esp == "":
    # Resultado deve ser o próprio:
    return (r == r_esp)
  elif isinstance(r_esp, type):
    # Basta ser desse tipo:
    return isinstance(r, r_esp)
  elif isinstance(r_esp, list) or isinstance(r_esp, tuple):
    if not isinstance(r, type(r_esp)) or len(r) != len(r_esp):
      return False
    else:
      for el, el_esp in zip(r, r_esp):
        if not check_result_recursive(el, el_esp): return False
      return True
  elif isinstance(r_esp, dict):
    if not isinstance(r, dict) or len(r) != len(r_esp):
      return False
    else:
      for chave in r_esp.keys():
        if not chave in r: return False
        if not check_result_recursive(r[chave], r_esp[chave]): return False
      return True
  else:
    return (r == r_esp)

def testa_funcao_que_gera_html(rot_teste, modulo, funcao, res_esp, frag, pretty, *args):
  html = True
  ok = testa_funcao(rot_teste, modulo, funcao, res_esp, html, frag, pretty, *args)
  return ok
 
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

def formata_valor(dado, html, max_len):

  dado = trunca_tamanho(dado, max_len)
  
  indenta = '&nbsp;&nbsp;' if html else '  '
  quebra = '<br/>' if html else ''
  sepcampo = ',' + quebra
  
  dados_lin = json.dumps(dado, indent=indenta, sort_keys=True, separators=(sepcampo, ': '), ensure_ascii=False)
  dados_lin = re.sub(r'\[', '[' + quebra, dados_lin)
  dados_lin = re.sub(r'\{', '{' + quebra, dados_lin)
  dados_lin = re.sub(r'\},', '  \},', dados_lin)
  
  return dados_lin
 
def trunca_tamanho(dado, max_len):
  # Indicadores de truncamento:
  fin_bytes = " [...]"
  ins_str = " «...» "
  ins_list = "..."
  
  # Lengths of prefix and suffix of truncated strings:
  pre_len = (2*max_len)//3
  pos_len = max_len - pre_len

  # Length of prefix and suffix of truncated lists:
  max_els = max(4, max_len//10)
  pre_els = max(2, pre_len//10)
  pos_els = max(1, pos_len//10)
  
  max_nbytes = 60;
  
  def recurse(arg):
    # Recurse:
    if arg == None:
      pass
    elif isinstance(arg, bytes):
      arg_trunc = f"bytes({len(arg)}):( "
      nbytes = len(arg)
      for i in range(min(nbytes, max_nbytes)):
        arg_trunc += f" {arg[i]:02x}"
      if nbytes > max_nbytes:
        arg_trunc += fin_bytes
      arg_trunc = arg_trunc + " )"
      arg = arg_trunc
    elif isinstance(arg, str):
      if len(arg) > max_len:
        arg_trunc = arg[:pre_len] + ins_str + arg[-pos_len:]
        arg = arg_trunc
    elif isinstance(arg, dict):
      res = {}
      for chave, val in arg.items():
        res[chave] = recurse(val)
      arg = res
    elif isinstance(arg, list) or isinstance(arg, tuple):
      res = []
      if len(arg) > max_els:
        arg_trunc = list(arg[:pre_els]) + [ ins_list, ] + list(arg[-pos_els:])
      else:
        arg_trunc = arg
      for el in arg_trunc:
        res.append(recurse(el))
      if isinstance(arg, tuple): res = tuple(res)
      arg = res
    else:
      arg = recurse(str(arg))
    return arg
    
  return recurse(dado)
  
def protege_html(cadeia):
  """Substitui caracteres [<>"'&] no string {cadeia}, que tem 
  significado especial para HTML, pelos equivalentes "&{nome};"."""
  assert isinstance(cadeia, str), "argumento inválido"
  cadeia = re.sub(r'&', "&amp;", cadeia) # Tem que ser o primeiro.
  cadeia = re.sub(r'<', "&lt;", cadeia)
  cadeia = re.sub(r'>', "&gt;", cadeia)
  cadeia = re.sub(r'"', "&quot;", cadeia)
  cadeia = re.sub(r"'", "&apos;", cadeia)
  return cadeia

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
      raise ErroAtrib([ f"argumento tem {len(lista)} elementos, máximo 1" ])
  else:
    st_lista = trunca_tamanho(str(lista), 200)
    raise ErroAtrib([ f"argumento {st_lista} não é {None} ou lista" ])
