import obj_video
import html_elem_span
import html_elem_button_simples
import html_estilo_texto
import html_elem_div

# --------------------------------------------------------------------------------
#
# Funçoes auxiliares para criação de classes css grid
# --------------------------------------------------------------------------------

# Gera uma classe css grid area com o nome {nome} e podendo ter estilo personalizado
def gera_classe_css_grid_area(nome, estilo=None):
  return "." + nome + "{grid-area:" + nome + ";" + (estilo if estilo != None else '') + "}\n"

# Retorna o template area da matriz para criar o container do css grid
def gera_classe_css_grid_template_area(matriz):
  saida = "grid-template-areas: "
  for linhas in matriz:
    saida += f'"{' '.join(linhas)}"\n'
  return saida + ";\n"

# Gera a classe do container do css grid, podendo ter algum estilo adicional
def gera_classe_container_css_grid(matriz, estilo=None):
  saida = ".container { display: grid; grid-template-rows: auto; " + (estilo if estilo != None else '') + gera_classe_css_grid_template_area(matriz) + " }"
  return saida

# Gera a folha de estilos com as grid areas e com o container
def gera_style_css_grid(matriz, estilos):
  lista = []
  for linha in matriz:
    for item in linha:
      lista.append(item)
  regioes = list(set(lista))
  lista_areas = " ".join([gera_classe_css_grid_area(area, estilos[area] if area in estilos else None) for area in regioes])
  return "<style>" + lista_areas + gera_classe_container_css_grid(matriz) + "</style>"

# Retorna uma div contendo a classe {nome}
def gera_div_com_classe(nome, conteudo):
  return f'<div class="{nome}">{conteudo}</div>'

# Gera uma div usando a miniatura do video {url_img} como fundo 
def gera_miniatura_video(url_img, altura, largura, conteudo):
  return html_elem_div.gera(f"background-size: cover; background-image: url({url_img}); width: {largura}; height: {altura};", conteudo)

# --------------------------------------------------------------------------------
#
# Geracao da linha de catalogo de videos
# --------------------------------------------------------------------------------

def gera(vid, mostra_autor):

  assert vid != None, "precisa especificar um vídeo"

  vid_id = obj_video.obtem_identificador(vid)
  atrs = obj_video.obtem_atributos(vid)
  
  titulo = atrs['titulo']
  autor = atrs['autor'] if mostra_autor else 'Anônimo'
  data = atrs['data']
  vistas = atrs['vistas']
  nota = atrs['nota']
  segundos = str((int(atrs['duracao'])//1000) % 60)
  segundos = segundos if len(segundos) == 2 else f"0{segundos}"
  minutos = str((int(atrs['duracao'])//1000) // 60)

  # --------------------------------------------------------------------------------
  #
  # Geracao do bloco de video
  # --------------------------------------------------------------------------------
  
  # Texto com duração sobroposto no video 
  estilo_duracao_div = f"position: sticky; top: 100%; word-wrap:break-word; background-color: #000000; width: fit-content; float: right;"
  estilo_duracao = html_estilo_texto.gera("18px", "medium", "#FFFFFF", "#FF0000", None)
  ht_duracao = html_elem_span.gera(estilo_duracao, html_elem_div.gera(estilo_duracao_div, f"{minutos}:{segundos}"))

  # Componente com miniatura do video no fundo e duração no canto inferior direito
  ht_janela = gera_miniatura_video(f"capas/{vid_id}.png", "150px", "250px", ht_duracao)

  # --------------------------------------------------------------------------------
  #
  # Geracao do bloco de atributos
  # --------------------------------------------------------------------------------
  estilo_texto_div = f"display:block; word-wrap:break-word; padding: 5px 0px 10px 10px;"

  disposicao_conteudo = [["titulo", "titulo", "titulo"],
		                     ["conteudo", "conteudo", "conteudo"],
                         ["rodape", "rodape", "botao"]]
  
  estilos_conteudo = gera_style_css_grid(disposicao_conteudo, {'botao' : 'place-self: end;'})

  # --------------------------------------------------------------------------------
  #
  # Area do Titulo
  # --------------------------------------------------------------------------------
  estilo_titulo = html_estilo_texto.gera("24px", "medium", "#000000", None, None)
  ht_titulo = html_elem_span.gera(estilo_titulo, html_elem_div.gera(estilo_texto_div, titulo))
  ht_titulo = gera_div_com_classe("titulo", ht_titulo)

  # --------------------------------------------------------------------------------
  #
  # Area do Conteudo
  # --------------------------------------------------------------------------------
  estilo_conteudo = html_estilo_texto.gera("14px", "medium", "#000000", "#FF0000", None)
  ht_conteudo = html_elem_span.gera(estilo_conteudo, html_elem_div.gera(estilo_texto_div, f'Por: {autor}, em {data}.'))
  ht_conteudo += html_elem_span.gera(estilo_conteudo, html_elem_div.gera(estilo_texto_div, f'Visto {vistas} vezes.'))
  ht_conteudo = gera_div_com_classe("conteudo", ht_conteudo)

  # --------------------------------------------------------------------------------
  #
  # Area do Rodape
  # --------------------------------------------------------------------------------
  estilo_rodape = html_estilo_texto.gera("16px", "medium", "#000000", "#FF0000", None)
  ht_rodape = html_elem_span.gera(estilo_rodape, html_elem_div.gera(estilo_texto_div, f'Nota: {str(nota)}'))
  ht_rodape = gera_div_com_classe("rodape", ht_rodape)

  # --------------------------------------------------------------------------------
  #
  # Area do Botao
  # --------------------------------------------------------------------------------
  bt_args = { 'video': vid_id }
  bt_ver = html_elem_button_simples.gera("Ver", "ver_video", bt_args, None)
  ht_botao = gera_div_com_classe("botao", bt_ver)

  # --------------------------------------------------------------------------------
  #
  # Componente com todas as areas dentro do container
  # --------------------------------------------------------------------------------
  ht_atributos = ht_titulo + ht_conteudo + ht_rodape + ht_botao
  ht_atributos = estilos_conteudo + gera_div_com_classe("container", ht_atributos)

  hts_linha = [ ht_janela, ht_atributos ]
  
  return hts_linha
