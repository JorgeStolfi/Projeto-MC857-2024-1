import html_bloco_dados_de_comentario
import html_elem_div
import obj_video
import obj_usuario
import obj_comentario

def gera(conversa):
  ht_bloco = formata_floresta(conversa)
  return ht_bloco

def formata_floresta(flor):
  """Formata a floresta de comentários {flor}, recursivamente."""
  if flor == None: flor = []
  assert isinstance(flor, list) or isinstance(flor, tuple)
  lista_hts_arvs = [].copy()
  for arv in flor:
    ht_arv = formata_arvore(arv)
    lista_hts_arvs.append(ht_arv)
    
  estilo = "padding: 0px 0px 0px 20px;"
  ht_floresta = html_elem_div.gera(estilo, "\n".join(lista_hts_arvs))
  
  return ht_floresta
  
def formata_arvore(arv):
  """Formata a árvore de comentários {arv}, recursivamente."""
  assert (isinstance(arv, list) or isinstance(arv, tuple))
  assert len(arv) > 0

  raiz_id = arv[0]
  raiz = obj_comentario.obtem_objeto(raiz_id)
  if raiz_id == None: erro_prog(f"Comentarion {raiz_id} nãoe existe")
  raiz_atrs = obj_comentario.obtem_atributos(raiz)
  ed_texto = False
  ht_raiz = html_bloco_dados_de_comentario.gera(raiz_id, raiz_atrs, ed_texto)
  ht_subarvs = formata_floresta(arv[1:])

  ht_arv = ht_raiz + "\n" + ht_subarvs
  return ht_arv
