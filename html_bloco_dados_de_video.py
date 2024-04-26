import html_bloco_dados_de_video_IMP

def gera(id_vid, atrs_vid, editavel):
  """
  Retorna um fragmento HTML que exibe os atributos do video {vid} cujo
  identificador é {id_vid} e cujos atributos são supostamente
  {atrs_vid}. 
  
  O resultado desta função será um bloco "<table>...</table>". Cada
  linha da tabela terá duas colunas, um rótulo ("Autor", "Data", etc.) e
  um campo "<input>" ou "<textarea>" com o valor do atributo
  correspondente. Alguns atributos podem ser editáveis, portanto este
  bloco deve ser incluído em um elemento "<form>...</form>". Veja
  {html_elem_form.gera}.
  
  O parâmetro {id_vid} deve ser {None} ou o identificador 
  (um string no formato "V-{NNNNNNNN}") de um vídeo existente.
  
  O parâmetro {atrs_vid} deve ser {None} ou um dict.

  Os parâmetros {editavel} é um {bool} que controla
  a editabilidade de certos campos. Vide abaixo.
   
  Se {id_vid} não é {None}, supõe que este bloco se destina a examinar o
  atributos de um vídeo previamente inserido no sistema. Neste caso o
  dicionário {atrs_vid} deve ter todos os atributos do vídeo {vid}. O
  bloco vai mostrar todos esses atributos, bem como o identificador
  {id_vid}. O campo 'titulo' será editável se {editavel} for True,
  caso contrário será readonly.
  
  Se {id_vid} é {None}, supõe este bloco
  vai ser usad para fazer upload de um novo vídeo. Nesse caso, o dicionário
  {atrs_com} precisa conter apenas o campo 'autor' definido. A tabela
  mostrará apenas esse campo como readonly, o campo 'titulo' editável, e
  uma linha "Arquivo a carregar".  Este campo será um 
  "<input>" de tipo "file" que deixa o usuário escolher, na sua
  máquina local, o arquivo de vídeo a ser submetido.  Opcionalmente, 
  se {atrs_vid['titulo']} existir e não for {None},
  esse valor será usado como valor inicial da linha "Título" da tabela. O
  parâmetro {editavel} é ignorado neste caso.
  """
  return html_bloco_dados_de_video_IMP.gera(id_vid, atrs_vid, editavel)
