import html_elem_textarea_IMP

def gera(rot_campo, chave, ident, val_ini, editavel, dica, cmd, obrigatorio):
  """Gera o HTML para um elemento de textarea  "<textarea ... ></textarea>".
  Este fragmento geralmente é incluído em um formulário "<form>...</form>".
  Veja a função {html_elem_form.gera}.
  
  O parâmetro {rot_campo} é um rótulo opcional. Se não for {None}, será inserido na frente
  do elemento "<textarea>" na forma de um elemento "<label>{rot_campo}</label>".
  
  O parâmetro {chave} é o nome do campo, que será usado para enviar o
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
  
  O valor do campo poderá ser editado pelo usuário apenas se {editavel} for {True}.
  Se for {False}, {val_ini} não pode ser {None}.
  
  O parâmetro {dica} é um texto que será mostrado no campo, se {val_ini}
  for {None}, para orientar o preenchimento (resulta em "<input ...
  placeholder='{dica}' .../>"). Este campo NÃO será devolvido ao
  servidor Se for {None}, o campo estará inicialmente em branco.
  
  O parâmetro {cmd}, se não for {None}, é o comando que será enviado ao 
  servidor via POST, quando o usuário alterar este campo, em vez do
  "action" default do formulário.
  
  O parâmetro {ident}, se não for {None}, será um string usado 
  no atributo "id="  do "<textarea>".

  O parâmetro {obrigatorio} indica se o campo deve ser obrigatóriamente preenchido ou não.
  Isso altera visualmente a forma como o campo é exibido para o usuário pelo navegador. O valor
  default deste parâmetro é False, por questões de compatibilidade.
  """  
  return html_elem_textarea_IMP.gera(rot_campo, chave, ident, val_ini, editavel, dica, cmd, obrigatorio)
