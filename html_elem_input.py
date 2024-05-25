import html_elem_input_IMP

def gera(tipo, chave, ident, val_ini, val_min, editavel, dica, cmd, obrigatorio, decimal):
  """
  Gera o HTML para um campo de dados "<input type='{tipo}' ... />" com atributos dados.
  Este fragmento geralmente é incluído em um formulário "<form>...</form>".
  
  O parâmetro {tipo} é o tipo de campo como definido pela linguagem HTML.
  As principais possibilidades são:

    » "text", uma linha de texto;

    » "password", uma senha, que é normalmente 
       invisível enquanto está sendo digitada;

    » "number", um valor numérico;

    » "checkbox", uma caixa que pode ser marcada ou desmarcada pelo usuário;

    » "email", um endereço de email;

    » "date", uma data;

    » "file", um arquivo no disco do usuário para upload;

    » "hidden", um campo que não é visível para o usuário
      mas cujo valor (inicial), obtido de {args}, será enviado
      como argumento do comando.

  O parâmetro {chave} é a chave que será usada para enviar o
  valor do mesmo ao servidor. Resulta em "<input ...
  name='{chave}'.../>". Quando o comando POST do formulário for emitido,
  este campo será enviado como um par {chave}: {val_fin} nos argumentos
  do POST, onde {val_fin} é o valor fornecido pelo usuário.
  
  O parâmetro {val_ini} é o valor inicial do campo (resulta em "<input
  ... value='{val_ini}'.../>"). Se for {None}, esse atributo é omitido e
  o valor do campo será inicialmente nulo. Senão, {val_ini} deve ser uma
  string (mesmo quando o campo é numérico). Se o usuário não editar o
  campo, {val_ini} será devolvido ao servidor no POST do formulário,
  como valor desse campo.
  
  O parâmetro {val_min} é relevante apenas se o {tipo} for 'number'. Se
  não for {None}, deve ser um string que define o valor mínimo que o
  usuário pode digitar neste campo ("<input ... min='{val_min}' .../>").
  
  O valor do campo poderá ser editado pelo usuário apenas se o tipo não
  for "hidden" e {editavel} for {True}. Caso contrário, {val_ini} 
  não pode ser {None}.
  
  O parâmetro {dica} é um texto que será mostrado no campo, se {val_ini}
  for {None}, para orientar o preenchimento (resulta em "<input ...
  placeholder='{dica}' .../>"). Este campo NÃO será devolvido ao
  servidor Se for {None}, o campo estará inicialmente em branco.
  
  O parâmetro {cmd}, se não for {None}, é o comando que será enviado ao 
  servidor via POST, quando o usuário alterar este campo, em vez do
  "action" default do formulário.
  
  O parâmetro {ident}, se não for {None}, é usado como o atributo "id=" do "<input>".

  O parâmetro {obrigatorio} indica se o campo deve ser obrigatóriamente preenchido ou não.
  Isso altera visualmente a forma como o campo é exibido para o usuário pelo navegador.

  O parâmetro {decimal} é relevante quando {tipo} for 'number' e determina se o
  campo aceitará valores decimais. No momento estão sendo considerados valores de até
  2 casas decimais.
  """  
  return html_elem_input_IMP.gera(tipo, chave, ident, val_ini, val_min, editavel, dica, cmd, obrigatorio, decimal)
