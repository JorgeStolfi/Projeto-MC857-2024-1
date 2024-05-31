import html_bloco_tabela_de_campos_IMP

def gera(dados_linhas, atrs):
  """
  Retorna HTML de um elemento tabela "<table>...</table>",
  onde cada linha tem duas colunas: um rótulo "<label>...<label/>", e 
  um campo editável "<input.../>" ou "<textarea...>...</textarea>". 
  
  Este bloco destina-se a ser incluído em um formulário HTML, um
  elemento "<form>...</form>"; veja o módulo {html_form}. Esse
  formulário deve ter pelo menos um botão de tipo submit que emitirá
  algum comando HTTP para o servidor. Os valores dos campos da tabela,
  possivelmente alterados ou preenchidos pele usuário, serão enviados ao
  servidor como argumentos desse comando.

  O parâmetro {dados_linhas} é uma seqüência de sextuplas
  {(rot,tipo,chave,editavel,dica,decimal)}, cada uma delas descrevendo as
  propriedades de uma linha da tabela. Em cada
  sextupla, 
  
    * {rot} é o rótulo visível da linha, o texto que vai aparecer 
      como um "<label>...</label>" à esquerda do elemento "<input>".
      Se for {None}, a linha da tabela ficará sem rótulo.
     
    * {tipo} é o tipo HTML do elemento "<input>" ("text", "number",
      "password", ...), usado no atributo "type=" do mesmo. Ele
      determina os valores que o campo pode assumir e como pode ser
      editado pelo usuário. Veja as possibilidades em
      {html_elem_input.gera}.
    
    * {chave} é o nome com que o valor deste campo da tabela
      está identificado em {args} e será identificado nos argumentos 
      de um comando emitido pelo formulário.
      
    * {editavel} é um booleano que especifica se o campo é editável
      ou não.
      
    * {dica} é um string que será exibido no campo caso o valor especificado em 
      {args} for {None} ou não existir.  Será usado no atributo 
      "placeholder=" do elemento "<input>".

    * {decimal} é um booleano que especifica se o campo aceita decimais
      ou não (valido apenas para inputs do tipo "number")
  
  O valor inicial {val} de cada elemento "<input>" ou "<textarea>" é
  normalmente obtido do dicionário {atrs} com a {chave} correspondente.
  Esse valor será convertido para um string válido em HTML.
  Se o valor em {atrs} for {None} ou ausente, o elemento <input> será
  inicialmente a {dica} fornecida; ou vazio se esta também for {None}.
  Se o valor em {atrs} for um objeto derivado de {obj_raiz.Classe},
  ele será convertido para o respectivo identificador.
  
  Porém, se o {tipo} do campo for "numeric", o dicionário também pode
  conter um valor adicional com chave '{chave}_min' que especifica o
  valor mínimo {val_min} permitido nesse campo, pelo atributo "min=" do
  "<input>". Nesse caso, se {val} não for {None} ele deve ser 
  maior ou igual a {val_min}, e se for {None} o valor de 
  {val_min} será usado como valor inicial.
  
  Se o {tipo} for "senha", o valor em {args} é ignorado, e o 
  valor {val} do campo editável começa sempre em branco ou com 
  a {dica}.

  O {tipo} pode ser também "textarea" para gerar um elemento 
  "<textarea ...>...<textarea/>" em vez de um "<input.../>.
  O efeito é similar a um "<input type='text'.../>" 
  mas permite digitar um texto com múltiplas linhas.
  
  A {dica} é sempre um string, mesmo se o tipo for "numeric",
  e não precisa ter o formato válido para o valor do campo.
  Caso o valor {val} em {args} seja {None} ou omitido, e
  o usuário deixe o campo sem editar, o valor enviado 
  ao servidor como argumento do comando será {None}, 
  NÃO a {dica}.
  """
  return html_bloco_tabela_de_campos_IMP.gera(dados_linhas, atrs)
