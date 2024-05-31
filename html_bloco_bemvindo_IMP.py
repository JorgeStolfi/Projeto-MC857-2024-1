import html_elem_div
import html_elem_link_img
import html_estilo_texto
import obj_sessao
import obj_usuario

bmu_debug = False

def gera(usr):
  
  # Estilo do texto:
  cor_texto = "#228800"
  cor_fundo = None
  margens = None
  estilo_texto = html_estilo_texto.gera("18px", "medium", cor_texto, cor_fundo, margens)

  # Determina a imagem{ht_imagem} e o texto {ht_texto}
  texto_bem = "Bem-vindo ao nosso site de vídeos!"
  if usr == None:
    texto = texto_bem
    ht_imagem = ""
  else:
    usr_id = obj_usuario.obtem_identificador(usr)

    # Olá personalizado:
    usr_nome = obj_usuario.obtem_atributo(usr, 'nome')
    texto_ola = "Olá " + usr_nome + "!"
    
    # Pega o avatar do usuário:
    avatar_descr = f"Avatar de {usr_nome}"
    avatar_tam = 36
    avatar_arq = f"avatares/avatar_{usr_id}.png"
    ht_imagem = html_elem_link_img.gera(avatar_arq, avatar_descr, avatar_tam, None)

    # Determina o número de sessões abertas {nsa}
    nsa = len(obj_sessao.busca_por_dono(usr, True)) if usr != None else 0
    if nsa > 1:
      if nsa == 2:
        texto_nsa = "Você tem outra sessao aberta."
      else:
        texto_nsa = f"Você tem outras {nsa-1} sessoes abertas."
      texto = texto_ola + "<br/>" + texto_nsa
    else:
      texto = texto_ola + "<br/>" + texto_bem

  # Formata {texto}:
  ht_texto = html_elem_div.gera(estilo_texto, texto)
  
  ht_bloco = \
    "<nav style=\"display:flex; gap:10px;\">" + \
    ht_imagem + \
    ht_texto + \
    "</nav>"
  return ht_bloco
