import obj_sessao
import html_pag_generica
import html_elem_button_simples

def gera(ses, erros):
  
  # Validação de tipos (paranóia):
  assert ses == None or isinstance(ses, obj_sessao.Classe)
  assert isinstance(erros, str) or isinstance(erros, list) or isinstance(erros, tuple) 
  
  if isinstance(erros, str): erros = [ erros, ]
  assert len(erros) > 0 # Não faz sentido chamar esta página sem erros.

  ht_botao = html_elem_button_simples.gera("OK", 'pag_principal', None, '#55ee55')
  pagina = html_pag_generica.gera(ses, ht_botao, erros)
  return pagina
