import html_bloco_dados_de_comentario_IMP

def gera(id_com, atrs_com, edita_texto):
  """
  Retorna um fragmento HTML que exibe os atributos do comentário {com}
  cujo identificador é {id_com} e cujos atributos são supostamente
  {atrs_com}.
  
  O resultado desta função será um bloco "<table>...</table>". Cada
  linha da tabela terá duas colunas, um rótulo ("Autor", "Data", etc.) e
  um campo "<input>" ou "<textarea>" com o valor do atributo
  correspondente. Alguns atributos podem ser editáveis, portanto este
  bloco deve ser incluído em um elemento "<form>...</form>". Veja
  {html_elem_form.gera}
  
  O parãmetro {id_com} deve ser {None} ou o identificador 
  (um string no formato "C-{NNNNNNNN}") de um comentário existente.
  
  O parãmetro {atrs_com} deve ser {None} ou um dict.
  
  O parâmetros {edita_texto} é um {bool} que controla
  a editabilidade de certos campos. Vide abaixo.
  
  Se {id_com} não é {None}, supõe que este bloco se destina a examinar o
  atributos de um comentário previamente inserido no sistema. Neste caso
  o dicionário {atrs_com} deve ter todos os atributos do comentário
  {com}. O bloco vai mostrar todos esses atributos, bem como o
  identificador {id_com}.  O campo 'texto'
  será editável se {edita_texto} for {True}, senão será readonly.
   
  Se {id_com} é {None}, supõe que este bloco vai ser usado para inserir
  um novo comentário. Neste casos, os valores {atrs_com['autor']},
  {atrs_com['video']}, e {atrs_com['pai']} devem estar definidos e devem
  ser objetos existentes. O bloco mostrará apenas esses campos (como
  readonly) e 'texto' (editável). O valor de {atrs_com['data']} se
  existir, será ignorado. Opcionalmente, {atrs_com['texto']} existir e não for {None},
  esse valor será usado como valor inicial da linha "Texto" da tabela. O
  parâmetro {edita_texto} é ignorado neste caso.
 
  Em qualquer caso,
  """
  return html_bloco_dados_de_comentario_IMP.gera(id_com, atrs_com, edita_texto)

