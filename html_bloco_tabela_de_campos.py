import html_bloco_tabela_de_campos_IMP

def gera(dados_linhas, atrs, admin, ignora_admin=False):
  """Retorna HTML de um elemento tabela "<table>...</table>" 
  com duas colunas: rótulos "<label>...<label/> e campos
  editáveis <input.../>".  Este bloco deve ser envolvido em 
  um "<form>...</form>"; veja o módulo {html_form}.

  O parâmetro {dados_linhas} é uma seqüência de quíntuplas
  {(rot,tipo,chave,dica,adm_only)}, cada uma delas
  descrevendo as propriedades de uma linha da tabela.
  O elemento {rot} de cada quíntupla é o texto a mostrar no rótulo, ou {None} para omitir o rótulo.
  O elemento {adm_only} é um booleano que diz se o campo só deve ser editável
  para administradores. Se for {True}, o campo será "readonly" para usuários normais.
  
  Os valores iniciais dos campos são obtidos do
  dicionário {atrs}.
  
  O parâmetro booleano {admin} diz se o usuário
  que pediu o formulário é administrador ({True}) ou cliente ({False}).
  
  O parâmetro {ignora_admin} tem valor default {False}. Se o seu valor for passado
  como {True}, o valor do parâmetro {admin} será ignorado.

  O campo editável será
  "<input type='{tipo}' name='{chave}' id='{chave}' value='{val}' placeholder='{dica}'/>"
  onde {val} é o valor {atrs[chave]} apropriadamente convertido para HTML.
  Se o {tipo} for "numeric" também tem "min='1'."""
  return html_bloco_tabela_de_campos_IMP.gera(dados_linhas, atrs, admin, ignora_admin)
