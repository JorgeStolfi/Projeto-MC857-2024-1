import html_bloco_dados_de_video_IMP

def gera(vid, usr, mostra_usr, edita_titulo):
  """
  Retorna uma tabela HTML "<table>...</table>" com os atributos 
  do video {vid}. do usuário {usr}. Alguns campos podem ser editáveis, 
  portanto este bloco deve ser incluído em um elemento "<form>...</form>".  
  Veja o módulo {html_elem_form}
  
  Em vez do atributo 'usr' do vídeo, a tabela incluirá um campo com nome 'id_usuario'
  contendo o identificador do usuário.
  
  Se {vid} é {None}, supõe que o vídeo ainda não existe a tabela será
  usada para fazer upload. Nesse caso, o parâmetro {usr} deve ser diferente
  de {None}. O campo 'id_usuario' da tabela será readonly e hidden. Os campos
  'duracao', 'largura', e 'altura' serão omitidos. Os demais campos serão 
  editáveis e em branco. Os parâmetros {mostra_usr} e {edita_titulo} serão ignorados.
  
  Se {vid} não é {None}, supõe que o vídeo já existe no sistema, e seus 
  dados estão sendo examinados.  Nesse caso {usr} deve ser {None} ou 
  igual a {obj_video.obtem_usuario(vid)}. Os valores dos campos 
  'titulo', 'arq', etc. serão obtidos a partir do identificador {vid}.  
  
  Se o vídeo já existe ({vid != None}), o campo 'id_usuario' da tabela
  será visível ser {mostra_usr} for {True}, e hidden se {mostra_usr} for{False}.
  
  Se o vídeo já existe ({vid != None}), o campo 'titulo'
  da tabela será editável se {edita_titulo} for {True}, e readonly 
  se {edita_titulo} for {False}.
  """
  return html_bloco_dados_de_video_IMP.gera(vid, usr, mostra_usr, edita_titulo)
