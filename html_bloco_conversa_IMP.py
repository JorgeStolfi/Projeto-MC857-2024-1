import html_bloco_comentario
import html_elem_div
import obj_video
import obj_usuario
import obj_comentario

def gera(conversa, ses_dono):

  # Verificação de tipos dos argumentos (paranóia):
  assert conversa == None or isinstance(conversa,list) or  isinstance(conversa,tuple)

  ht_bloco = formata_floresta(conversa, ses_dono)
  return ht_bloco

def formata_floresta(flor, ses_dono):
  """Formata a floresta de comentários {flor}, recursivamente."""
  if flor == None: flor = []
  assert isinstance(flor, list) or isinstance(flor, tuple)
  lista_hts_arvs = []
  for arv in flor:
    ht_arv = formata_arvore(arv, ses_dono)
    lista_hts_arvs.append(ht_arv)
    
  estilo = "padding: 0px 0px 0px 20px;"
  ht_floresta = html_elem_div.gera(estilo, "\n".join(lista_hts_arvs))
  
  return ht_floresta
  
def formata_arvore(arv, ses_dono):
  """Formata a árvore de comentários {arv}, recursivamente."""
  assert (isinstance(arv, list) or isinstance(arv, tuple))
  assert len(arv) > 0

  raiz_id = arv[0]
  raiz = obj_comentario.obtem_objeto(raiz_id)
  if raiz == None: erro_prog(f"Comentário {raiz_id} não existe")
  raiz_autor = obj_comentario.obtem_autor(raiz)
  assert raiz_autor != None
  logado = (ses_dono != None)
  para_admin = obj_usuario.eh_administrador(ses_dono) if ses_dono != None else False
  para_autor = (ses_dono == raiz_autor) if ses_dono != None else False
  ht_raiz = html_bloco_comentario.gera \
    ( raiz, largura = 600, mostra_id = True, mostra_data = True, 
      mostra_video = False, mostra_pai = False, mostra_bloqueado = para_admin,
      bt_conversa = True, 
      bt_responder = logado, 
      bt_editar = (para_admin or para_autor),
      bt_calcnota = (para_admin or para_autor),
      bt_bloq_desbloq = para_admin
    )

  ht_subarvs = formata_floresta(arv[1:], ses_dono)

  ht_arv = ht_raiz + "\n" + ht_subarvs
  return ht_arv
