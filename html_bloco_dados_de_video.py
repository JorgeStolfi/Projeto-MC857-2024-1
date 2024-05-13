import html_bloco_dados_de_video_IMP

def gera(vid_id, atrs, editavel, para_admin, para_proprio):
  """
  Retorna um fragmento HTML que exibe 
  dados do video {vid} cujo identificador é {vid_id} e 
  cujos atributos são supostamente {atrs_vid}, ou de um vídeo a ser criado
  se {vid_id} é {None}.
  
  Esta função pode ser usada para entrar dados de um novo vídeo, ou
  visualizar e possivelmente alterar dados de um vídeo existente.
  
  O resultado desta função será um bloco "<table>...</table>". Cada
  linha da tabela terá duas colunas, um rótulo ("Autor", "Data", etc.) e
  um campo "<input>" ou "<textarea>" com o valor do atributo
  correspondente. Alguns atributos podem ser editáveis, portanto este
  bloco deve ser incluído em um elemento "<form>...</form>". Veja
  {html_elem_form.gera}.
  
  O parâmetro {vid_id} deve ser {None} ou o identificador (um string no
  formato "V-{NNNNNNNN}") de um vídeo existente.
  
  O parâmetro {atrs} deve ser {None} ou um {dict}.  Os valores iniciais
  dos campos do formulário serão obtidos de {atrs}, se constarem ali,
  ou do vídeo {vid} caso contrário.

  Os parâmetros booleanos {editavel}, {para_admin} e {para_proprio}
  especificam quais campos do formulário serão visíveis e/ou editáveis,
  como detalhado abaixo. Se {para_admin} for {True}, a função entende que
  o usuário que pediu o formulário é administrador. Se {para_proprio} for
  {True}, entende que o formulário foi pedido pelo próprio autor do
  vídeo {vid}.
   
  Se {editavel} é {False}, nenhum campo será editável.  Se for {True},
  os campos editáveis dependerão de {para_admin} e {para_proprio} 
  
  Se {vid_id} não é {None}, supõe que este bloco se destina a examinar o
  atributos de um vídeo previamente inserido no sistema. Neste caso o
  dicionário {atrs_vid} deve ter todos os atributos do vídeo {vid}. O
  bloco vai mostrar todos esses atributos, bem como o identificador
  {vid_id}. O campo 'titulo' será editável se {editavel} for True,
  caso contrário será readonly.
  
  Se {editavel} é {False}, nenhum campo será editável. Se for {True},
  os campos editáveis dependerão de {para_admin} e {para_proprio}.

  Se {vid_id} é {None}, supõe este bloco vai ser usado para fazer upload
  de um novo vídeo.  O parâmetro {editavel} deve ser {True} neste caso. 
  Neste caso, o dicionário {atrs_com} precisa conter
  apenas o campo 'autor' definido, que deve ser um objeto de
  tipo {obj_usuario.Classe}.  A tabela mostrará apenas esse campo
  como readonly, o campo 'titulo' editável, e uma linha "Arquivo a
  carregar". Este campo será um "<input>" de tipo "file" que deixa o
  usuário escolher, na sua máquina local, o arquivo de vídeo a ser
  submetido.  Os demais atributos de {atrs} serão ignorados 
  e não exibidos.
  
  Se {vid_id} não é {None}, retorma uma tabela de campos adequada para
  visualizar ou alterar os dados do vídeo {vid} com esse identificador,
  que supostamente já existe.  Neste caso, alguns campos
  serão editáves se e somente se {editavel} for {True}. Especificamente:
  
    * Haverá um campo "Vídeo", sempre readonly, que mostra
    {vid_id}, com chave 'video'.
    
    * Os atributos 'data', 'duracao', 'altura' e 'largura' serão
    exibidos mas nunca editáveis.
    
    * Haverá um campo "Título" com chave 'titulo', editável se
    {editavel} for {True}.
  
  O resultado NÃO inclui uma janela que exibe o vídeo em si.
  Veja {html_elem_video.gera} para esse fim.
  """
  return html_bloco_dados_de_video_IMP.gera(vid_id, atrs, editavel, para_admin, para_proprio)
