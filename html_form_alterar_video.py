import html_form_alterar_video_IMP

def gera(vid_id, atrs_mod, eh_adm):
  """
  Retorna um elemento "<form>...</form>" adequado para
  alterar os dados de um vídeo {vid} cujo identificador é {vid_id}.
  
  O parâmetro {vid_id} deve ser o identificador "V-{NNNNNNNN}" de um
  vídeo que existe. O formulário vai mostrar {vid_id} como um campo
  "readonly".
  
  O parâmetro booleano {eh_adm} diz se o usuário que vai editar o vídeo
  é administrador.
  
  O formulário terá campos editáveis com os atributos mutáveis do vídeo. O
  parâmetro {atrs_mod} deve ser um dicionário com um subconjuto
  (possivelmente vazio) das chaves desses atributos. Os valores
  especificados em {atrs_mod} serão mostrados no formulário em vez dos
  valores correntes dos atributos de {vid}. 
  
  Alguns atributos do vídeo não podem ser alterados, nem mesmo
  por admnistradores. Esses atributos serão mostrados, mas como 
  "readonly". Se seus valores forem especificados em {atrs_mod},
  eles devem coincidir vid os respectivos valores atuais no
  vídeo {vid}.
  
  Por enquanto os únicos atributos editáveis são 'titulo' e 'bloqueado'.
  O 'titulo' será sempre editável. O atributo 'bloqueado' será editável só se
  {eh_adm} for {True}, caso contrário não será exibido e nem editável.
  
  O formulário conterá um botão "Alterar", "Confirmar alterações" ou
  similar. Quando o usuário clicar nesse botão, será emitido um comando
  POST com ação "alterar_video". Os argumentos desse POST são todos os
  atributos alteráveis da classe {obj_video.Classe}, com valores
  de {atrs_mod} depois das alterações feitas pelo dono da sessão.
  
  O formulário também terá um botão simples "Cancelar", que, 
  quando clicado, emite o comando "pag_principal".
  
  O formulário também tera um botão simples "Recalcular nota", que,
  quando clicado, emite o comando "recalcular_nota".
  """
  return html_form_alterar_video_IMP.gera(vid_id, atrs_mod, eh_adm)
