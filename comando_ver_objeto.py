import comando_ver_objeto_IMP

def processa(ses, cmd_args):
  """
  Esta função é chamada quando servidor do site recebe um comando HTTP
  "ver_objeto". Esse comando é tipicamente emitido pelo browser de um
  usuário quando este aperta um botão "Ver objeto" ou equivalente.
  
  O parâmetro {ses} é a sessão de login corrente, que emitiu o comando.
  Pode ser {None} ou um objeto de tipo {obj_sessão.Classe}, ainda
  aberta.  
  
  O parãmetro {cmd_args} deve ser um dicionário com um único campo
  de chave 'objeto', cujo valor é o identificador de um objeto do
  sistema, como "U-00000003" (usuário) ou "V-00001234" (vídeo).
  
  Esta função chama a função específica para ver esse tipo de objeto,
  dependendo da letra inicial do identificador:
  
    "U": {comando_ver_usuario.processa} 
    "S": {comando_ver_sessao.processa}
    "V": {comando_ver_video.processa}
    "C": {comando_ver_comentario.processa}
    
  Note que cada um destes comandos tem suas restrições sobre quem pode
  ver o que.
  """
  return comando_ver_objeto_IMP.processa(ses, cmd_args)
