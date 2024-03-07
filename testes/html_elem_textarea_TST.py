import html_elem_textarea
import util_testes

def testa(rotulo, *args):
  """Testa {funcao(*args, "elucubrar")}, grava resultado 
  em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""
  modulo = html_elem_textarea
  funcao = modulo.gera
  frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
  pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
  util_testes.testa_gera_html(modulo, modulo.gera, rotulo, frag, pretty, *args)
   
testa("text_dica",   "Peso", "textarea", "peso", None,    None, True,  "Máximo 50 kg", "vade_retro")
testa("text_vini",   "Peso", "textarea", "peso", "30 kg", None, True,  None,           "vade_retro")
testa("text_rdonly", "Peso", "textarea", "peso", "30 kg", None, False, None,           "vade_retro")

testa("text_obrigatorio",  None, "textarea", "user", "U-12345678", None, True, None,   "do_it", True)
testa("text_not_obrigatorio",  None, "textarea", "user", "U-12345678", None, True, None,   "do_it", False)
testa("text_not_obrigatorio_default",  None, "textarea", "user", "U-12345678", None, True, None,   "do_it")
